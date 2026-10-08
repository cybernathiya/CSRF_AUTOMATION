🔐 CSRF Automation & Vulnerability Scanner

<p align="center">

<img src="https://img.shields.io/badge/Security-CSRF%20Scanner-red?style=for-the-badge" alt="CSRF Scanner">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">

<img src="https://img.shields.io/badge/Web%20Security-Automation-orange?style=for-the-badge" alt="Web Security">

<img src="https://img.shields.io/badge/Status-Educational-success?style=for-the-badge" alt="Educational">

</p>

<p align="center"> <b>Automated heuristic CSRF security assessment for authorized web applications</b> </p>

📌 Project Overview

CSRF Automation is an educational web-security automation project designed to identify potential Cross-Site Request Forgery (CSRF) weaknesses in web applications.

The scanner crawls authorized target applications, discovers HTML forms, analyzes their request characteristics, detects fields that appear to represent CSRF tokens, observes cookie attributes, and generates structured security reports.

The project also provides monitoring interfaces for observing scan progress, discovered forms, CSRF-token indicators, potential findings, errors, and scanner logs.

⚠️ Important: This project is intended for systems that you own or have explicit permission to test. It is a heuristic scanner and does not submit forms or prove exploitability. Findings marked as potential issues require manual validation.
✨ Features
🔍 Automated website crawling
📝 HTML form discovery
🛡️ CSRF-token field detection
🍪 Cookie/security-attribute observation
🔐 Optional authenticated scanning using Netscape/Mozilla cookie files
🌐 Support for multiple starting URLs
📂 Configurable crawl scope
🚫 Configurable path exclusions
⏱️ Configurable request delay
🌎 Optional JavaScript rendering using Playwright
📊 JSON report generation
📄 HTML report generation
🖥️ Console result summary
📜 Scan logging
📈 Real-time scanner monitoring
🧪 Test-target application support
🔐 Event report generation
🧩 Modular scanner architecture

The main scanner connects the input/configuration layer to session creation, crawling/form collection, token detection, request analysis, reporting, and console/HTML output. 
G
GitHub

🎯 What Is CSRF?

Cross-Site Request Forgery (CSRF) is a web security vulnerability where an attacker tricks an authenticated user's browser into sending an unintended request to a trusted application.

A typical vulnerable request may look conceptually like:

Victim Browser
      |
      | Authenticated request
      | + session cookie
      v
Trusted Web Application
      |
      | Performs state-changing action
      v
Unauthorized Operation


CSRF attacks rely heavily on browser behavior surrounding authenticated sessions and application requests. OWASP recommends defenses such as CSRF tokens and appropriate cookie protections. 
G
GitHub
+1

🧠 How This Project Works

The scanner follows this general process:

flowchart TD

    A["👤 User Starts Scanner"] --> B["⚙️ Read Scanner Configuration"]

    B --> C["🌐 Enter Target URL(s)"]

    C --> D["🔐 Create HTTP Session"]

    D --> E{"🍪 Cookie File Provided?"}

    E -->|Yes| F["Load Authorized Session Cookies"]
    E -->|No| G["Create New Session"]

    F --> H["🕷️ Start Crawler"]
    G --> H

    H --> I["🔎 Discover Pages"]

    I --> J["📝 Discover HTML Forms"]

    J --> K["🍪 Observe Cookies"]

    K --> L["🛡️ Detect Possible CSRF Tokens"]

    L --> M["📡 Analyze Request Characteristics"]

    M --> N["📊 Generate Findings"]

    N --> O["📄 Generate JSON Report"]

    N --> P["🌐 Generate HTML Report"]

    N --> Q["🖥️ Console Summary"]

    O --> R["📁 Output Directory"]
    P --> R
    Q --> R

    R --> S["📜 Scan Logs"]

    S --> T["✅ Scan Complete"]

