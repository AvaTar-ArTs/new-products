# WorkVault Control launch brief

## One-line pitch

WorkVault Control makes long-running Mac maintenance and local-AI operations
observable, cancellable, and resumable.

## The problem

Homebrew upgrades, cleanup scripts, model checks, and agent processes often
run for a long time. When a terminal closes or a network step stalls, users
cannot tell what finished, what remains, or which child processes are safe to
kill.

## Demo sequence

```bash
wv plan
wv apply ollama
wv status
wv logs RUN_ID
wv report RUN_ID
```

## Audience

AI-heavy Mac developers, consultants, solo founders, and creative technologists
who run multiple package managers, local models, agents, and automation scripts.

## Offer

- Free local CLI for personal use.
- Pro desktop/control-room edition for $39.
- Optional team history and shared reports for $12/month.

## Trust message

Local-first. No account required. Plans are read-only. Cleanup is separate from
updates. Every run has logs, status, and an evidence-backed report.
