🛡️ CSRF AUTOMATION

<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Security-CSRF-EF4444?style=for-the-badge" alt="CSRF"> <img src="https://img.shields.io/badge/Automation-Scanner-7C3AED?style=for-the-badge" alt="Automation"> <img src="https://img.shields.io/badge/License-Educational-22C55E?style=for-the-badge" alt="Educational"> </p>

<p align="center"> <strong>Automated CSRF Security Assessment for Authorized Web Applications</strong> </p>

<p align="center"> Discover forms • Analyze CSRF token indicators • Inspect cookies • Generate reports </p>

📌 Overview

CSRF AUTOMATION is a Python-based security assessment tool designed to discover and analyze potential Cross-Site Request Forgery (CSRF) weaknesses in authorized web applications.

The scanner performs bounded crawling, discovers forms, analyzes possible CSRF-token fields, observes cookies, analyzes request characteristics, and produces JSON and HTML reports.

⚠️ Important: This is a heuristic security scanner. It does not automatically prove that a CSRF vulnerability is exploitable and does not replace manual security testing.
✨ Features
Feature	Description
🕷️ Web Crawling	Discovers pages within the configured scope
📝 Form Discovery	Finds HTML forms during crawling
🛡️ Token Detection	Detects fields that appear to be CSRF tokens
📡 Request Analysis	Analyzes discovered form/request characteristics
🍪 Cookie Observation	Records cookie-related security observations
🔐 Cookie-Based Sessions	Supports authorized cookie-file sessions
🎭 JavaScript Rendering	Optional Playwright support
📄 JSON Report	Machine-readable scan results
🌐 HTML Report	Human-readable security report
📜 Logging	Stores scan history and summaries
⏱️ Request Delay	Controls request frequency
🚧 Crawl Scope	Limits crawling to the configured scope
🧭 How It Works

The scanner follows this general pipeline:

flowchart TD
    A["👤 Security Tester"] --> B["🖥️ CLI Input"]

    B --> C["⚙️ Scan Configuration"]

    C --> D["🔐 Create Session"]

    D --> E["🕷️ Form Collector"]

    E --> F["🌐 Authorized Target"]

    F --> G["📄 Discover Pages"]

    G --> H["📝 Discover Forms"]

    G --> I["🍪 Observe Cookies"]

    H --> J["🛡️ Token Detector"]

    H --> K["📡 Request Analyzer"]

    I --> K

    J --> L["📊 Report Generator"]
    K --> L

    L --> M["📄 JSON Report"]
    L --> N["🌐 HTML Report"]

    E --> O["📜 Scan Statistics"]
    O --> P["📜 Logs"]

    M --> Q["👤 Security Tester"]
    N --> Q
    P --> Q

🏗️ Architecture
flowchart LR
    USER["👤 Tester"]

    CLI["CLI Input"]
    SESSION["Session Factory"]
    CRAWLER["Form Collector"]

    TARGET["🌐 Target Application"]

    TOKEN["Token Detector"]
    ANALYZER["Request Analyzer"]

    REPORT["Report Generator"]
    DISPLAY["Result Display"]
    LOGGER["Logger"]

    JSON["report.json"]
    HTML["report.html"]
    LOG["scan_log.txt"]

    USER --> CLI
    CLI --> SESSION

    SESSION --> CRAWLER
    CRAWLER <--> TARGET

    CRAWLER --> TOKEN
    CRAWLER --> ANALYZER

    TOKEN --> REPORT
    ANALYZER --> REPORT

    REPORT --> JSON
    REPORT --> DISPLAY

    DISPLAY --> HTML

    CRAWLER --> LOGGER
    REPORT --> LOGGER

    LOGGER --> LOG

    JSON --> USER
    HTML --> USER
    LOG --> USER

🔍 Scan Lifecycle
sequenceDiagram
    actor Tester
    participant Scanner
    participant Target
    participant Analyzer
    participant Reports

    Tester->>Scanner: Start scanner

    Scanner->>Scanner: Read scan configuration

    Scanner->>Scanner: Create HTTP session

    Scanner->>Target: Crawl starting URL

    Target-->>Scanner: HTML response

    Scanner->>Scanner: Discover pages and forms

    Scanner->>Scanner: Observe cookies

    Scanner->>Analyzer: Analyze discovered forms

    Analyzer->>Analyzer: Check token indicators

    Analyzer->>Analyzer: Analyze request characteristics

    Analyzer-->>Scanner: Analysis results

    Scanner->>Reports: Generate JSON report

    Scanner->>Reports: Generate HTML report

    Reports-->>Tester: Scan results

🕷️ Crawling Flow
flowchart TD
    A["🌐 Start URL"]

    B["📡 Request Page"]

    C["🔍 Parse Response"]

    D["🔗 Extract Links"]

    E["📝 Extract Forms"]

    F["🍪 Record Cookie Observations"]

    G{"Within Scope?"}

    H["📋 Queue Page"]

    I["⏭️ Ignore Page"]

    J{"More Pages?"}

    K["✅ Crawling Complete"]

    A --> B
    B --> C

    C --> D
    C --> E
    C --> F

    D --> G

    G -->|Yes| H
    G -->|No| I

    H --> J
    E --> J
    F --> J

    J -->|Yes| B
    J -->|No| K

