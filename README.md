# WorkVault Maintenance

Observable, resumable maintenance for macOS developer and AI workstations.

This is the first executable product in the AvaTar-ArTs product portfolio.
The portfolio strategy and product specifications live in
[`docs/MARKET-PORTFOLIO-2026-09-04.md`](docs/MARKET-PORTFOLIO-2026-09-04.md),
with the shared product catalog in [`products/product-catalog.json`](products/product-catalog.json).

WorkVault Maintenance is the first product in the AvaTar-ArTs `new-products`
repository. It turns package updates, local-AI checks, and cleanup workflows
into inspectable runs instead of fragile terminal one-liners.

## Current release: 0.1.0

The zero-dependency runtime provides:

- read-only plans before mutation
- Homebrew, MacPorts, and Ollama detection
- one durable run directory per operation
- JSONL event history and per-step logs
- process-group cancellation for Ctrl-C/Ctrl-\n+- timeouts and SIGKILL escalation
- exclusive locking to prevent overlapping runs
- status, logs, reports, and resume commands

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .

wv plan
wv apply brew
wv status
wv report RUN_ID
wv logs RUN_ID
wv resume RUN_ID
```

Run data is stored in `~/.workvault-maintenance/runs/`, or in `WV_HOME` when
set. The first version intentionally keeps provider logic small and explicit;
the next phase adds a proper provider protocol, heartbeat monitoring,
checkpoint-aware cancellation, cleanup analysis, and WorkVault event-schema
integration.

## Safety model

`plan` never mutates the machine. `apply` is explicit. Cleanup is not bundled
into ordinary updates. Provider output is written to logs and the terminal
only displays a compact summary. No secrets or command output are sent to a
remote service.

## Roadmap

1. provider protocol and capability probes
2. heartbeat/stall detection and cancellation-aware resume
3. Homebrew bottle/source-build risk scoring for Intel Macs
4. cleanup scan with quarantine/trash recovery
5. WorkVault canonical events and SQLite materialized views
6. iTerm2 status-bar/control-room renderer and optional MCP read layer
7. signed releases and launchd scheduling

## License

MIT
