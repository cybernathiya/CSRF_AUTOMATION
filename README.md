🛡️ CSRF AUTOMATION

<p align="center"> <img src="https://img.shields.io/badge/CSRF-AUTOMATION-EF4444?style=for-the-badge&logo=security&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Web%20Security-Scanner-7C3AED?style=for-the-badge" /> <img src="https://img.shields.io/badge/Status-Educational-22C55E?style=for-the-badge" /> </p>

<p align="center"> <b>🔎 Automated CSRF Detection • 🕷️ Smart Crawling • 📊 Security Reports • 📈 Live Monitoring</b> </p>

<p align="center"> A Python-based heuristic security scanner for discovering and analyzing potential Cross-Site Request Forgery (CSRF) weaknesses in authorized web applications. </p>

⚡ What is CSRF AUTOMATION?

CSRF AUTOMATION is a lightweight web-security assessment framework that automatically:

        🌐 TARGET
           │
           ▼
      🕷️ CRAWLER
           │
           ▼
     📝 FORM DISCOVERY
           │
           ▼
     🛡️ TOKEN ANALYSIS
           │
           ▼
     🍪 COOKIE ANALYSIS
           │
           ▼
     📡 REQUEST ANALYSIS
           │
           ▼
       📊 FINDINGS
        ╱    │    ╲
       ▼     ▼     ▼
     JSON   HTML   LIVE
    REPORT REPORT MONITOR

Important: This is a heuristic scanner, not an exploitation framework. It does not submit forms or claim that a finding is automatically exploitable.
🎯 Why this project?

Traditional manual CSRF assessment can become repetitive:

Open Page
   ↓
Find Forms
   ↓
Inspect Inputs
   ↓
Search for CSRF Token
   ↓
Inspect Cookies
   ↓
Check Requests
   ↓
Document Result
   ↓
Repeat...


CSRF AUTOMATION turns this into:

             ┌─────────────────────┐
             │   START SCAN 🚀     │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │  DISCOVER PAGES 🌐  │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │   FIND FORMS 📝     │
             └──────────┬──────────┘
                        ↓
          ┌─────────────┴─────────────┐
          ↓                           ↓
   🛡️ TOKEN CHECK              🍪 COOKIE CHECK
          │                           │
          └─────────────┬─────────────┘
                        ↓
                 📡 ANALYSIS
                        ↓
                  📊 REPORT
                        ↓
             ┌──────────┼──────────┐
             ↓          ↓          ↓
           JSON       HTML       LIVE UI

🧠 Core Architecture
flowchart TB

    USER(["👤 Security Tester"])

    CLI["🖥️ CLI / Input"]

    CONFIG["⚙️ Configuration"]

    SESSION["🔐 Session Factory"]

    CRAWLER["🕷️ Smart Crawler"]

    TARGET["🌐 Authorized Web Application"]

    FORMS["📝 Form Collector"]

    TOKEN["🛡️ Token Detector"]

    COOKIE["🍪 Cookie Analyzer"]

    REQUEST["📡 Request Analyzer"]

    RESULT["📊 Findings Engine"]

    JSON["📄 JSON Report"]

    HTML["🌐 HTML Report"]

    LOG["📜 Logs"]

    MONITOR["📈 Live Monitor"]

    USER --> CLI
    CLI --> CONFIG
    CONFIG --> SESSION

    SESSION --> CRAWLER
    CRAWLER <--> TARGET

    CRAWLER --> FORMS
    CRAWLER --> COOKIE

    FORMS --> TOKEN
    FORMS --> REQUEST

    TOKEN --> RESULT
    COOKIE --> RESULT
    REQUEST --> RESULT

    RESULT --> JSON
    RESULT --> HTML
    RESULT --> LOG
    RESULT --> MONITOR

    MONITOR --> USER
    JSON --> USER
    HTML --> USER

🔥 Features
Feature	Description
🕷️ Web Crawler	Discovers pages and forms
📝 Form Detection	Finds HTML forms automatically
🛡️ CSRF Token Detection	Searches for token-like fields
🍪 Cookie Analysis	Observes cookie security attributes
🔐 Authenticated Scanning	Supports authorized cookie-file sessions
🎭 JavaScript Rendering	Optional Playwright support
📊 JSON Reports	Machine-readable results
🌐 HTML Reports	Human-readable reports
📈 Live Monitoring	Monitor scanner progress
📜 Logging	Detailed scan logs
🚫 Scope Control	Restrict crawler boundaries
⏱️ Request Delay	Control request frequency
🔄 THE SCAN PIPELINE
flowchart LR

    A["🚀 START"] --> B["🌐 TARGET"]

    B --> C["🕷️ CRAWL"]

    C --> D["📄 PAGE"]

    D --> E["📝 FORM"]

    E --> F["🛡️ TOKEN"]

    E --> G["📡 REQUEST"]

    D --> H["🍪 COOKIE"]

    F --> I["🧠 ANALYZE"]
    G --> I
    H --> I

    I --> J{"Potential Issue?"}

    J -->|YES| K["⚠️ REVIEW"]

    J -->|NO| L["✅ PROTECTED / INFO"]

    K --> M["📊 REPORT"]
    L --> M

    M --> N["📄 JSON"]
    M --> O["🌐 HTML"]
    M --> P["📈 MONITOR"]