🏗️ System Architecture
flowchart LR

    U["👤 Security Tester"]

    CLI["🖥️ CLI Input"]

    CONFIG["⚙️ Config"]

    SESSION["🔐 Session Factory"]

    CRAWLER["🕷️ Form Collector / Crawler"]

    TOKEN["🛡️ Token Detector"]

    ANALYZER["📡 Request Analyzer"]

    REPORT["📊 Report Generator"]

    DISPLAY["🖥️ Result Display"]

    JSON["📄 report.json"]

    HTML["🌐 report.html"]

    LOG["📜 scan_log.txt"]

    MONITOR["📈 Scanner Monitor"]

    TARGET["🌍 Authorized Target"]

    U --> CLI
    CONFIG --> SESSION

    CLI --> SESSION
    CLI --> CRAWLER

    SESSION --> CRAWLER
    CRAWLER <--> TARGET

    CRAWLER --> TOKEN
    CRAWLER --> ANALYZER

    TOKEN --> REPORT
    ANALYZER --> REPORT

    REPORT --> JSON
    REPORT --> DISPLAY

    DISPLAY --> HTML
    DISPLAY --> LOG

    LOG --> MONITOR
    CRAWLER --> MONITOR
    REPORT --> MONITOR

🔄 Detailed Scanning Flow
flowchart TD

    START(["🚀 Start"])

    INPUT["Read user input"]

    URLS["Load target URL(s)"]

    OPTIONS["Load scan options"]

    SESSION["Create scanner session"]

    COOKIE{"Cookie file?"}

    LOADCOOKIE["Load Netscape/Mozilla cookies"]

    NORMALSESSION["Use normal session"]

    CRAWL["Start crawling"]

    SCOPE{"Within configured scope?"}

    EXCLUDE{"Excluded path?"}

    FETCH["Fetch page"]

    RENDER{"JavaScript rendering enabled?"}

    PLAYWRIGHT["Render using Playwright"]

    HTTP["Process HTTP response"]

    FORMS["Extract HTML forms"]

    COOKIES["Record cookie observations"]

    LINKS["Extract links"]

    TOKEN["Analyze possible CSRF token fields"]

    REQUEST["Analyze form/request characteristics"]

    RESULT["Create heuristic result"]

    MORE{"More pages/forms?"}

    REPORT["Generate reports"]

    JSON["JSON report"]

    HTML["HTML report"]

    LOG["Write scan logs"]

    END(["✅ Complete"])

    START --> INPUT
    INPUT --> URLS
    URLS --> OPTIONS
    OPTIONS --> SESSION

    SESSION --> COOKIE

    COOKIE -->|Yes| LOADCOOKIE
    COOKIE -->|No| NORMALSESSION

    LOADCOOKIE --> CRAWL
    NORMALSESSION --> CRAWL

    CRAWL --> SCOPE

    SCOPE -->|No| MORE
    SCOPE -->|Yes| EXCLUDE

    EXCLUDE -->|Yes| MORE
    EXCLUDE -->|No| FETCH

    FETCH --> RENDER

    RENDER -->|Yes| PLAYWRIGHT
    RENDER -->|No| HTTP

    PLAYWRIGHT --> HTTP

    HTTP --> FORMS
    HTTP --> COOKIES
    HTTP --> LINKS

    FORMS --> TOKEN
    FORMS --> REQUEST

    TOKEN --> RESULT
    REQUEST --> RESULT

    LINKS --> SCOPE

    RESULT --> MORE

    MORE -->|Yes| CRAWL
    MORE -->|No| REPORT

    REPORT --> JSON
    REPORT --> HTML
    REPORT --> LOG

    JSON --> END
    HTML --> END
    LOG --> END

🛡️ CSRF Analysis Flow
flowchart TD

    FORM["📝 Discovered Form"]

    METHOD["Determine HTTP Method"]

    ACTION["Determine Form Action"]

    FIELDS["Inspect Form Fields"]

    TOKENSCAN["🔎 Search for CSRF-like Token"]

    TOKENFOUND{"Possible token found?"}

    COOKIES["🍪 Inspect Cookie Observations"]

    REQUEST["📡 Analyze Request"]

    METHODCHECK{"State-changing method?"}

    INFO["ℹ️ Informational Result"]

    REVIEW["🔎 Manual Review Required"]

    POTENTIAL["⚠️ Potential CSRF Issue"]

    PROTECTED["🛡️ Potentially Protected"]

    REPORT["📊 Add Result to Report"]

    FORM --> METHOD
    METHOD --> ACTION
    ACTION --> FIELDS

    FIELDS --> TOKENSCAN
    TOKENSCAN --> TOKENFOUND

    TOKENFOUND -->|Yes| COOKIES
    TOKENFOUND -->|No| COOKIES

    COOKIES --> REQUEST
    REQUEST --> METHODCHECK

    METHODCHECK -->|No| INFO
    METHODCHECK -->|Yes| REVIEW

    REVIEW --> POTENTIAL
    REVIEW --> PROTECTED

    INFO --> REPORT
    POTENTIAL --> REPORT
    PROTECTED --> REPORT

