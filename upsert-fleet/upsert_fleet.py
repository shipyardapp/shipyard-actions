import os
import sys

import requests
import yaml

BASE_URL = "https://api.app.shipyardapp.com"
ORG_ID = os.getenv("ORG_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
API_KEY = os.environ["SHIPYARD_API_KEY"]
YAML_PATH = os.getenv("YAML_PATH")


def upsert_fleet():
    url = f"{BASE_URL}/orgs/{ORG_ID}/projects/{PROJECT_ID}/fleets"

    headers = {
        "accept": "application/json",
        "content-type": "application/yaml",
        "X-Shipyard-API-Key": API_KEY
    }

    with open(YAML_PATH, 'r') as file:
        data = yaml.safe_load(file)

    response = requests.put(url, headers=headers, data=yaml.dump(data), timeout=30)
    if response.ok:
        print("Fleet upserted successfully")
    else:
        print("Fleet upsert failed")
        print(response.content)
        sys.exit(1)


if __name__ == "__main__":
    upsert_fleet()
