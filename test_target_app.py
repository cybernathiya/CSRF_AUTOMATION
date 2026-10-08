"""

test_target_app.py

Local CSRF practice app: 20 sites, runtime registration/login,

per-site accounts, event HTML reports, and the original four CSRF

risk categories with two dashboard forms per site.

Run only in your local lab.

"""

import os

import sqlite3

import html

import secrets

from datetime import datetime, timezone

from pathlib import Path


from flask import (

    Flask, request, redirect, session, render_template_string,

    make_response, abort, url_for, send_from_directory

)

from werkzeug.security import generate_password_hash, check_password_hash

import config

app = Flask(__name__)

app.secret_key = os.environ.get("CSRF_LAB_SECRET_KEY", getattr(config, "SECRET_KEY", "local-csrf-lab-change-this-key"))

DB_PATH = Path(getattr(config, "DATABASE_PATH", "data/users.db"))

EVENT_DIR = Path(getattr(config, "EVENT_REPORT_DIR", "output/events"))

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

EVENT_DIR.mkdir(parents=True, exist_ok=True)

def get_db():

    db = sqlite3.connect(DB_PATH)

    db.row_factory = sqlite3.Row

    return db

def initialize_database():

    with get_db() as db:

        db.execute("""

            CREATE TABLE IF NOT EXISTS users (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                site_id INTEGER NOT NULL,

                username TEXT NOT NULL,

                password_hash TEXT NOT NULL,

                created_at TEXT NOT NULL,

                UNIQUE(site_id, username)

            )

        """)

        db.execute("""

            CREATE TABLE IF NOT EXISTS site_events (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                site_id INTEGER NOT NULL,

                username TEXT NOT NULL,

                event_type TEXT NOT NULL,

                event_time TEXT NOT NULL,

                result TEXT NOT NULL

            )

        """)

def record_event(site_id, username, event_type, result):

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    with get_db() as db:

        cur = db.execute(

            """INSERT INTO site_events

               (site_id, username, event_type, event_time, result)

               VALUES (?, ?, ?, ?, ?)""",

            (site_id, username or "Unknown", event_type, timestamp, result)

        )

        event_id = cur.lastrowid

    safe = [html.escape(str(x)) for x in

            (username or "Unknown", event_type, timestamp, result)]

    report = f"""<!doctype html>

<html lang="en"><head><meta charset="utf-8">

<meta name="viewport" content="width=device-width,initial-scale=1">

<title>Site {site_id} Event Report</title>

<style>

body{{font-family:Arial,sans-serif;max-width:800px;margin:40px auto;

padding:20px;background:#f4f6f8;color:#222}}

.card{{background:white;padding:24px;border-radius:10px}}

table{{width:100%;border-collapse:collapse}}th,td{{padding:12px;

border-bottom:1px solid #ddd;text-align:left}}

</style></head><body><div class="card">

<h1>User Event Report</h1><table>

<tr><th>Event ID</th><td>{event_id}</td></tr>

<tr><th>Site</th><td>Site {site_id}</td></tr>

<tr><th>Username</th><td>{safe[0]}</td></tr>

<tr><th>Event</th><td>{safe[1]}</td></tr>

<tr><th>Time</th><td>{safe[2]}</td></tr>

<tr><th>Result</th><td>{safe[3]}</td></tr>

</table></div></body></html>"""

    path = EVENT_DIR / f"site_{site_id}_event_{event_id}.html"

    path.write_text(report, encoding="utf-8")

    print(f"[EVENT REPORT] {path}")

def get_category(site_id):

    return (site_id - 1) % 4

CATEGORY_LABELS = {

    0: ("Both forms vulnerable", "#e74c3c"),

    1: ("Both forms protected", "#27ae60"),

    2: ("Mixed - SameSite only", "#f39c12"),

    3: ("Mixed - token + SameSite", "#2980b9"),

}

SITES = {

    i: {"id": i, "name": f"Site {i}", "category": get_category(i)}

    for i in range(1, 21)

}