Note: Detection is heuristic. A field whose name looks like a CSRF token does not necessarily mean the server validates it. Likewise, the absence of an obvious token does not by itself prove a vulnerability. The repository's own documentation explicitly treats HIGH/MEDIUM results as potential findings requiring manual validation. 
G
GitHub
🍪 Cookie Analysis Flow
flowchart TD

    PAGE["🌐 HTTP Response"]

    SETCOOKIE["Read Set-Cookie Headers"]

    COOKIE["🍪 Cookie Observation"]

    NAME["Cookie Name"]

    FLAGS["Security Attributes"]

    SECURE["Secure"]

    HTTPONLY["HttpOnly"]

    SAMESITE["SameSite"]

    SESSION{"Looks like session/auth cookie?"}

    AUTH["🔐 Possible Authentication Cookie"]

    NORMAL["Normal Cookie"]

    REPORT["📊 Store Observation"]

    PAGE --> SETCOOKIE
    SETCOOKIE --> COOKIE

    COOKIE --> NAME
    COOKIE --> FLAGS

    FLAGS --> SECURE
    FLAGS --> HTTPONLY
    FLAGS --> SAMESITE

    NAME --> SESSION

    SESSION -->|Yes| AUTH
    SESSION -->|No| NORMAL

    AUTH --> REPORT
    NORMAL --> REPORT
    SECURE --> REPORT
    HTTPONLY --> REPORT
    SAMESITE --> REPORT

🌐 JavaScript Rendering Flow

The project supports optional Playwright rendering for pages where important content is generated by JavaScript. The browser-enabled dependency file adds Playwright on top of the normal requirements. 
G
GitHub

flowchart TD

    START["🌐 Target Page"]

    MODE{"Render JavaScript?"}

    HTTP["📡 HTTP Crawler"]

    PW["🎭 Playwright Chromium"]

    DOM["📄 Final DOM"]

    FORMS["📝 Extract Forms"]

    LINKS["🔗 Extract Links"]

    ANALYSIS["🔎 Security Analysis"]

    START --> MODE

    MODE -->|No| HTTP
    MODE -->|Yes| PW

    HTTP --> DOM
    PW --> DOM

    DOM --> FORMS
    DOM --> LINKS

    FORMS --> ANALYSIS
    LINKS --> ANALYSIS

📊 Report Generation Flow
flowchart LR

    FORM["📝 Form"]

    TOKEN["🛡️ Token Analysis"]

    REQUEST["📡 Request Analysis"]

    RESULT["📊 Combined Result"]

    GENERATOR["Report Generator"]

    JSON["report.json"]

    HTML["report.html"]

    CONSOLE["Console Summary"]

    LOG["scan_log.txt"]

    FORM --> TOKEN
    FORM --> REQUEST

    TOKEN --> RESULT
    REQUEST --> RESULT

    RESULT --> GENERATOR

    GENERATOR --> JSON
    GENERATOR --> HTML
    GENERATOR --> CONSOLE
    GENERATOR --> LOG


The current entry point writes JSON results, renders an HTML report, prints a console summary, and records crawl/scan information in the configured log path. 
G
GitHub

📈 Real-Time Monitoring Architecture

The repository contains monitoring interfaces that expose scanner status, current site/form, total sites, scanned sites, forms, CSRF-token indicators, vulnerable/protected form counts, errors, progress, timestamps, and live logs. 
G
GitHub
+1