📝 Form Analysis

Each discovered form is passed through the analysis pipeline.

flowchart TD
    A["📝 Discovered Form"]

    B["HTTP Method"]
    C["Form Action"]
    D["Input Fields"]

    E["🛡️ Token Detector"]
    F["📡 Request Analyzer"]

    G["📊 Combined Result"]

    A --> B
    A --> C
    A --> D

    D --> E

    B --> F
    C --> F
    A --> F

    E --> G
    F --> G

🛡️ CSRF Token Detection

The token detector looks for token-like indicators in discovered forms.

Conceptually:

flowchart LR
    FORM["📝 Form"]

    INPUTS["Input Fields"]

    CHECK["🔎 Token Detection"]

    FOUND{"Token-like Field?"}

    YES["🛡️ Token Indicator Found"]

    NO["⚠️ No Token Indicator"]

    REVIEW["👤 Manual Review"]

    FORM --> INPUTS
    INPUTS --> CHECK

    CHECK --> FOUND

    FOUND -->|Yes| YES
    FOUND -->|No| NO

    YES --> REVIEW
    NO --> REVIEW

A token-like field does not prove that the server correctly validates the token.
🍪 Cookie Observation

Cookie information is collected during crawling and supplied to the request-analysis stage.

flowchart TD
    A["🌐 HTTP Response"]

    B["🍪 Cookie Observation"]

    C["Cookie Attributes"]

    D["📡 Request Analyzer"]

    E["📊 Finding"]

    A --> B
    B --> C
    C --> D
    D --> E

🎭 JavaScript Rendering

For applications that depend on client-side JavaScript, the project provides optional Playwright support.

flowchart LR
    A["🌐 Target Page"]

    B{"JavaScript Rendering?"}

    C["📡 Normal HTTP Request"]

    D["🎭 Playwright"]

    E["📄 Page Content"]

    F["📝 Form Discovery"]

    A --> B

    B -->|No| C
    B -->|Yes| D

    C --> E
    D --> E

    E --> F

📊 Reporting

The scanner generates two primary report formats.

flowchart TD
    A["📊 Scan Results"]

    B["📄 JSON Report"]
    C["🌐 HTML Report"]

    D["📜 Scan Log"]

    A --> B
    A --> C
    A --> D

JSON
output/report.json

HTML
output/report.html

Log
logs/scan_log.txt

📁 Project Structure
CSRF_AUTOMATION/
│
├── main.py
├── config.py
├── event_report.py
│
├── monitor.py
├── monitor.html
├── monitor1.html
├── scanner_monitor.py
│
├── test_target_app.py
├── Untitled-1.html
│
├── requirements.txt
├── requirements-browser.txt
├── .gitignore
│
├── modules/
│   ├── form_collector.py
│   ├── session_factory.py
│   ├── token_detector.py
│   ├── request_analyzer.py
│   ├── report_generator.py
│   └── result_display.py
│
├── utils/
│   ├── cli_input.py
│   └── logger.py
│
├── output/
│   ├── report.json
│   ├── report.html
│   └── events/
│
├── logs/
│   └── scan_log.txt
│
└── data/
    └── users.db

🧩 Main Components
main.py

The main entry point coordinates the scanner.

The current implementation:

Reads user configuration.
Creates the scanner session.
Starts the form collector.
Collects discovered forms.
Runs token detection.
Runs request analysis.
Generates JSON output.
Generates HTML output.
Prints a console summary.
Writes scan logs.

This matches the current implementation in main.py. 
G
GitHub

modules/form_collector.py

Responsible for crawling the configured target and collecting discovered pages/forms.

It also maintains crawler statistics and cookie observations used later in the scan.

modules/session_factory.py

Creates the HTTP session used by the scanner.

The session can use an authorized cookie file and optional proxy configuration.

modules/token_detector.py

Analyzes discovered forms for possible CSRF-token indicators.

Results should be treated as heuristic signals rather than proof of a vulnerability.

modules/request_analyzer.py

Analyzes form/request characteristics together with cookie observations.

modules/report_generator.py

Collects analysis results and creates the structured JSON report.

modules/result_display.py

Handles human-readable output, including the console summary and HTML report.

utils/logger.py

Records scanner activity, crawl summaries, errors, and scan results.

🚀 Installation
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


The current project pins dependencies including Requests, BeautifulSoup, lxml, Colorama, Jinja2, the OWASP ZAP Python client, and Tabulate. 
G
GitHub

🎭 Optional Browser Support

Install the browser requirements:

pip install -r requirements-browser.txt


Then install Chromium:

python -m playwright install chromium


The browser requirements currently extend the main requirements with Playwright. 
G
GitHub

▶️ Running the Scanner

Start the application with:

python main.py


The scanner will prompt for the scan configuration.

The current main.py supports configuration for:

Starting URLs
Cookie file
Request delay
Maximum pages
Crawl scope
Path exclusions
JavaScript rendering
Proxy configuration

