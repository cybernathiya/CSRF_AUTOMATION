<!DOCTYPE html>
<html>
<head>
    <title>CSRF Scanner Monitor</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #111827;
            color: white;
            margin: 0;
        }

        header {
            background: #1f2937;
            padding: 20px;
        }

        .container {
            padding: 20px;
        }

        .status {
            padding: 20px;
            background: #1f2937;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
        }

        .card {
            background: #1f2937;
            padding: 20px;
            border-radius: 10px;
        }

        .card h3 {
            color: #9ca3af;
            margin-top: 0;
        }

        .value {
            font-size: 30px;
            font-weight: bold;
        }

        .progress-box {
            margin-top: 20px;
            background: #374151;
            height: 25px;
            border-radius: 20px;
            overflow: hidden;
        }

        #progress {
            height: 100%;
            width: 0%;
            background: #06b6d4;
            transition: width 0.5s;
        }

        .panel {
            background: #1f2937;
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
        }

        #logs {
            background: #000;
            padding: 15px;
            height: 250px;
            overflow-y: auto;
            font-family: monospace;
            white-space: pre-wrap;
        }

        .running {
            color: #22c55e;
        }

        .stopped {
            color: #ef4444;
        }
    </style>
</head>

<body>

<header>
    <h1>CSRF Vulnerability Scanner Monitor</h1>
    <p>Real-time Scanner Monitoring</p>
</header>

<div class="container">

    <div class="status">

        <h2>
            Scanner Status:
            <span id="status">Loading...</span>
        </h2>

        <p>
            Current Site:
            <strong id="currentSite">-</strong>
        </p>

        <p>
            Current Form:
            <strong id="currentForm">-</strong>
        </p>

    </div>


    <div class="cards">

        <div class="card">
            <h3>Total Sites</h3>
            <div class="value" id="totalSites">0</div>
        </div>

        <div class="card">
            <h3>Sites Scanned</h3>
            <div class="value" id="scannedSites">0</div>
        </div>

        <div class="card">
            <h3>Forms Found</h3>
            <div class="value" id="totalForms">0</div>
        </div>

        <div class="card">
            <h3>CSRF Tokens</h3>
            <div class="value" id="csrfTokens">0</div>
        </div>

        <div class="card">
            <h3>Vulnerable Forms</h3>
            <div class="value" id="vulnerableForms">0</div>
        </div>

        <div class="card">
            <h3>Protected Forms</h3>
            <div class="value" id="protectedForms">0</div>
        </div>

        <div class="card">
            <h3>Errors</h3>
            <div class="value" id="errors">0</div>
        </div>

    </div>


    <div class="panel">

        <h2>Scan Progress</h2>

        <div class="progress-box">
            <div id="progress"></div>
        </div>

        <p id="progressText">0%</p>

    </div>


    <div class="panel">

        <h2>Scan Information</h2>

        <p>
            Started:
            <strong id="startedAt">-</strong>
        </p>

        <p>
            Completed:
            <strong id="completedAt">-</strong>
        </p>

    </div>


    <div class="panel">

        <h2>Live Scanner Logs</h2>

        <div id="logs">
            Waiting for scanner logs...
        </div>

    </div>

</div>


<script>

async function updateMonitor() {

    try {

        const response = await fetch("/api/monitor");

        const data = await response.json();

        const s = data.status;


        document.getElementById("status").innerText =
            s.status || "Idle";


        document.getElementById("status").className =
            s.running ? "running" : "stopped";


        document.getElementById("currentSite").innerText =
            s.current_site || "-";


        document.getElementById("currentForm").innerText =
            s.current_form || "-";


        document.getElementById("totalSites").innerText =
            s.total_sites || 0;


        document.getElementById("scannedSites").innerText =
            s.scanned_sites || 0;


        document.getElementById("totalForms").innerText =
            s.total_forms || 0;


        document.getElementById("csrfTokens").innerText =
            s.csrf_tokens || 0;


        document.getElementById("vulnerableForms").innerText =
            s.vulnerable_forms || 0;


        document.getElementById("protectedForms").innerText =
            s.protected_forms || 0;


        document.getElementById("errors").innerText =
            s.errors || 0;


        const progress = s.progress || 0;

        document.getElementById("progress").style.width =
            progress + "%";


        document.getElementById("progressText").innerText =
            progress + "%";


        document.getElementById("startedAt").innerText =
            s.started_at || "-";


        document.getElementById("completedAt").innerText =
            s.completed_at || "-";


        const logs = document.getElementById("logs");

        if (data.logs && data.logs.length > 0) {

            logs.innerText = data.logs.join("\n");

            logs.scrollTop = logs.scrollHeight;

        } else {

            logs.innerText =
                "Waiting for scanner logs...";

        }

    }

    catch (error) {

        document.getElementById("logs").innerText =
            "Monitor connection error: " + error;

    }

}


updateMonitor();

setInterval(updateMonitor, 2000);

</script>

</body>
</html>