flowchart TD

    SCANNER["🛡️ CSRF Scanner"]

    STATUS["📊 Scanner Status"]

    SITE["🌐 Current Site"]

    FORM["📝 Current Form"]

    STATS["📈 Scan Statistics"]

    PROGRESS["⏳ Progress"]

    LOGS["📜 Scanner Logs"]

    API["🔌 /api/monitor"]

    UI["🖥️ Monitoring Dashboard"]

    SCANNER --> STATUS
    SCANNER --> SITE
    SCANNER --> FORM
    SCANNER --> STATS
    SCANNER --> PROGRESS
    SCANNER --> LOGS

    STATUS --> API
    SITE --> API
    FORM --> API
    STATS --> API
    PROGRESS --> API
    LOGS --> API

    API --> UI

    UI --> REFRESH["🔄 Periodic Refresh"]
    REFRESH --> API


The monitor UI refreshes its monitoring data periodically and displays live scanner information. 
G
GitHub
+1

🗂️ Project Structure

Current repository files include the scanner entry point, configuration, reporting components, monitoring interfaces, test target application, and dependency files. 
G
GitHub

CSRF_AUTOMATION/
│
├── 📄 main.py
├── 📄 config.py
├── 📄 event_report.py
│
├── 📄 monitor.py
├── 📄 monitor1.html
├── 📄 monitor.html
├── 📄 scanner_monitor.py
│
├── 📄 test_target_app.py
├── 📄 Untitled-1.html
│
├── 📄 requirements.txt
├── 📄 requirements-browser.txt
├── 📄 .gitignore
│
├── 📁 modules/
│   ├── form_collector.py
│   ├── session_factory.py
│   ├── token_detector.py
│   ├── request_analyzer.py
│   ├── report_generator.py
│   └── result_display.py
│
├── 📁 utils/
│   ├── cli_input.py
│   └── logger.py
│
├── 📁 output/
│   ├── report.json
│   ├── report.html
│   └── events/
│
├── 📁 logs/
│   └── scan_log.txt
│
└── 📁 data/
    └── users.db

🧩 Core Components
main.py

The primary entry point.

It coordinates:

User input
Logging
Session creation
Form collection
Token detection
Request analysis
Report generation
Console output
HTML report generation

The current implementation imports FormCollector, TokenDetector, RequestAnalyzer, ReportGenerator, ResultDisplay, ScanLogger, and the session factory. 
G
GitHub

config.py

Contains application paths and configuration values such as:

logs/scan_log.txt
data/users.db
output/events


It also reads the application's secret key from the SECRET_KEY environment variable, with a development fallback. 
G
GitHub

For production deployments, use an environment-provided secret rather than the development fallback.

FormCollector

Responsible for crawling pages and discovering forms.

Conceptually:

Target URL
    ↓
Fetch Page
    ↓
Parse HTML
    ↓
Find Links
    ↓
Find Forms
    ↓
Record Cookies
    ↓
Return Form Inventory

TokenDetector

Analyzes discovered forms for fields that appear to represent CSRF tokens.

Possible examples of token-like fields include names containing concepts such as:

csrf
csrf_token
csrf-token
xsrf
xsrf_token


Detection should be treated as a heuristic, not proof that the application accepts or validates the token.

RequestAnalyzer

Analyzes discovered requests/forms and their associated observations.

The scanner is designed to inspect requests rather than actively exploit them.

ReportGenerator

Combines scanner observations into structured findings and writes the JSON report.

ResultDisplay

Provides:

Console summaries
HTML reporting
Human-readable scan results
event_report.py

Generates HTML event reports for application events.

The implementation creates reports containing fields such as:

Event ID
Event type
Username
Site ID
Timestamp
IP address
Status

User-supplied values are HTML-escaped before being inserted into the generated report. 
G
GitHub

📈 Monitoring Dashboard

The monitoring interface provides a visual overview of the scan.

Typical dashboard information includes:

Metric	Description
Scanner Status	Current scanner state
Current Site	Site currently being processed
Current Form	Form currently under analysis
Total Sites	Number of discovered/target sites
Sites Scanned	Number of processed sites
Forms Found	Number of discovered forms
CSRF Tokens	Possible CSRF-token indicators
Vulnerable Forms	Potentially vulnerable forms
Protected Forms	Potentially protected forms
Errors	Scanner errors
Progress	Scan completion percentage
Started	Scan start time
Completed	Scan completion time
Logs	Live scanner messages

