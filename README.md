# shipyard-actions
# Trigger Shipyard Fleet GitHub Action

This GitHub Action allows you to trigger a Shipyard fleet based on GitHub events such as commits, pull request openings, or merges. It's designed to integrate seamlessly with your CI/CD workflows, providing a dynamic way to interact with Shipyard directly from GitHub.

## Prerequisites

Before you begin, you will need:
- A Shipyard account with an active fleet.
- An API key from Shipyard for authentication.

## Setup

### 1. Storing Your Shipyard API Key

For security reasons, your Shipyard API key should be stored as a secret in your GitHub repository:
- Navigate to your repository on GitHub.
- Go to 'Settings' > 'Secrets' and click on 'New repository secret'.
- Name the secret `SHIPYARD_API_KEY` and paste your Shipyard API key as the value.
- Click 'Add secret'.

### 2. Creating the Workflow

Create a YAML file in the `.github/workflows` directory of your repository. If this directory does not exist, you will need to create it.

### 3. Configuring the Workflow

Here is a sample workflow configuration. This example triggers the Shipyard fleet whenever a push is made to the `main` branch:

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
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Trigger Shipyard Fleet
      uses: shipyardapp/shipyard-actions/trigger-fleet@v1
      with:
        org_id: 'your-organization-id'
        project_id: 'your-project-id'
        fleet_id: 'your-fleet-id'
        overrides: '{}'
        shipyard_api_key: ${{ secrets.SHIPYARD_API_KEY }}
        wait_for_run: 'false'
        wait_time: '5'
```
Replace your-organization-id, your-project-id, and your-fleet-id with the actual IDs from your Shipyard setup.

**Parameters**

* org_id: The organization ID in Shipyard where the fleet is located.
* project_id: The project ID within the organization in Shipyard.
* fleet_id: The ID of the fleet you want to trigger.
* overrides: JSON string of parameters to override the default fleet settings (optional).
* shipyard_api_key: Your Shipyard API key, stored securely in GitHub secrets.
* wait_for_run: Whether to wait for the fleet run to complete before the action finishes (default: false).
* wait_time: Time in seconds to wait before rechecking the fleet run status if wait_for_run is set to true (default: 5).

# Upsert Fleet Action for Shipyard

This GitHub Action allows you to upsert a fleet configuration in Shipyard from a YAML file located in your GitHub repository. It is designed to integrate seamlessly with your CI/CD workflows, enabling dynamic configuration of fleet settings directly from your repository.

## Prerequisites

Before you begin, you will need:
- A Shipyard account with appropriate permissions.
- An API key from Shipyard.
- The IDs for your organization, project, and fleet, obtainable from your Shipyard dashboard.

## Usage

To use this action, you will need to set up several secrets in your GitHub repository for security. These include your Shipyard API key, organization ID, project ID, and fleet ID. Additionally, you will specify the path to your fleet configuration YAML file in your workflow file.

### Setup GitHub Secrets

Go to your repository settings in GitHub, find the "Secrets" section, and add the following secrets:
- `SHIPYARD_API_KEY`: Your Shipyard API key.
- `ORG_ID`: Your Shipyard organization ID.
- `PROJECT_ID`: Your Shipyard project ID.
- `FLEET_ID`: Your Shipyard fleet ID.

### Workflow Configuration

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
          org_id: ${{ secrets.ORG_ID }}
          project_id: ${{ secrets.PROJECT_ID }}
          yaml_path: 'path/to/fleet-config.yaml'
```
Action Inputs
* org_id	The ID of your Shipyard organization
* project_id	The ID of your Shipyard project
* yaml_path	Relative path to the YAML file in your repository	Yes

Additional Notes
Ensure that the path to the YAML configuration file (yaml_path) starts from the root of your repository.
If your repository includes submodules containing the YAML file, modify the actions/checkout step to check out submodules by adding submodules: 'recursive'.