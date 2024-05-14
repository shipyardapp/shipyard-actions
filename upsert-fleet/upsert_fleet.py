import argparse
import sys

import yaml
from shipyard_api import ShipyardClient



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--organization-id", dest="org_id", required=True)
    parser.add_argument("--api-key", dest="api_key", required=True)
    parser.add_argument("--project-id", dest="project_id", required=True)
    parser.add_argument("--yaml-path", dest="yaml_path", required=True)
    return parser.parse_args()


def main():
    args = get_args()
    client = ShipyardClient(org_id=args.org_id, api_key=args.api_key, project_id=args.project_id)

    with open(args.yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    response = client.upsert_fleet(data)
    if response.ok:
        print("Fleet upserted successfully")
    else:
        print("Fleet upsert failed")
        print(response.content)
        sys.exit(1)


if __name__ == "__main__":
    main()