🛡️ CSRF Detection Logic

The scanner looks for indicators, not guaranteed vulnerabilities.

flowchart TD

    FORM["📝 HTML FORM"]

    METHOD["HTTP METHOD"]

    ACTION["FORM ACTION"]

    INPUTS["INPUT FIELDS"]

    TOKEN["🔎 TOKEN-LIKE FIELD"]

    COOKIE["🍪 COOKIE OBSERVATION"]

    ANALYZE["🧠 HEURISTIC ANALYSIS"]

    RESULT{"Result"}

    HIGH["🔴 Potentially Significant"]

    MEDIUM["🟠 Potential Issue"]

    INFO["🔵 Informational"]

    REVIEW["🟡 Manual Review"]

    FORM --> METHOD
    FORM --> ACTION
    FORM --> INPUTS

    INPUTS --> TOKEN
    FORM --> COOKIE

    METHOD --> ANALYZE
    ACTION --> ANALYZE
    TOKEN --> ANALYZE
    COOKIE --> ANALYZE

    ANALYZE --> RESULT

    RESULT --> HIGH
    RESULT --> MEDIUM
    RESULT --> INFO
    RESULT --> REVIEW

🔎 A scanner result is not proof of exploitability. Manual validation is required.
🕷️ CRAWLER FLOW
flowchart TD

    START(["🌐 START URL"])

    FETCH["📡 Fetch Page"]

    PARSE["🔍 Parse HTML"]

    LINKS["🔗 Extract Links"]

    FORMS["📝 Extract Forms"]

    COOKIE["🍪 Record Cookies"]

    SCOPE{"Within Scope?"}

    QUEUE["📋 Add to Crawl Queue"]

    SKIP["⏭️ Skip"]

    MORE{"More Pages?"}

    DONE(["✅ Crawl Complete"])

    START --> FETCH
    FETCH --> PARSE

    PARSE --> LINKS
    PARSE --> FORMS
    PARSE --> COOKIE

    LINKS --> SCOPE

    SCOPE -->|YES| QUEUE
    SCOPE -->|NO| SKIP

    QUEUE --> MORE
    FORMS --> MORE
    COOKIE --> MORE

    MORE -->|YES| FETCH
    MORE -->|NO| DONE

🎭 JavaScript Rendering

For modern JavaScript-heavy applications, optional browser rendering can be enabled.

flowchart LR

    PAGE["🌐 Web Page"]

    CHECK{"JavaScript Required?"}

    HTTP["📡 HTTP Request"]

    PLAYWRIGHT["🎭 Playwright"]

    DOM["📄 Final DOM"]

    ANALYZE["🔎 Analyze"]

    PAGE --> CHECK

    CHECK -->|NO| HTTP
    CHECK -->|YES| PLAYWRIGHT

    HTTP --> DOM
    PLAYWRIGHT --> DOM

    DOM --> ANALYZE


Install browser support:

pip install -r requirements-browser.txt
python -m playwright install chromium

🍪 AUTHENTICATED SCANNING

Authorized browser cookies can be supplied using a Netscape/Mozilla-format cookie file.

sequenceDiagram

    actor Tester
    participant Browser
    participant CookieFile
    participant Scanner
    participant Target

    Tester->>Browser: Login
    Browser->>CookieFile: Export authorized cookies
    Tester->>Scanner: Provide cookie file
    Scanner->>Scanner: Load cookies
    Scanner->>Target: Authenticated request
    Target-->>Scanner: Response
    Scanner->>Scanner: Analyze forms
    Scanner-->>Tester: Generate report


⚠️ Treat cookie files like passwords.

📊 REPORTING ENGINE

One scan → multiple outputs.

                       📊 SCAN RESULTS
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
          📄 JSON         🌐 HTML        📜 LOGS
              │              │              │
              ▼              ▼              ▼
        Automation      Human Review     Debugging

JSON
output/report.json

HTML
output/report.html

Logs
logs/scan_log.txt

📈 LIVE MONITORING

The project includes a monitoring interface for observing the scan while it is running.

