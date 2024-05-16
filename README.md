# Shipyard Actions

This repository contains GitHub Actions designed to interact with Shipyard, allowing seamless integration with your CI/CD workflows. These actions enable you to dynamically trigger or update Shipyard fleets based on GitHub events like commits, pull requests, or merges.

## Actions Included

1. **Trigger Shipyard Fleet GitHub Action** - Trigger a Shipyard fleet using GitHub events.
2. **Upsert Fleet Action for Shipyard** - Update or create a fleet configuration in Shipyard from a YAML file in your repository.

## Prerequisites

Before you use these actions, you need:
- A Shipyard account.
- An API key from Shipyard for authentication.

### Storing Your Shipyard API Key

Your Shipyard API key should be stored as a secret in your GitHub repository:
1. Navigate to your repository on GitHub.
2. Go to 'Settings' > 'Secrets' and click on 'New repository secret'.
3. Name the secret `SHIPYARD_API_KEY` and paste your Shipyard API key as the value.
4. Click 'Add secret'.

## Usage

Each action has its detailed usage instructions in its respective directory. See the links below for specific guidance:
- [Trigger Shipyard Fleet Action](./trigger-fleet/README.md)
- [Upsert Fleet Action](./upsert-fleet/README.md)

## Contributing

Contributions are welcome! Please read our contributing guidelines for how to propose updates or improvements.