def forms_config(category):

    """Return (form1_has_token, form2_has_token, needs_samesite_cookie)."""

    if category == 0:

        return False, False, False

    if category == 1:

        return True, True, False

    if category == 2:

        return False, False, True

    return True, False, True

BASE_STYLE = """

<style>

*{box-sizing:border-box}body{font-family:'Segoe UI',Arial,sans-serif;

background:#f4f6f8;margin:0;padding:40px 20px;color:#2c3e50}

.card{background:#fff;max-width:480px;margin:0 auto;padding:32px;

border-radius:10px;box-shadow:0 2px 10px #0001}

.wide-card{max-width:760px}h2{margin-top:0;color:#1a252f}

.subtitle{color:#7f8c8d;font-size:14px;margin-bottom:20px}

input[type=text],input[type=email],input[type=password]{width:100%;

padding:10px 12px;margin:8px 0 16px;border:1px solid #dcdde1;

border-radius:6px;font-size:14px}

button{background:#2980b9;color:white;border:0;padding:10px 18px;

border-radius:6px;cursor:pointer}a{color:#2980b9}

.error-box{background:#fdecea;color:#c0392b;padding:10px 14px;

border-radius:6px;margin-bottom:16px}

.form-block{border:1px solid #ecf0f1;border-radius:8px;padding:18px;

margin-bottom:20px;background:#fafbfc}

.badge{display:inline-block;padding:3px 10px;border-radius:12px;

font-size:12px;font-weight:bold;color:white;margin-left:8px}

.top-bar{display:flex;justify-content:space-between;align-items:center}

table{width:100%;border-collapse:collapse}th,td{text-align:left;

padding:10px 12px;border-bottom:1px solid #ecf0f1}

</style>

"""

AUTH_PAGE = """<!doctype html><html><head><title>{{ title }}</title>""" + BASE_STYLE + """</head>

<body><div class="card"><h2>{{ title }}</h2>

<p class="subtitle">{{ subtitle }}</p>

{% if error %}<div class="error-box">{{ error }}</div>{% endif %}

<form method="post">

<label>Username</label><input type="text" name="username" required minlength="3" maxlength="50" autocomplete="username">

<label>Password</label><input type="password" name="password" required minlength="{{ min_password }}" autocomplete="{{ autocomplete }}">

<button type="submit">{{ button }}</button></form>

<p><a href="{{ other_url }}">{{ other_text }}</a></p>

<p><a href="/">All sites</a></p></div></body></html>"""

DASHBOARD_PAGE = """<!doctype html><html><head><title>{{ site.name }} Dashboard</title>""" + BASE_STYLE + """</head>

<body><div class="card wide-card"><div class="top-bar"><h2>{{ site.name }} Dashboard</h2>

<a href="/site/{{ site.id }}/logout">Logout</a></div>

<p class="subtitle">Logged in as <strong>{{ user }}</strong></p>

<div class="form-block"><h3>Change Email

<span class="badge" style="background:{{ '#27ae60' if form1_token else '#e74c3c' }}">{{ 'TOKEN PRESENT' if form1_token else 'NO TOKEN' }}</span></h3>

<form method="post" action="/site/{{ site.id }}/change-email">

{% if form1_token %}<input type="hidden" name="csrf_token" value="{{ form1_token }}">{% endif %}

<input type="email" name="new_email" placeholder="New email address">

<button type="submit">Update Email</button></form></div>

<div class="form-block"><h3>Transfer Money

<span class="badge" style="background:{{ '#27ae60' if form2_token else '#e74c3c' }}">{{ 'TOKEN PRESENT' if form2_token else 'NO TOKEN' }}</span></h3>

<form method="post" action="/site/{{ site.id }}/transfer">

{% if form2_token %}<input type="hidden" name="csrf_token" value="{{ form2_token }}">{% endif %}

<input type="text" name="amount" placeholder="Amount to transfer">

<button type="submit">Transfer</button></form></div>

</div></body></html>"""

@app.route("/")