flowchart LR

    SCANNER["🛡️ Scanner"]

    STATUS["⚡ Status"]
    SITE["🌐 Current Site"]
    FORM["📝 Current Form"]
    STATS["📊 Statistics"]
    LOGS["📜 Logs"]
    PROGRESS["⏳ Progress"]

    API["🔌 Monitoring API"]

    UI["🖥️ Dashboard"]

    SCANNER --> STATUS
    SCANNER --> SITE
    SCANNER --> FORM
    SCANNER --> STATS
    SCANNER --> LOGS
    SCANNER --> PROGRESS

    STATUS --> API
    SITE --> API
    FORM --> API
    STATS --> API
    LOGS --> API
    PROGRESS --> API

    API --> UI

Dashboard Concept
┌──────────────────────────────────────────────────────┐
│              🛡️ CSRF AUTOMATION MONITOR             │
├──────────────────────────────────────────────────────┤
│                                                      │
│  STATUS        🟢 RUNNING                            │
│                                                      │
│  CURRENT SITE  https://target.example                │
│                                                      │
│  CURRENT FORM  /account/update                       │
│                                                      │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐       │
│  │ 🌐 SITES   │ │ 📝 FORMS   │ │ 🛡️ TOKENS │       │
│  │     12     │ │     47     │ │     31     │       │
│  └────────────┘ └────────────┘ └────────────┘       │
│                                                      │
│  PROGRESS                                           │
│  ███████████████████████░░░░░  78%                 │
│                                                      │
│  📜 LIVE LOGS                                        │
│  ├─ Page discovered                                  │
│  ├─ Form analyzed                                    │
│  ├─ Token detected                                   │
│  └─ Report updated                                   │
│                                                      │
└──────────────────────────────────────────────────────┘

🗂️ PROJECT STRUCTURE
CSRF_AUTOMATION/
│
├── 🧠 main.py
├── ⚙️ config.py
├── 📊 event_report.py
│
├── 📈 monitor.py
├── 🖥️ monitor.html
├── 🖥️ monitor1.html
├── 📈 scanner_monitor.py
│
├── 🧪 test_target_app.py
├── 📄 Untitled-1.html
│
├── 📦 requirements.txt
├── 🎭 requirements-browser.txt
├── 🚫 .gitignore
│
├── modules/
│   ├── 🕷️ form_collector.py
│   ├── 🔐 session_factory.py
│   ├── 🛡️ token_detector.py
│   ├── 📡 request_analyzer.py
│   ├── 📊 report_generator.py
│   └── 🖥️ result_display.py
│
├── utils/
│   ├── 🖥️ cli_input.py
│   └── 📜 logger.py
│
├── output/
│   ├── 📄 report.json
│   ├── 🌐 report.html
│   └── events/
│
├── logs/
│   └── 📜 scan_log.txt
│
└── data/
    └── users.db

🚀 INSTALLATION
1️⃣ Clone
git clone https://github.com/cybernathiya/CSRF_AUTOMATION.git
cd CSRF_AUTOMATION

2️⃣ Virtual Environment
Linux / macOS
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install
pip install -r requirements.txt

▶️ RUN
python main.py


Follow the prompts to configure the authorized target and scan parameters.

🎭 OPTIONAL BROWSER MODE
pip install -r requirements-browser.txt


Then:

python -m playwright install chromium

📸 SCREENSHOTS

Add your project screenshots here:

images/
├── scanner.png
├── dashboard.png
├── report.png
├── json-report.png
└── event-report.png

🖥️ Scanner

<p align="center"> <img src="images/scanner.png" width="90%" alt="CSRF Automation Scanner"> </p>

📈 Monitoring Dashboard

<p align="center"> <img src="images/dashboard.png" width="90%" alt="CSRF Automation Dashboard"> </p>

📊 Security Report

<p align="center"> <img src="images/report.png" width="90%" alt="CSRF Security Report"> </p>

🔬 EXAMPLE WORKFLOW
        👤 SECURITY TESTER
                 │
                 ▼
        ┌─────────────────┐
        │ python main.py  │
        └────────┬────────┘
                 │
                 ▼
          🌐 TARGET URL
                 │
                 ▼
          🕷️ CRAWLER
                 │
          ┌──────┴──────┐
          ▼             ▼
       📝 FORMS      🍪 COOKIES
          │             │
          ▼             │
    🛡️ TOKEN CHECK     │
          │             │
          └──────┬──────┘
                 ▼
          📡 ANALYZER
                 │
                 ▼
          📊 FINDINGS
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
      JSON      HTML      LIVE
       │         │         │
       ▼         ▼         ▼
     🤖 CI     👤 USER    📈 UI

