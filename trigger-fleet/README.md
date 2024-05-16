# Trigger Shipyard Fleet GitHub Action

This action allows you to trigger a Shipyard fleet based on GitHub events such as commits, pull request openings, or merges.

### Creating and Configuring the Workflow

Create a YAML file in the `.github/workflows` directory of your repository with the following configuration:

```yaml
name: Trigger Shipyard Fleet on Push
on:
  push:
    branches:
      - main

jobs:
  trigger-fleet:
    runs-on: ubuntu-latest
    steps:
    - name: Trigger Shipyard Fleet
      uses: shipyardapp/shipyard-actions/trigger-fleet@v1
      with:
        org_id: 'your-organization-id'
        project_id: 'your-project-id'
        fleet_id: 'your-fleet-id'
        overrides: '{
    "vessel_overrides": [
        {
            "name": "Execute Python Script",
            "environment_variable_overrides": {
                "name": "NEW VALUE"
            }
        }
    ]
}'
        shipyard_api_key: ${{ secrets.SHIPYARD_API_KEY }}
        wait_for_run: 'false'
        wait_time: 5
```
### Action Inputs:

* org_id: Your organization ID in Shipyard.
* project_id: Your project ID in Shipyard.
* fleet_id: The ID of the fleet you want to trigger.
* overrides: JSON string of parameters to override the default fleet settings (optional).
* shipyard_api_key: Your Shipyard API key, stored securely in GitHub secrets.
* wait_for_run: Whether to wait for the fleet run to complete before the action finishes. **NOTE:** The success of the action will be determined by the final status of the fleet run. (default: false).
* wait_time: Time in seconds to wait before rechecking the fleet run status if wait_for_run is set to true (default: 5).