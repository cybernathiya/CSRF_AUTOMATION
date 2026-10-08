import os
import html
import uuid
from datetime import datetime
from pathlib import Path


# Folder for registration and login event reports
EVENT_REPORT_DIR = Path("output/events")
EVENT_REPORT_DIR.mkdir(parents=True, exist_ok=True)


def generate_event_report(
    username,
    site_id,
    event_type,
    ip_address="Unknown"
):
    """
    Generate an individual HTML report for a registration or login event.
    """

    timestamp = datetime.now().astimezone()
    timestamp_text = timestamp.strftime("%d-%m-%Y %I:%M:%S %p %Z")

    # Escape user-supplied values before inserting them into HTML
    safe_username = html.escape(str(username))
    safe_site_id = html.escape(str(site_id))
    safe_event_type = html.escape(str(event_type))
    safe_ip_address = html.escape(str(ip_address))

    event_id = uuid.uuid4().hex[:12]

    filename = (
        f"{timestamp.strftime('%Y%m%d_%H%M%S')}_"
        f"site_{site_id}_{event_type}_{event_id}.html"
    )

    report_path = EVENT_REPORT_DIR / filename

    report_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>User Activity Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f4f6f8;
            color: #2c3e50;
        }}

        .container {{
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }}

        h1 {{
            color: #2c3e50;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }}

        th, td {{
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
            overflow-wrap: anywhere;
        }}

        th {{
            background: #2c3e50;
            color: white;
            width: 35%;
        }}

        tr:nth-child(even) {{
            background: #f9f9f9;
        }}

        .status {{
            color: #218838;
            font-weight: bold;
        }}

        .footer {{
            margin-top: 25px;
            font-size: 12px;
            color: #666;
        }}
    </style>
</head>

<body>
    <div class="container">
        <h1>User Activity Report</h1>

        <p>Event recorded successfully.</p>

        <table>
            <tr>
                <th>Event ID</th>
                <td>{event_id}</td>
            </tr>
            <tr>
                <th>Event Type</th>
                <td>{safe_event_type}</td>
            </tr>
            <tr>
                <th>Username</th>
                <td>{safe_username}</td>
            </tr>
            <tr>
                <th>Site ID</th>
                <td>{safe_site_id}</td>
            </tr>
            <tr>
                <th>Timestamp</th>
                <td>{html.escape(timestamp_text)}</td>
            </tr>
            <tr>
                <th>IP Address</th>
                <td>{safe_ip_address}</td>
            </tr>
            <tr>
                <th>Status</th>
                <td class="status">SUCCESS</td>
            </tr>
        </table>

        <div class="footer">
            Generated automatically by the CSRF testing application.
            No password or authentication secret is included.
        </div>
    </div>
</body>
</html>
"""

    # Write the report as UTF-8 HTML
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report_html)

    return str(report_path)