These fields correspond to the monitoring UI currently present in the repository. 
G
GitHub
+1

📸 Screenshots / Images

Create a directory for project screenshots:

images/
├── architecture.png
├── scanner-start.png
├── scanner-progress.png
├── dashboard.png
├── report-html.png
├── report-json.png
└── event-report.png


Then add the screenshots to this README.

🖥️ Scanner
![Scanner](images/scanner-start.png)

📈 Monitoring Dashboard
![Monitoring Dashboard](images/dashboard.png)

📊 HTML Report
![HTML Report](images/report-html.png)

📄 JSON Report
![JSON Report](images/report-json.png)

🔐 Event Report
![Event Report](images/event-report.png)

Recommended: Capture screenshots from your own running instance and commit them under images/. This avoids documenting UI that differs from the current implementation.
🛠️ Installation
1. Clone the Repository
git clone https://github.com/cybernathiya/CSRF_AUTOMATION.git
cd CSRF_AUTOMATION

2. Create a Virtual Environment
Linux / macOS
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


The current dependency file includes Requests, BeautifulSoup, lxml, argparse, colorama, Jinja2, OWASP ZAP's Python client, and Tabulate. 
G
GitHub

🎭 Optional Browser Support

For JavaScript-rendered applications:

pip install -r requirements-browser.txt


Then install Chromium:

python -m playwright install chromium


The repository's browser requirements extend the normal dependency set with Playwright. 
G
GitHub

🚀 Running the Scanner

Run the scanner:

python main.py


The application will display the CSRF scanner interface and request scan parameters.

🔎 Typical Scan Workflow
sequenceDiagram

    actor Tester
    participant Scanner
    participant Target
    participant Analyzer
    participant Report
    participant Monitor

    Tester->>Scanner: Start scanner

    Scanner->>Scanner: Read configuration

    Scanner->>Target: Request target page

    Target-->>Scanner: HTML response

    Scanner->>Scanner: Extract links/forms/cookies

    Scanner->>Target: Request discovered pages

    Target-->>Scanner: Page responses

    Scanner->>Analyzer: Analyze forms

    Analyzer->>Analyzer: Detect possible CSRF token

    Analyzer->>Analyzer: Analyze request characteristics

    Analyzer-->>Scanner: Heuristic result

    Scanner->>Report: Save findings

    Report-->>Tester: JSON/HTML reports

    Scanner->>Monitor: Update status

    Monitor-->>Tester: Live progress

🌐 Multiple Targets

Multiple starting URLs can be supplied when supported by the scanner's input layer.

Conceptually:

Target 1 ─┐
Target 2 ─┼──> Scanner ──> Analysis ──> Reports
Target 3 ─┤
Target N ─┘


Example:

https://authorized-app.example/
https://authorized-app.example/account/


Only scan systems for which you have explicit authorization.

🍪 Authenticated Scanning

The scanner supports loading an authorized browser-exported Netscape/Mozilla-format cookie file.

Conceptual flow:

flowchart LR

    BROWSER["🌐 Authorized Browser"]

    LOGIN["🔐 Login"]

    COOKIE["🍪 Export Cookies"]

    FILE["cookies.txt"]

    SCANNER["🛡️ CSRF Scanner"]

    TARGET["🌐 Target Application"]

    REPORT["📊 Report"]

    BROWSER --> LOGIN
    LOGIN --> COOKIE
    COOKIE --> FILE
    FILE --> SCANNER
    SCANNER --> TARGET
    TARGET --> SCANNER
    SCANNER --> REPORT


The repository documentation specifies that cookie values are kept in memory for requests and are not written to reports or scan logs. The cookie file itself should still be treated like a password and removed/protected after use. 
G
GitHub

Example:

python main.py


Then provide the authorized cookie file when requested.

⚙️ Scan Configuration

The scanner supports configuration concepts including:

Option	Purpose
Start URL	Initial target
Multiple targets	Scan multiple starting points
Maximum pages	Limit crawl size
Scope	Restrict crawl to path/origin
Exclusions	Avoid selected paths
Delay	Pause between requests
Cookie file	Use an authorized session
JS rendering	Process JavaScript-generated pages
Proxy	Optional proxy configuration
Output paths	Configure generated reports