These options are passed into the form collector and session factory by the main application. 
G
GitHub

🔐 Authenticated Scanning

The scanner supports an authorized cookie file for authenticated testing.

Conceptual workflow:

sequenceDiagram
    actor Tester
    participant Browser
    participant Cookies
    participant Scanner
    participant Target

    Tester->>Browser: Authenticate
    Browser->>Cookies: Export session cookies
    Tester->>Scanner: Provide cookie file
    Scanner->>Scanner: Load cookies
    Scanner->>Target: Authenticated request
    Target-->>Scanner: Response
    Scanner->>Scanner: Analyze response/forms
    Scanner-->>Tester: Generate report

🔒 Treat exported session cookies as sensitive credentials. Never commit cookie files to Git.
📦 Output

After a scan, the primary outputs are:

output/
├── report.json
└── report.html


The scanner also maintains:

logs/
└── scan_log.txt


The current application prints the HTML report location and log location after completing the scan. 
G
GitHub

🖥️ Example Result Flow
┌────────────────────────────────────────────┐
│             🛡️ CSRF AUTOMATION             │
├────────────────────────────────────────────┤
│                                            │
│  🌐 Target                                 │
│       │                                    │
│       ▼                                    │
│  🕷️ Crawl                                  │
│       │                                    │
│       ▼                                    │
│  📝 Forms                                  │
│       │                                    │
│   ┌───┴─────────────┐                      │
│   ▼                 ▼                      │
│ 🛡️ Token        📡 Request                 │
│ Detection       Analysis                   │
│   │                 │                      │
│   └───────┬─────────┘                      │
│           ▼                                │
│      📊 Results                            │
│           │                                │
│     ┌─────┼─────┐                          │
│     ▼     ▼     ▼                          │
│   JSON   HTML   LOG                        │
│                                            │
└────────────────────────────────────────────┘

📈 Monitoring

The repository contains monitoring-related files:

monitor.py
monitor.html
monitor1.html
scanner_monitor.py


These components are separate from the core scan pipeline.

The primary scanner itself is implemented through main.py and the modules under modules/. 
G
GitHub

🧪 Test Target

The repository also includes:

test_target_app.py


This can be used as a local testing target while developing or validating the scanner.

For safe development, use a local laboratory or an application for which you have explicit authorization.

🔬 Detection Philosophy

This project performs heuristic analysis.

A simplified interpretation is:

flowchart TD
    A["🔎 Scanner Observation"]

    B["🛡️ Token Indicator"]
    C["📡 Request Characteristics"]
    D["🍪 Cookie Observations"]

    E["🧠 Heuristic Analysis"]

    F["📊 Potential Finding"]

    G["👤 Manual Validation"]

    A --> B
    A --> C
    A --> D

    B --> E
    C --> E
    D --> E

    E --> F
    F --> G

Important distinction
Scanner Finding
       ≠
Confirmed Vulnerability


A finding should be manually reviewed before being classified as a confirmed security issue.

⚠️ Limitations

The scanner should not be considered a replacement for a complete penetration test.

It may not detect:

Forms created dynamically after complex JavaScript interactions
Application logic that is not exposed through discovered forms
CSRF protections implemented outside the inspected form
Server-side token validation behavior
Complex multi-step workflows
Business-logic-dependent security controls

JavaScript rendering can improve coverage for some applications, but it does not guarantee complete application discovery.

🛡️ Responsible Use

Use this project only against systems you are authorized to test.

✅ Appropriate
Your own applications
Local development environments
Security laboratories
CTF environments
Authorized penetration tests
Applications with explicit testing permission
❌ Not appropriate
Unauthorized websites
Third-party applications without permission
Systems where scanning is prohibited
Production systems where testing could cause disruption
🔒 Security Notes

Never commit sensitive files such as:

.env
cookies.txt
*.cookie
session files
private keys
credentials


Use .gitignore to prevent accidental credential exposure.

🧰 Technology Stack
Technology	Purpose
🐍 Python	Core implementation
🌐 Requests	HTTP communication
🍲 BeautifulSoup	HTML parsing
⚡ lxml	HTML/XML parsing
🎨 Jinja2	HTML/report templating
🖍️ Colorama	Terminal formatting
📋 Tabulate	Console tables
🎭 Playwright	Optional browser rendering
🛡️ OWASP ZAP Python Client	Security tooling dependency
🗺️ Development Roadmap
timeline
    title CSRF AUTOMATION Roadmap

    Current
        : Form discovery
        : CSRF token heuristics
        : Request analysis
        : Cookie observations
        : JSON reports
        : HTML reports

    Next
        : Improved crawling
        : Better JavaScript coverage
        : Improved detection rules
        : Better reporting

    Future
        : Automated regression testing
        : CI/CD integration
        : Extended security checks

📚 References
OWASP CSRF Prevention Cheat Sheet
OWASP Web Security Testing Guide
MDN Web Security
👨‍💻 Author

cybernathiya

Repository:

CSRF_AUTOMATION

<p align="center"> <strong>🛡️ Discover • Analyze • Report • Secure</strong> </p>

<p align="center"> Built for authorized security testing and cybersecurity education. </p>
