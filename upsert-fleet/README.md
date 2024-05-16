# Upsert Fleet Action for Shipyard

This GitHub Action allows you to upsert a fleet configuration in Shipyard from a YAML file located in your GitHub repository.

## Prerequisites

- A Shipyard account with appropriate permissions.
- An API key from Shipyard.

## Workflow Configuration

Here is a sample workflow file to use the `upsert-fleet` action:

```yaml
name: Upsert Shipyard Fleet
on:
  push:
    paths:
      - 'path/to/your/yaml/**'
jobs:
  upsert_fleet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Upsert Fleet
        uses: shipyardapp/shipyard-actions/upsert-fleet@v1
        with:
          org_id: `your-org-id`
          project_id: `your-project-id`
          yaml_path: 'path/to/fleet-config.yaml'
          shipyard_api_key: ${{ secrets.SHIPYARD_API_KEY }}
```
### Action Inputs:
* org_id: Your organization ID in Shipyard.
* project_id: Your project ID in Shipyard.
* yaml_path: The path to the YAML file containing the fleet configuration.
* shipyard_api_key: Your Shipyard API key, stored securely in GitHub secrets.