The repository's README describes bounded crawling, configurable page limits, path exclusions, request delays, cookie-file authentication, and optional Playwright rendering. 
G
GitHub

🧭 Crawl Scope

The scanner is designed to keep crawling bounded.

flowchart TD

    START["Starting URL"]

    PATH["Starting URL Path"]

    ORIGIN["Target Origin"]

    PAGE["Candidate Page"]

    SCOPE{"Within Scope?"}

    SCAN["Scan Page"]

    SKIP["Skip Page"]

    START --> PATH
    START --> ORIGIN

    PATH --> PAGE
    ORIGIN --> PAGE

    PAGE --> SCOPE

    SCOPE -->|Yes| SCAN
    SCOPE -->|No| SKIP


This helps prevent accidental expansion into unrelated parts of a target application.

🚫 Exclusions

State-changing or sensitive routes should be treated carefully.

Examples include:

logout
delete
unsubscribe


The repository documentation indicates that state-like paths such as these are excluded by default. 
G
GitHub

📁 Output

After a successful scan, the project can generate:

output/
│
├── report.json
├── report.html
│
└── events/
    ├── event-report-1.html
    ├── event-report-2.html
    └── ...


Logs:

logs/
└── scan_log.txt


The main scanner explicitly reports output/report.html and the configured scan-log location when the scan completes. 
G
GitHub

📄 JSON Report

The JSON report is intended for machine-readable processing.

Conceptual structure:

{
  "scan": {
    "start_urls": [],
    "scope": "path",
    "max_pages": 100,
    "request_delay_seconds": 0.2,
    "render_js": false
  },
  "results": [],
  "generated_at": "..."
}


This makes the scanner suitable for integration into larger security-testing or reporting workflows.

🌐 HTML Report

The HTML report is designed for human-readable analysis.

┌───────────────────────────────────────┐
│        CSRF SCAN REPORT               │
├───────────────────────────────────────┤
│ Target                                │
│ Crawl Statistics                      │
│ Forms Discovered                      │
│ Token Indicators                      │
│ Cookie Observations                   │
│ Findings                              │
│ Severity / Review Status              │
└───────────────────────────────────────┘

📜 Logging Flow
flowchart TD

    START["Scanner Start"]

    STARTLOG["Write Start Event"]

    CRAWLLOG["Write Crawl Information"]

    RESULTLOG["Write Result Summary"]

    ERRORLOG["Write Errors"]

    FILE["logs/scan_log.txt"]

    END["Scan Complete"]

    START --> STARTLOG
    STARTLOG --> CRAWLLOG

    CRAWLLOG --> RESULTLOG
    CRAWLLOG --> ERRORLOG

    RESULTLOG --> FILE
    ERRORLOG --> FILE

    FILE --> END

🔐 Security Model

The project is intended to support authorized security assessment.

flowchart TD

    AUTH["🔐 Authorized Tester"]

    TARGET["🌐 Authorized Application"]

    SCANNER["🛡️ CSRF Scanner"]

    OBSERVE["🔎 Observe"]

    ANALYZE["📊 Analyze"]

    REPORT["📄 Report"]

    AUTH --> TARGET
    AUTH --> SCANNER

    SCANNER --> TARGET

    TARGET --> OBSERVE
    OBSERVE --> ANALYZE
    ANALYZE --> REPORT


The scanner should be considered an observation and heuristic analysis tool, not an automated exploitation framework.

⚠️ Limitations

This project does not prove that a CSRF vulnerability is exploitable.

Important limitations include:

Form discovery does not guarantee complete application coverage.
JavaScript-heavy applications may require browser rendering.
A CSRF-token-looking field may not actually be validated server-side.
Absence of a token-looking field does not automatically prove CSRF.
Cookie-name heuristics may misclassify cookies.
SameSite behavior depends on browser context.
Routes reachable only through non-link navigation may not be discovered.
The scanner does not submit forms.
The scanner does not attempt to bypass CSRF protections.
Potential findings require manual validation.