def home():

    rows = []

    for site in SITES.values():

        label, color = CATEGORY_LABELS[site["category"]]

        rows.append({**site, "label": label, "color": color})

    return render_template_string("""<!doctype html><html><head><title>CSRF Lab</title>""" + BASE_STYLE + """</head>

<body><div class="card wide-card"><h2>Available Test Sites</h2>

<p class="subtitle">20 simulated sites for CSRF scanner practice</p>

<p><a href="/event-reports">View Registration &amp; Login Reports</a></p>

<table><tr><th>Site</th><th>Risk profile</th><th>Register</th><th>Login</th></tr>

{% for row in rows %}<tr><td>{{ row.name }}</td>

<td><span class="badge" style="background:{{ row.color }}">{{ row.label }}</span></td>

<td><a href="/site/{{ row.id }}/register">Register</a></td>

<td><a href="/site/{{ row.id }}/login">Login</a></td></tr>{% endfor %}

</table></div></body></html>""", rows=rows)

@app.route("/site/<int:site_id>/register", methods=["GET", "POST"])

def register(site_id):

    site = SITES.get(site_id)

    if not site:

        abort(404)

    if request.method == "GET":

        return render_template_string(AUTH_PAGE, title=f"{site['name']} — Register",

            subtitle="Create an account for this site.", error=None,

            min_password=8, autocomplete="new-password", button="Register",

            other_url=f"/site/{site_id}/login", other_text="Already registered? Log in")

    username = request.form.get("username", "").strip()

    password = request.form.get("password", "")

    if not 3 <= len(username) <= 50:

        record_event(site_id, username, "REGISTRATION", "FAILED")

        return render_template_string(AUTH_PAGE, title="Registration failed",

            subtitle="", error="Username must be 3–50 characters.",

            min_password=8, autocomplete="new-password", button="Register",

            other_url=f"/site/{site_id}/register", other_text="Try again"), 400

    if len(password) < 8:

        record_event(site_id, username, "REGISTRATION", "FAILED")

        return render_template_string(AUTH_PAGE, title="Registration failed",

            subtitle="", error="Password must contain at least 8 characters.",

            min_password=8, autocomplete="new-password", button="Register",

            other_url=f"/site/{site_id}/register", other_text="Try again"), 400

    try:

        with get_db() as db:

            db.execute("""INSERT INTO users(site_id,username,password_hash,created_at)

                VALUES(?,?,?,?)""", (site_id, username,

                generate_password_hash(password), datetime.now(timezone.utc).isoformat()))

        record_event(site_id, username, "REGISTRATION", "SUCCESS")

        return redirect(url_for("login", site_id=site_id))

    except sqlite3.IntegrityError:

        record_event(site_id, username, "REGISTRATION", "FAILED - username exists")

        return render_template_string(AUTH_PAGE, title="Registration failed",

            subtitle="", error="That username already exists on this site.",

            min_password=8, autocomplete="new-password", button="Register",

            other_url=f"/site/{site_id}/register", other_text="Try again"), 409

@app.route("/site/<int:site_id>/login", methods=["GET", "POST"])

def login(site_id):

    site = SITES.get(site_id)

    if not site:

        abort(404)

    if request.method == "GET":

        return render_template_string(AUTH_PAGE, title=f"{site['name']} — Login",

            subtitle="Sign in to continue.", error=None, min_password=1,

            autocomplete="current-password", button="Login",

            other_url=f"/site/{site_id}/register", other_text="Create an account")

    username = request.form.get("username", "").strip()

    password = request.form.get("password", "")

    with get_db() as db:

        user = db.execute("SELECT * FROM users WHERE site_id=? AND username=?",

                          (site_id, username)).fetchone()

    if user and check_password_hash(user["password_hash"], password):

        session.clear()

        session[f"user_{site_id}"] = username

        session[f"csrf_token_form1_{site_id}"] = secrets.token_hex(16)

        session[f"csrf_token_form2_{site_id}"] = secrets.token_hex(16)

        resp = make_response(redirect(url_for("dashboard", site_id=site_id)))

        _, _, needs_samesite = forms_config(site["category"])

        if needs_samesite:

            resp.set_cookie(f"site_policy_{site_id}", "protected", samesite="Lax")

        record_event(site_id, username, "LOGIN", "SUCCESS")

        return resp

    record_event(site_id, username, "LOGIN", "FAILED")

    return render_template_string(AUTH_PAGE, title=f"{site['name']} — Login",

        subtitle="Sign in to continue.", error="Invalid username or password.",

        min_password=1, autocomplete="current-password", button="Login",

        other_url=f"/site/{site_id}/register", other_text="Create an account"), 401

