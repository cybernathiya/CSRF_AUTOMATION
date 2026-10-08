import os
import json
from datetime import datetime

from flask import Flask, jsonify, Response


# ============================================================
# CSRF SCANNER MONITOR
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

STATUS_FILE = os.path.join(
    OUTPUT_DIR,
    "scanner_status.json"
)

RESULT_FILE = os.path.join(
    OUTPUT_DIR,
    "report.json"
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "scanner.log"
)


# Create directories automatically
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


app = Flask(__name__)


# ============================================================
# DEFAULT STATUS
# ============================================================

DEFAULT_STATUS = {
    "running": False,
    "status": "Idle",

    "started_at": None,
    "completed_at": None,

    "total_sites": 0,
    "scanned_sites": 0,

    "total_forms": 0,

    "csrf_tokens": 0,

    "vulnerable_forms": 0,
    "protected_forms": 0,

    "errors": 0,

    "current_site": "-",
    "current_form": "-",

    "progress": 0
}


# ============================================================
# READ STATUS
# ============================================================

def get_status():

    status = DEFAULT_STATUS.copy()

    if os.path.exists(STATUS_FILE):

        try:

            with open(
                STATUS_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                saved_status = json.load(file)

                if isinstance(saved_status, dict):
                    status.update(saved_status)

        except Exception as error:

            status["status"] = "Monitor Error"
            status["errors"] = 1

            print(
                "Status file error:",
                error
            )

    return status


# ============================================================
# READ RESULTS
# ============================================================

def get_results():

    if not os.path.exists(RESULT_FILE):
        return {}

    try:

        with open(
            RESULT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return {}


# ============================================================
# READ LOGS
# ============================================================

def get_logs(number_of_lines=50):

    if not os.path.exists(LOG_FILE):
        return [
            "Waiting for scanner logs..."
        ]

    try:

        with open(
            LOG_FILE,
            "r",
            encoding="utf-8",
            errors="replace"
        ) as file:

            lines = file.readlines()

        return [
            line.rstrip()
            for line in lines[-number_of_lines:]
        ]

    except Exception as error:

        return [
            "Unable to read log file:",
            str(error)
        ]


# ============================================================
# DASHBOARD HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>CSRF Scanner Monitor</title>


<style>

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background: #0f172a;

    color: #ffffff;
}


.header {

    background: #1e293b;

    padding: 25px 35px;

    border-bottom:
        1px solid #334155;
}


.header h1 {

    margin: 0 0 8px 0;

    font-size: 28px;
}


.header p {

    margin: 0;

    color: #94a3b8;
}


.container {

    max-width: 1400px;

    margin: auto;

    padding: 25px;
}


/* STATUS */

.status-panel {

    background: #1e293b;

    border-radius: 12px;

    padding: 25px;

    margin-bottom: 25px;

    border:
        1px solid #334155;
}


.status-title {

    font-size: 22px;

    margin-bottom: 20px;
}


#status {

    font-weight: bold;

}


.running {

    color: #22c55e;

}


.stopped {

    color: #ef4444;

}


/* CARDS */

.cards {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(180px, 1fr)
        );

    gap: 15px;

    margin-bottom: 25px;
}


.card {

    background: #1e293b;

    border:
        1px solid #334155;

    border-radius: 12px;

    padding: 20px;
}


.card-title {

    color: #94a3b8;

    font-size: 14px;

    margin-bottom: 12px;
}


.card-value {

    font-size: 32px;

    font-weight: bold;
}


/* PROGRESS */

.panel {

    background: #1e293b;

    border:
        1px solid #334155;

    border-radius: 12px;

    padding: 25px;

    margin-bottom: 25px;
}


.panel h2 {

    margin-top: 0;
}


.progress-background {

    width: 100%;

    height: 28px;

    background: #334155;

    border-radius: 20px;

    overflow: hidden;
}


#progress {

    height: 100%;

    width: 0%;

    background: #06b6d4;

    transition:
        width 0.4s ease;
}