🧩 TECHNOLOGY STACK

<p align="center">

Technology	Role
🐍 Python	Core engine
🌐 Requests	HTTP communication
🍲 BeautifulSoup	HTML parsing
⚡ lxml	HTML/XML processing
🎨 Jinja2	Report templates
🖍️ Colorama	CLI formatting
📋 Tabulate	Console tables
🎭 Playwright	JavaScript rendering
🛡️ OWASP ZAP Client	Security tooling integration

</p>

🧠 SECURITY MODEL
flowchart TD

    AUTH["🔐 AUTHORIZED TESTING"]

    TARGET["🌐 Target Application"]

    SCAN["🛡️ Scanner"]

    OBSERVE["🔎 Observe"]

    ANALYZE["🧠 Analyze"]

    REPORT["📊 Report"]

    REVIEW["👤 Human Review"]

    AUTH --> TARGET
    AUTH --> SCAN

    SCAN --> TARGET
    TARGET --> OBSERVE

    OBSERVE --> ANALYZE
    ANALYZE --> REPORT

    REPORT --> REVIEW

    REVIEW --> DECISION{"Security Decision"}

    DECISION -->|Protected| SAFE["✅ Documented"]
    DECISION -->|Potential Issue| INVESTIGATE["🔎 Investigate"]

⚠️ IMPORTANT LIMITATIONS

This project is intentionally designed as a heuristic assessment tool.

It does not:

❌ Automatically prove exploitability
❌ Submit discovered forms
❌ Bypass CSRF protections
❌ Guarantee complete application coverage
❌ Replace manual penetration testing


It does:

✅ Discover pages
✅ Discover forms
✅ Inspect fields
✅ Identify token-like indicators
✅ Observe cookies
✅ Analyze request characteristics
✅ Generate reports
✅ Provide monitoring information

🛡️ RESPONSIBLE USE

Use this project only against:

✅ Your own applications
✅ Local test environments
✅ CTF/lab environments
✅ Applications where you have explicit authorization


Do not scan systems without permission.

📚 REFERENCES
OWASP CSRF Prevention Cheat Sheet
OWASP Web Security Testing Guide
MDN Web Security
🗺️ ROADMAP
timeline

    title CSRF AUTOMATION

    Current
        : 🕷️ Form Discovery
        : 🛡️ Token Detection
        : 🍪 Cookie Analysis
        : 📡 Request Analysis
        : 📄 JSON Reports
        : 🌐 HTML Reports
        : 📈 Monitoring

    Next
        : 🎭 Better JavaScript Crawling
        : 🧠 Improved Detection Rules
        : 📊 Better Visualizations

    Future
        : 🔄 CI/CD Integration
        : 🧪 Automated Regression Testing
        : 🔐 Advanced Authentication
        : 📈 Advanced Analytics

⭐ PROJECT IN ONE IMAGE
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║              🛡️  CSRF AUTOMATION                        ║
║                                                          ║
║       ┌───────────────┐                                  ║
║       │  🌐 TARGET    │                                  ║
║       └───────┬───────┘                                  ║
║               ▼                                          ║
║       ┌───────────────┐                                  ║
║       │  🕷️ CRAWLER  │                                  ║
║       └───────┬───────┘                                  ║
║               ▼                                          ║
║       ┌───────────────┐                                  ║
║       │  📝 FORMS     │                                  ║
║       └───────┬───────┘                                  ║
║               ▼                                          ║
║      ┌────────┴─────────┐                                ║
║      ▼                  ▼                                ║
║  🛡️ TOKEN            🍪 COOKIE                           ║
║  ANALYSIS             ANALYSIS                           ║
║      │                  │                                ║
║      └────────┬─────────┘                                ║
║               ▼                                          ║
║       ┌───────────────┐                                  ║
║       │ 🧠 ANALYZER   │                                  ║
║       └───────┬───────┘                                  ║
║               ▼                                          ║
║       ┌───────────────┐                                  ║
║       │ 📊 FINDINGS   │                                  ║
║       └───────┬───────┘                                  ║
║               │                                          ║
║       ┌───────┼────────┐                                 ║
║       ▼       ▼        ▼                                 ║
║     📄 JSON  🌐 HTML  📈 LIVE                            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

👨‍💻 AUTHOR

<p align="center">

<b>cybernathiya</b>

<br><br>

<a href="https://github.com/cybernathiya"> <img src="https://img.shields.io/badge/GitHub-cybernathiya-181717?style=for-the-badge&logo=github" /> </a>

</p>

<p align="center">

🔐 Build • Scan • Analyze • Secure

<b>CSRF AUTOMATION</b>

<br>

For authorized security testing and educational purposes.

</p>