@app.route("/site/<int:site_id>/dashboard")

def dashboard(site_id):

    site = SITES.get(site_id)

    if not site:

        abort(404)

    user_key = f"user_{site_id}"

    if user_key not in session:

        return redirect(url_for("login", site_id=site_id))

    form1_has_token, form2_has_token, _ = forms_config(site["category"])

    return render_template_string(DASHBOARD_PAGE, site=site,

        user=session[user_key],

        form1_token=session.get(f"csrf_token_form1_{site_id}") if form1_has_token else None,

        form2_token=session.get(f"csrf_token_form2_{site_id}") if form2_has_token else None)

@app.route("/site/<int:site_id>/change-email", methods=["POST"])

def change_email(site_id):

    if site_id not in SITES:

        abort(404)

    if f"user_{site_id}" not in session:

        return redirect(url_for("login", site_id=site_id))

    return f"Email changed to {html.escape(request.form.get('new_email', ''))} (demo only)"

@app.route("/site/<int:site_id>/transfer", methods=["POST"])

def transfer(site_id):

    if site_id not in SITES:

        abort(404)

    if f"user_{site_id}" not in session:

        return redirect(url_for("login", site_id=site_id))

    return f"Transfer request received: {html.escape(request.form.get('amount', ''))} (demo only)"

@app.route("/site/<int:site_id>/logout")

def logout(site_id):

    if site_id not in SITES:

        abort(404)

    username = session.pop(f"user_{site_id}", None)

    session.pop(f"csrf_token_form1_{site_id}", None)

    session.pop(f"csrf_token_form2_{site_id}", None)

    if username:

        record_event(site_id, username, "LOGOUT", "SUCCESS")

    return redirect(url_for("login", site_id=site_id))

@app.route("/event-reports")
def event_reports():
    """List the HTML reports generated by record_event()."""
    reports = sorted(
        EVENT_DIR.glob("*.html"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    return render_template_string("""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Event Reports - CSRF Lab</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px;
                   background: #f4f6f8; color: #2c3e50; }
            .card { max-width: 900px; margin: auto; padding: 30px;
                    background: white; border-radius: 10px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; border-bottom: 1px solid #ddd;
                     text-align: left; overflow-wrap: anywhere; }
            th { background: #2c3e50; color: white; }
            a { color: #2980b9; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>User Event Reports</h1>
            <p>Total reports: {{ reports|length }}</p>
            {% if reports %}
            <table>
                <tr><th>Report File</th><th>Action</th></tr>
                {% for report in reports %}
                <tr>
                    <td>{{ report }}</td>
                    <td><a href="{{ url_for('view_event_report',
                                            filename=report) }}">View HTML Report</a></td>
                </tr>
                {% endfor %}
            </table>
            {% else %}
            <p>No event reports found yet. Register or log in to a test site first.</p>
            {% endif %}
            <p><a href="/">Back to All Sites</a></p>
        </div>
    </body>
    </html>
    """, reports=[p.name for p in reports])


@app.route("/event-reports/<path:filename>")
def view_event_report(filename):
    """Serve a report from EVENT_DIR, without exposing other files."""
    if not filename.lower().endswith(".html"):
        abort(404)
    return send_from_directory(EVENT_DIR, filename)


if __name__ == "__main__":

    initialize_database()

    app.run(host="127.0.0.1", port=5000, debug=False)