.progress-text {

    margin-top: 10px;

    font-size: 18px;

    font-weight: bold;
}


/* ACTIVITY */

.activity {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(250px, 1fr)
        );

    gap: 15px;
}


.activity-box {

    background: #0f172a;

    padding: 18px;

    border-radius: 8px;
}


.activity-label {

    color: #94a3b8;

    font-size: 13px;

    margin-bottom: 8px;
}


/* LOGS */

.logs {

    background: #020617;

    border-radius: 8px;

    padding: 15px;

    height: 350px;

    overflow-y: auto;

    font-family:
        Consolas,
        "Courier New",
        monospace;

    font-size: 13px;

    line-height: 1.6;

    white-space: pre-wrap;

    border:
        1px solid #334155;
}


/* REFRESH */

.refresh {

    color: #94a3b8;

    font-size: 13px;

    margin-top: 15px;
}

</style>

</head>


<body>


<div class="header">

    <h1>
        CSRF Vulnerability Scanner Monitor
    </h1>

    <p>
        Real-time scanner monitoring dashboard
    </p>

</div>


<div class="container">


    <!-- STATUS -->

    <div class="status-panel">

        <div class="status-title">

            Scanner Status:

            <span id="status">
                Loading...
            </span>

        </div>


        <div class="activity">

            <div class="activity-box">

                <div class="activity-label">
                    CURRENT SITE
                </div>

                <div id="currentSite">
                    -
                </div>

            </div>


            <div class="activity-box">

                <div class="activity-label">
                    CURRENT FORM
                </div>

                <div id="currentForm">
                    -
                </div>

            </div>

        </div>

    </div>


    <!-- STATISTICS -->

    <div class="cards">


        <div class="card">

            <div class="card-title">
                TOTAL SITES
            </div>

            <div
                class="card-value"
                id="totalSites">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                SITES SCANNED
            </div>

            <div
                class="card-value"
                id="scannedSites">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                FORMS FOUND
            </div>

            <div
                class="card-value"
                id="totalForms">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                CSRF TOKENS
            </div>

            <div
                class="card-value"
                id="csrfTokens">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                VULNERABLE FORMS
            </div>

            <div
                class="card-value"
                id="vulnerableForms">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                PROTECTED FORMS
            </div>

            <div
                class="card-value"
                id="protectedForms">
                0
            </div>

        </div>


        <div class="card">

            <div class="card-title">
                ERRORS
            </div>

            <div
                class="card-value"
                id="errors">
                0
            </div>

        </div>


    </div>


    <!-- PROGRESS -->

    <div class="panel">

        <h2>
            Scan Progress
        </h2>


        <div class="progress-background">

            <div id="progress"></div>

        </div>


        <div
            class="progress-text"
            id="progressText">

            0%

        </div>

    </div>


    <!-- TIME -->

    <div class="panel">

        <h2>
            Scan Information
        </h2>


        <div class="activity">


            <div class="activity-box">

                <div class="activity-label">
                    STARTED
                </div>

                <div id="startedAt">
                    -
                </div>

            </div>


            <div class="activity-box">

                <div class="activity-label">
                    COMPLETED
                </div>

                <div id="completedAt">
                    -
                </div>

            </div>


        </div>

    </div>


    <!-- LOGS -->

    <div class="panel">

        <h2>
            Live Scanner Logs
        </h2>


        <div
            class="logs"
            id="logs">

            Connecting to scanner...

        </div>


        <div class="refresh">

            Automatically refreshes every 2 seconds.

        </div>

    </div>


</div>


<script>


