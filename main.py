"""
Entry point for an authorized, bounded CSRF signal scan.
"""

import config
import http.cookiejar
from utils.cli_input import get_user_inputs
from utils.logger import ScanLogger
from modules.form_collector import FormCollector
from modules.session_factory import create_session
from modules.token_detector import TokenDetector
from modules.request_analyzer import RequestAnalyzer
from modules.report_generator import ReportGenerator
from modules.result_display import ResultDisplay


def main():
    print("=" * 60)
    print(" CSRF Vulnerability Detection Automation Tool")
    print("=" * 60)

    logger = ScanLogger(config.LOG_PATH)
    user_input = get_user_inputs()
    logger.log_start(
        "Cookie file" if user_input["cookie_file"] else "Not used",
        user_input["start_urls"]
    )

    proxy = config.PROXY if config.USE_PROXY else None
    try:
        session = create_session(
            cookie_file=user_input["cookie_file"],
            proxy=proxy
        )
    except (OSError, http.cookiejar.LoadError) as error:
        logger.log_error(f"Could not prepare scanner session: {error}")
        print(f"[SESSION ERROR] Could not prepare scanner session: {error}")
        return

    form_collector = FormCollector(session, delay=user_input["delay"])
    try:
        forms = form_collector.collect_sites(
            user_input["start_urls"],
            max_pages=user_input["max_pages"],
            scope=user_input["scope"],
            exclusions=user_input["exclusions"],
            render_js=user_input["render_js"],
        )
    except RuntimeError as error:
        logger.log_error(str(error))
        print(f"[SCANNER ERROR] {error}")
        return

    token_detector = TokenDetector()
    request_analyzer = RequestAnalyzer(
        session,
        cookie_observations=form_collector.cookie_observations
    )
    report_generator = ReportGenerator()

    for form in forms:
        token_result = token_detector.check_form(form)
        request_result = request_analyzer.analyze(form)
        report_generator.add_result(form, token_result, request_result)

    scan_metadata = {
        "start_urls": user_input["start_urls"],
        "scope": user_input["scope"],
        "max_pages": user_input["max_pages"],
        "request_delay_seconds": user_input["delay"],
        "render_js": user_input["render_js"],
        "crawler": form_collector.scan_stats,
    }
    report = report_generator.save_json(
        config.OUTPUT_JSON_PATH,
        scan_metadata=scan_metadata
    )

    display = ResultDisplay()
    display.print_console_summary(report_generator.results)
    display.render_html(
        report_generator.results,
        config.OUTPUT_HTML_PATH,
        scan_metadata={
            **report["scan"],
            "generated_at": report["generated_at"],
        }
    )

    logger.log_crawl_summary(form_collector.scan_stats)
    logger.log_summary(report_generator.results)

    print("\nScan complete. Open output/report.html for findings and crawl details.")
    print(f"Run history saved to {config.LOG_PATH}")


if __name__ == "__main__":
    main()
