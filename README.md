# sync-projectv2-field

An action to sync values between items and organization-level (v2) project boards

### Required inputs

- `org`: The name of the organization where the ProjectV2 board lives
- `project_id`: The number of the project to update
- `item_property`: The property of [the ProjectV2 item](https://docs.github.com/en/graphql/reference/objects#projectv2item)
- `sync_field`: The name of the field to sync the value for
- `github_token`: A personal access token (PAT) with `project` write access

> DO NOT hard-code your token in the Action config! This is a major security issue! Use repository secrets to store the token.

### Example config

The following configuration will run the sync each time a push is made to the repo:

```
name: Test Action
on: [push]

jobs:
  sync-field:
    runs-on: ubuntu-latest
    name: Run the project field sync
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Run the sync
        id: run-sync
        uses: ./
        with:
          project_id: 10068
          item_property: "created"
          org: "github"
          sync_field: "Open Date"
          github_token: ${{ secrets.AUTOMATION_TOKEN }}
```