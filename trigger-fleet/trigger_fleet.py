import time

from shipyard_api import ShipyardClient

COMPLETED_STATUSES = ["Success", "Errored", "Terminated"]

import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--organization-id", dest="org_id", required=True)
    parser.add_argument("--api-key", dest="api_key", required=True)
    parser.add_argument("--project-id", dest="project_id", required=True)
    parser.add_argument("--fleet-id", dest="fleet_id", required=True)
    parser.add_argument("--overrides", dest="overrides", required=False)
    parser.add_argument("--wait-time", dest="wait_time", required=False)
    parser.add_argument("--wait-for-run", dest="wait_for_run", required=False)
    return parser.parse_args()


def main():
    args = get_args()

    client = ShipyardClient(org_id=args.org_id, api_key=args.api_key, project_id=args.project_id)

    run_id = client.trigger_fleet(fleet_id=args.fleet_id,
                                      fleet_overrides=args.overrides).get("data").get("fleet_run_id")
    if args.wait_for_run:

        while True:
            time.sleep(int(args.wait_time))
            status = client.get_run_status(fleet_id=args.fleet_id, run_id=run_id)
            print(f"Run status: {status}")

            if status in COMPLETED_STATUSES:
                print("Run completed")
                if status != "Success":
                    exit(1)
                break

            print("Waiting for run to complete...")


if __name__ == "__main__":
    main()