These limitations are consistent with the repository's current README, which describes the scanner as heuristic and explicitly states that it does not submit forms, test token enforcement, or confirm exploitability. 
G
GitHub

🔍 Manual Validation

When the scanner reports a potential issue, a security tester should manually validate the application using an authorized test environment.

A conceptual validation workflow is:

flowchart TD

    FINDING["⚠️ Potential Finding"]

    REVIEW["🔎 Review Form"]

    TOKEN["Check CSRF Token"]

    SESSION["Check Session Behavior"]

    SERVER["Review Server-Side Validation"]

    SAFE["Use Controlled Test Account"]

    CONFIRM{"Security Control Effective?"}

    PROTECTED["🛡️ Protection Appears Effective"]

    REVIEW_REQUIRED["🔎 Further Manual Review"]

    FINDING --> REVIEW
    REVIEW --> TOKEN
    TOKEN --> SESSION
    SESSION --> SERVER
    SERVER --> SAFE

    SAFE --> CONFIRM

    CONFIRM -->|Yes| PROTECTED
    CONFIRM -->|Unclear| REVIEW_REQUIRED

🧪 Testing Architecture

The repository also contains a target application used for testing the scanner.

flowchart LR

    TESTER["👤 Tester"]

    TARGET["🧪 Test Target Application"]

    SCANNER["🛡️ Scanner"]

    MONITOR["📈 Monitor"]

    REPORT["📊 Reports"]

    TESTER --> TARGET
    TESTER --> SCANNER

    SCANNER --> TARGET

    TARGET --> SCANNER

    SCANNER --> MONITOR
    SCANNER --> REPORT

    MONITOR --> TESTER
    REPORT --> TESTER

🧱 Technology Stack
Technology	Purpose
Python	Core implementation
Requests	HTTP communication
BeautifulSoup	HTML parsing
lxml	HTML/XML parsing
Jinja2	HTML/report templating
Colorama	Console formatting
Tabulate	Table formatting
Playwright	Optional JavaScript rendering
OWASP ZAP Python Client	Security-testing integration/dependency
HTML/CSS/JavaScript	Monitoring interfaces

The dependency versions are defined in the repository's requirements.txt; Playwright is separately included in requirements-browser.txt. 
G
GitHub
+1

🔄 Complete End-to-End Architecture
flowchart TB

    USER["👤 Security Tester"]

    INPUT["🖥️ CLI / Input Layer"]

    CONFIG["⚙️ Configuration"]

    SESSION["🔐 Session Factory"]

    COOKIE["🍪 Optional Cookie File"]

    CRAWLER["🕷️ Form Collector"]

    TARGET["🌐 Authorized Web Application"]

    PAGES["📄 Discovered Pages"]

    FORMS["📝 Discovered Forms"]

    COOKIES["🍪 Cookie Observations"]

    TOKEN["🛡️ Token Detector"]

    ANALYZER["📡 Request Analyzer"]

    RESULTS["📊 Scanner Results"]

    JSON["📄 JSON Report"]

    HTML["🌐 HTML Report"]

    CONSOLE["🖥️ Console Output"]

    LOGS["📜 Scan Logs"]

    MONITORAPI["🔌 Monitoring API"]

    DASHBOARD["📈 Monitoring Dashboard"]

    EVENTS["📋 Event Reports"]

    USER --> INPUT
    INPUT --> CONFIG

    CONFIG --> SESSION
    INPUT --> SESSION

    COOKIE --> SESSION

    SESSION --> CRAWLER

    CRAWLER <--> TARGET

    TARGET --> PAGES
    PAGES --> FORMS
    PAGES --> COOKIES

    FORMS --> TOKEN
    FORMS --> ANALYZER

    COOKIES --> ANALYZER
    TOKEN --> RESULTS
    ANALYZER --> RESULTS

    RESULTS --> JSON
    RESULTS --> HTML
    RESULTS --> CONSOLE

    RESULTS --> LOGS

    LOGS --> MONITORAPI
    RESULTS --> MONITORAPI

    MONITORAPI --> DASHBOARD

    USER --> DASHBOARD

    EVENTS --> USER

