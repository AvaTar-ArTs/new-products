# Commercial Foundry Architecture

```text
source repositories and local assets
                ↓
        catalog + evidence
                ↓
       opportunity scoring
                ↓
 product packages and shared runtime
                ↓
 GitHub / PyPI / npm / MCP / Gumroad / Product Hunt / services
                ↓
        launch and usage metrics
```

The repository must not become a dump of private terminal history, credentials,
model blobs, or raw workstation exports. Ingest locally, classify, redact or
reference, and explicitly export only sanitized artifacts.

Product packages may depend on source repositories, but each dependency must
be recorded in the catalog with a version, license, and integration boundary.
