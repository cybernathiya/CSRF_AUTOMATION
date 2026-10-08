# CSRF Scanner

This is an educational, heuristic scanner for web apps you are authorized to
test. It crawls HTML links, inventories forms and cookie attributes, and emits
JSON and HTML reports. It does not submit forms or confirm exploitability.

## Run a scan

```powershell
.\venv\Scripts\python.exe .\main.py --url https://your-app.example/account/
```

The default crawl stays under the starting URL's path, is limited to 100 pages,
and pauses 0.2 seconds between page fetches. State-like paths such as `logout`,
`delete`, and `unsubscribe` are excluded by default. The scanner does not submit
forms, follow cross-origin links, or follow cross-origin redirects.

Useful options:

```text
--max-pages 250           Set a page cap (1 through 10000)
--scope origin            Crawl the whole starting origin instead of its path
--exclude admin           Exclude paths containing another path segment
--delay 0.5               Increase the pause between page fetches
--cookie-file cookies.txt Load a Netscape/Mozilla-format cookie file
--render-js               Render pages using optional Playwright Chromium
```

Multiple start URLs can be provided as:

```powershell
.\venv\Scripts\python.exe .\main.py --targets https://app.example/ https://app.example/account/
```

Authenticated scans can use a browser-exported Netscape/Mozilla cookie file.
Use an exporter that creates a Netscape `cookies.txt` file; the browser's
JSON storage-state export is not accepted by `--cookie-file`.
Cookie values are used only in memory for requests and are never written to the
reports or scan log. Common sensitive query parameters such as tokens,
passwords, and API keys are redacted in reports and scan logs. Protect the
cookie file like a password and remove it when the scan is complete. The
Netscape format does not reliably preserve SameSite
attributes; the report will show only cookie attributes the scanner actually
observes. If an imported cookie has not been re-observed in an HTTP
`Set-Cookie` response, its SameSite declaration is marked unavailable rather
than assumed to be absent.

## JavaScript-rendered pages

Playwright is optional. Install the browser-enabled requirements and Chromium:

```powershell
.\venv\Scripts\python.exe -m pip install -r .\requirements-browser.txt
.\venv\Scripts\python.exe -m playwright install chromium
```

Then add `--render-js` to the scan command. HTTP crawling remains the default.

## Interpreting the report

Reports are written to `output/report.json` and `output/report.html`. `HIGH` and
`MEDIUM` are potential issues requiring manual validation, not confirmed
vulnerabilities. A field whose name resembles a CSRF token may not be validated
by the server. Cookie names are only heuristics for identifying likely
authentication/session cookies, and SameSite behavior depends on browser
context. `INFO` marks GET/HEAD/OPTIONS forms because those methods should not
change application state; if they do, that is a separate application issue.
`REVIEW` means the scanner lacks enough evidence for a meaningful rating.

The scanner should be run only against systems for which you have explicit
authorization. It does not fill or submit forms, test token enforcement, or
explore application routes accessible only by non-link navigation.
