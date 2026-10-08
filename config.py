

#BASE_URL = "http://127.0.0.1:5000"

#PROFILES = [
    #{
      #  "id": i,
      #  "label": f"Site {i}",
     #   "login_url": f"{BASE_URL}/site/{i}/login",
    #    "register_url": f"{BASE_URL}/site/{i}/register",
   #     "targets": [
  #          f"{BASE_URL}/site/{i}/dashboard"
 #       ],
#    }
#    for i in range(1, 21)
#]

#USE_PROXY = False

#PROXY = {
#    "http": "http://127.0.0.1:8080",
#    "https": "http://127.0.0.1:8080",
#}

#OUTPUT_JSON_PATH = "output/report.json"
#OUTPUT_HTML_PATH = "output/report.html"
#LOG_PATH = "logs/scan_log.txt"

#DATABASE_PATH = "data/users.db"
#EVENT_REPORT_DIR = "output/events"

# Use an environment variable in a real deployment.
# This is a development-only fallback.
#SECRET_KEY = "change-this-development-secret"


import os

LOG_PATH = "logs/scan_log.txt"

DATABASE_PATH = "data/users.db"
EVENT_REPORT_DIR = "output/events"

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change-this-development-secret"
)