📋 Scanner Lifecycle
stateDiagram-v2

    [*] --> Idle

    Idle --> Initializing: Start scanner

    Initializing --> SessionReady: Session created

    SessionReady --> Crawling: Begin crawl

    Crawling --> DiscoveringForms: Page loaded

    DiscoveringForms --> Analyzing: Forms discovered

    Analyzing --> Crawling: More pages

    Analyzing --> Reporting: Crawl complete

    Reporting --> Completed: Reports generated

    Crawling --> Error: Scanner error
    Analyzing --> Error: Analysis error

    Error --> Idle: Stop / recover

    Completed --> Idle

📊 Finding Classification

The scanner should be understood as producing signals, not guaranteed exploit results.

flowchart TD

    RESULT["Scanner Observation"]

    HIGH["🔴 HIGH\nPotentially Significant"]

    MEDIUM["🟠 MEDIUM\nPotential Issue"]

    INFO["🔵 INFO\nInformational"]

    REVIEW["🟡 REVIEW\nInsufficient Evidence"]

    MANUAL["👤 Manual Validation"]

    RESULT --> HIGH
    RESULT --> MEDIUM
    RESULT --> INFO
    RESULT --> REVIEW

    HIGH --> MANUAL
    MEDIUM --> MANUAL
    REVIEW --> MANUAL


The project's documentation specifically notes that HIGH and MEDIUM should be manually validated, while INFO and REVIEW represent different levels of available evidence. 
G
GitHub

🛡️ Recommended CSRF Defenses

For applications being tested, recommended defensive controls include:

Use unpredictable CSRF tokens.
Bind tokens appropriately to the user's session.
Validate tokens server-side.
Use appropriate SameSite cookie settings.
Use secure authentication/session management.
Avoid state-changing actions through unsafe HTTP methods such as GET.
Consider additional verification for highly sensitive operations.

OWASP recommends CSRF tokens and appropriate cookie protections as important defensive mechanisms. 
G
GitHub

🔒 Responsible Use

This project is intended for:

Security education
Local security laboratories
CTF environments
Applications you own
Applications for which you have explicit written authorization
Defensive security testing
Secure-development testing

Do not use this tool against systems without authorization.

⚠️ Disclaimer

This project is provided for educational and authorized security-testing purposes only.

The author and contributors are not responsible for misuse, unauthorized scanning, disruption, data loss, privacy violations, or other consequences resulting from use of this software.

Always obtain explicit permission before scanning a target.

📚 Security References
OWASP CSRF Prevention Cheat Sheet
OWASP Web Security Testing Guide – CSRF Testing
MDN – Cross-Site Request Forgery
🤝 Contributing

Contributions are welcome.

Suggested improvements:

Add additional CSRF heuristics
Improve JavaScript crawling
Add authenticated browser sessions
Improve report visualization
Add automated regression tests
Add CI/CD security testing
Improve scanner performance
Add configurable rule sets
Add richer dashboard charts
Add export formats such as CSV/PDF
Improve documentation and examples
🗺️ Future Roadmap
timeline
    title CSRF Automation Roadmap

    Current : Form Discovery
            : Token Detection
            : Cookie Observation
            : Request Analysis
            : JSON/HTML Reports
            : Monitoring Dashboard

    Next : Better JavaScript Crawling
         : Improved Heuristics
         : Better Reporting

    Future : Advanced Authentication
           : CI/CD Integration
           : Security Regression Testing
           : Extended Web Security Checks

⭐ Project Summary
                 🔐 CSRF AUTOMATION
                         │
                         ▼
                ┌─────────────────┐
                │ Target Discovery│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Form Discovery │
                └────────┬────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      🛡️ Token Detection       🍪 Cookie Analysis
             │                       │
             └───────────┬───────────┘
                         ▼
                 📡 Request Analysis
                         │
                         ▼
                  📊 Risk Signals
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          JSON        HTML       Console
             │           │           │
             └───────────┼───────────┘
                         ▼
                  📈 Monitoring

👨‍💻 Author

cybernathiya

GitHub Repository:

CSRF_AUTOMATION

<p align="center">

<b>🔐 Security Testing • Automation • CSRF Analysis • Defensive Security</b>

</p>