async function updateMonitor() {

    try {

        const response =
            await fetch(
                "/api/monitor",
                {
                    cache: "no-store"
                }
            );


        if (!response.ok) {

            throw new Error(
                "HTTP " +
                response.status
            );

        }


        const data =
            await response.json();


        const status =
            data.status || {};


        // STATUS

        const statusElement =
            document.getElementById(
                "status"
            );


        statusElement.textContent =
            status.status || "Idle";


        statusElement.className =
            status.running
                ? "running"
                : "stopped";


        // CURRENT SITE

        document.getElementById(
            "currentSite"
        ).textContent =
            status.current_site || "-";


        // CURRENT FORM

        document.getElementById(
            "currentForm"
        ).textContent =
            status.current_form || "-";


        // STATISTICS

        document.getElementById(
            "totalSites"
        ).textContent =
            status.total_sites || 0;


        document.getElementById(
            "scannedSites"
        ).textContent =
            status.scanned_sites || 0;


        document.getElementById(
            "totalForms"
        ).textContent =
            status.total_forms || 0;


        document.getElementById(
            "csrfTokens"
        ).textContent =
            status.csrf_tokens || 0;


        document.getElementById(
            "vulnerableForms"
        ).textContent =
            status.vulnerable_forms || 0;


        document.getElementById(
            "protectedForms"
        ).textContent =
            status.protected_forms || 0;


        document.getElementById(
            "errors"
        ).textContent =
            status.errors || 0;


        // PROGRESS

        let progress =
            Number(
                status.progress || 0
            );


        if (progress < 0)
            progress = 0;

        if (progress > 100)
            progress = 100;


        document.getElementById(
            "progress"
        ).style.width =
            progress + "%";


        document.getElementById(
            "progressText"
        ).textContent =
            progress + "%";


        // TIMES

        document.getElementById(
            "startedAt"
        ).textContent =
            status.started_at || "-";


        document.getElementById(
            "completedAt"
        ).textContent =
            status.completed_at || "-";


        // LOGS

        const logElement =
            document.getElementById(
                "logs"
            );


        const logs =
            data.logs || [];


        if (logs.length === 0) {

            logElement.textContent =
                "Waiting for scanner logs...";

        } else {

            logElement.textContent =
                logs.join("\n");

            logElement.scrollTop =
                logElement.scrollHeight;

        }

    }

    catch (error) {

        console.error(
            "Monitor error:",
            error
        );


        document.getElementById(
            "status"
        ).textContent =
            "Connection Error";


        document.getElementById(
            "status"
        ).className =
            "stopped";


        document.getElementById(
            "logs"
        ).textContent =
            "Unable to connect to monitor API.\n\n"
            + error;

    }

}


// Initial update

updateMonitor();


// Refresh every 2 seconds

setInterval(
    updateMonitor,
    2000
);


</script>


</body>

</html>
"""


# ============================================================
# ROUTE: DASHBOARD
# ============================================================

@app.route("/")
def dashboard():

    return Response(
        HTML,
        mimetype="text/html"
    )


# ============================================================
# ROUTE: STATUS
# ============================================================

@app.route("/api/status")
def api_status():

    return jsonify(
        get_status()
    )


# ============================================================
# ROUTE: RESULTS
# ============================================================

@app.route("/api/results")
def api_results():

    return jsonify(
        get_results()
    )


# ============================================================
# ROUTE: LOGS
# ============================================================

@app.route("/api/logs")
def api_logs():

    return jsonify({
        "logs": get_logs()
    })


# ============================================================
# ROUTE: COMPLETE MONITOR
# ============================================================

@app.route("/api/monitor")
def api_monitor():

    return jsonify({

        "status": get_status(),

        "results": get_results(),

        "logs": get_logs(),

        "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    })


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/health")
def health():

    return jsonify({
        "status": "online",
        "monitor": "CSRF Scanner Monitor"
    })


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("CSRF SCANNER MONITOR")
    print("=" * 60)
    print()
    print("Project directory:")
    print(BASE_DIR)
    print()
    print("Output directory:")
    print(OUTPUT_DIR)
    print()
    print("Status file:")
    print(STATUS_FILE)
    print()
    print("Dashboard:")
    print("http://127.0.0.1:5050")
    print()
    print("Health check:")
    print("http://127.0.0.1:5050/health")
    print()
    print("=" * 60)
    print()


    app.run(
        host="127.0.0.1",
        port=5050,
        debug=False,
        threaded=True
    )
    