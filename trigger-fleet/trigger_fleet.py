import io
import os
import time

import pandas
import requests

# BASE_URL = "https://api.app.shipyardapp.com"

BASE_URL = "https://api.int.shipyardapp.io"
ORG_ID = os.getenv("ORG_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
FLEET_ID = os.getenv("FLEET_ID")
OVERRIDES = os.getenv("OVERRIDES")
API_KEY = os.environ["SHIPYARD_API_KEY"]
WAIT_TIME = os.getenv("WAIT_TIME", 5)
WAIT_FOR_RUN = os.getenv("WAIT_FOR_RUN", "false").lower() == "true"

HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-Shipyard-API-Key": API_KEY
}

COMPLETED_STATUSES = ["Success", "Errored", "Terminated"]


def get_run_status(run_id):
    log_response = requests.get(f"{BASE_URL}/orgs/{ORG_ID}/projects/{PROJECT_ID}/fleets/{FLEET_ID}/fleetruns?days=1",
                                headers=HEADERS)

    log_data = log_response.content.decode('utf-8')

    df = pandas.read_csv(io.StringIO(log_data))
    fleet_run = df[df['Fleet Log ID'] == run_id]
    return fleet_run["Status"].values[0]


def trigger_fleet_run():

    if OVERRIDES:
        print("Triggering fleet run with overrides")
        response = requests.post(f"{BASE_URL}/orgs/{ORG_ID}/projects/{PROJECT_ID}/fleets/{FLEET_ID}/fleetruns",
                                 headers=HEADERS,
                                 data=OVERRIDES)
    else:
        response = requests.post(f"{BASE_URL}/orgs/{ORG_ID}/projects/{PROJECT_ID}/fleets/{FLEET_ID}/fleetruns",
                                 headers=HEADERS)

    if response.ok:
        print("Fleet run triggered successfully")
        response_json = response.json()
        if log := response_json.get("log"):
            print(log)
        return response_json
    else:
        print("Fleet run trigger failed")
        print(response.content)
        exit(1)

run_id = trigger_fleet_run().get("data").get("fleet_run_id")
if WAIT_FOR_RUN:

    while True:
        time.sleep(WAIT_TIME)
        status = get_run_status(run_id)
        print(f"Run status: {status}")

        if status in COMPLETED_STATUSES:
            print("Run completed")
            if status != "Success":
                exit(1)
            break

        print("Waiting for run to complete...")
