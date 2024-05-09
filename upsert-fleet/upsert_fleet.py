import os
import sys

import requests
import yaml

BASE_URL = "https://api.int.shipyardapp.io"
ORG_ID = os.getenv("ORG_ID")
PROJECT_ID = os.getenv("PROJECT_ID")
FLEET_ID = os.getenv("FLEET_ID")
API_KEY = os.environ["SHIPYARD_API_KEY"]
YAML_PATH = os.getenv("YAML_PATH")  # Get the path from environment variables


def upsert_fleet():
    url = f"{BASE_URL}/orgs/{ORG_ID}/projects/{PROJECT_ID}/fleets/{FLEET_ID}"  # Assuming you need FLEET_ID to upsert

    headers = {
        "accept": "application/json",
        "content-type": "application/yaml",
        "X-Shipyard-API-Key": API_KEY
    }

    # Load YAML from the specified file path
    with open(YAML_PATH, 'r') as file:
        data = yaml.safe_load(file)

    response = requests.put(url, headers=headers, data=yaml.dump(data))
    if response.ok:
        print("Fleet upserted successfully")
        print(response.text)
    else:
        print("Fleet upsert failed")
        print(response.content)
        sys.exit(1)


if __name__ == "__main__":
    upsert_fleet()
