# AvaTar-ArTs Product Portfolio

**Date:** 2026-09-04  
**Purpose:** Convert existing AvaTar-ArTs capabilities into products that can
be shipped, marketed, and sold without creating five unrelated codebases.

## Executive decision

Build one shared local-first runtime and sell several focused products around
it. The flagship should be **WorkVault Control**, a macOS control plane for
AI-powered developer workstations. It combines maintenance, agent operations,
local-AI inventory, cleanup intelligence, and evidence-backed reports.

The commercial wedge is not another package updater or Mac cleaner. It is:

> **Know what your AI workstation is doing, why it is doing it, and recover
> when it fails.**

## Market signals

The current market is crowded, but the demand is clear:

| Signal | Evidence | Product implication |
|---|---|---|
| Multi-manager updates | Topgrade detects tools and runs the appropriate package-manager commands | Provider adapters are table stakes |
| Mac cleanup and monitoring | Mole combines cleanup, uninstall, disk analysis, optimization, and live health | Cleanup must include analysis, history, and recovery |
| Background installation | Package Mate queues Homebrew jobs, daemonizes work, and exposes a dashboard | Long jobs need durable status and cancellation |
| Agentic development | Product Hunt’s AI coding-agent category is full of model-selectable and autonomous coding products | Approval, evidence, and cost controls are opportunities |
| Local AI and desktop agents | Current open-source projects emphasize local models, tool calling, and computer use | Model/service health belongs in the workstation inventory |
| Developer + AI cache growth | Your Mac contains Homebrew, Python, npm, Ollama, Docker, editor, and media tooling | A specialized developer/AI cleanup product has a concrete buyer |

Sources: [Topgrade](https://github.com/topgrade-rs/topgrade),
[Mole](https://github.com/tw93/Mole),
[Package Mate](https://www.producthunt.com/products/package-mate-open-source-cli-for-macos),
[Product Hunt AI coding agents](https://www.producthunt.com/categories/ai-coding-agents).

Claims about “300%+ growth” should be treated as hypotheses until the product
has a dated metric, baseline, and source. Launch rankings, GitHub stars, and
social posts are demand signals—not proof of growth.

## Local capability inventory

The existing machine and repositories provide these reusable assets:

| Existing asset | Product value |
|---|---|
| `~/scripts/updater-pro.sh` | Provider orchestration, logs, profiles, terminal UX |
| `~/scripts/mac-cleanup-pro.sh` | Cleanup categories, dry-run flow, progress UI |
| `~/scripts/local-ecosystem-audit.py` | Bounded filesystem inspection and reports |
| `~/scripts/ollama-*` | Local model install, grouping, and lifecycle ideas |
| `agent_ops/` | JSONL events, spans, tool tracking, handoffs |
| WorkVault schemas/docs | Sessions, runs, artifacts, resources, provenance, recovery |
| `my-mcp-creator` | Bounded read-only project intelligence and redaction |
| iTerm2 profile and UI work | Control-room presentation and terminal-native workflow |
| Media/ffprobe scripts and CSVs | Creator asset inventory and batch processing |
| `~/pythons` and `~/scripts` | Large existing automation corpus to mine into adapters |
| Local apps: Ollama, OllaMan, Claude Terminal, Cursor, Windsurf, Obsidian | Immediate integrations and customer scenarios |

## Products to build and sell

### 1. WorkVault Control — flagship

**Buyer:** AI-heavy developers, consultants, solo founders, and small teams
with unreliable or crowded Mac workstations.

**Promise:** See every update, agent run, model service, process, failure, and
cleanup action in one recoverable timeline.

**MVP:**

- `wv plan`, `apply`, `status`, `logs`, `cancel`, `resume`, `report`
- Homebrew, MacPorts, Ollama adapters
- process-group cancellation and timeouts
- run lock and checkpoint files
- JSONL event stream plus HTML report
- Intel/Apple Silicon capability and risk report
- no cloud account required

**Pricing:** Free CLI; $39 one-time Pro desktop/control-room build; $9/month
optional sync and team history.

**Why it can win:** Topgrade updates and Mole cleans, but neither is designed
around agent-session provenance, local models, process recovery, or a durable
work history.

### 2. DevAI Cleanroom

**Buyer:** Developers and AI users running out of disk space or afraid to
delete caches.

**Promise:** Reclaim space from development and AI tools with an explanation
and recovery path for every item.

**MVP:**

- scan Homebrew, npm, pnpm, Yarn, pip, uv, Cargo, Go, Docker, Ollama,
  Xcode, IDE, and browser caches
- explain “safe / review / risky” per path
- quarantine to Trash or a recoverable staging area
- before/after storage report
- whitelist and policy files
- JSON/CSV export for consultants

**Pricing:** $19 one-time CLI; $29 desktop edition; $59 consultant license.

**Why it can win:** It specializes in the developer + AI footprint that
general Mac cleaners treat as generic cache data.

### 3. Agent Control Room

**Buyer:** Power users running Claude, Codex, Gemini, Qwen, Cursor, local
agents, and background scripts in parallel.

**Promise:** Know which agent is running, what it changed, what failed, and
how to resume it.

**MVP:**

- TTY/process/cwd/Git correlation
- session and run timeline
- child-process tree
- terminal status bar
- checkpoint and handoff generation
- read-only MCP interface
- explicit approval gates for filesystem and shell actions

**Pricing:** Free local mode; $49 Pro; $12/month team history.

**Why it can win:** This uses your WorkVault architecture directly and targets
the operational gap around autonomous coding tools.

### 4. Local AI Fleet Manager

**Buyer:** People running Ollama or llama.cpp across Intel Macs, Apple Silicon,
Linux boxes, and remote machines.

**Promise:** Inventory models, test endpoints, recommend a model for the
machine, and keep local AI services healthy.

**MVP:**

- Ollama endpoint discovery and health checks
- model inventory, disk usage, and last-used tracking
- Intel-aware model recommendations
- remote endpoint profiles
- prompt/latency smoke tests
- model backup/export manifest

**Pricing:** $29 one-time; $79 multi-machine edition.

**Why it can win:** Your existing `.ollama` analysis and Ollama scripts provide
the first real fixtures; the product stays useful even when one installer or
package manager fails.

### 5. Creator Asset Intelligence

**Buyer:** Artists, YouTubers, media freelancers, and agencies with large
video/image/audio archives.

**Promise:** Turn scattered media into a searchable, validated, duplicate-aware
asset library.

**MVP:**

- ffprobe/MediaInfo metadata extraction
- CSV/SQLite inventory
- duplicate and near-duplicate candidates
- portrait/short/video filters
- missing-file and stale-CSV comparison
- thumbnail/contact-sheet generation
- optional transcription and caption pipeline

**Pricing:** $39 one-time; $99 agency edition.

**Why it can win:** You already have real inventories across `DeVonDaTa`,
`2T-Xx`, `bakUp`, and local Movies, so this can be validated against real
work instead of synthetic sample data.

## Shared platform design

All products should share:

```text
workvault-core/
  runs/             durable jobs and checkpoints
  events/           append-only JSONL events
  adapters/         brew, macports, ollama, media, agents
  policy/           allowlists, protected paths, approval rules
  reports/          JSON, CSV, Markdown, HTML
  renderers/        plain, iTerm2, Rich/TUI, web
```

The shared event vocabulary should include:

```text
run.created
run.started
run.heartbeat
step.started
step.progress
step.stalled
step.cancelled
step.failed
step.succeeded
artifact.created
artifact.verified
resource.observed
policy.blocked
report.created
```

## Go-to-market order

1. **WorkVault Control CLI** — prove the reliability engine using your own
   Homebrew/Ollama failures.
2. **DevAI Cleanroom** — easiest paid utility and strongest immediate pain.
3. **Agent Control Room** — higher-value Pro product built on the same runs.
4. **Local AI Fleet Manager** — package the Ollama work separately.
5. **Creator Asset Intelligence** — sell into the AvaTar-ArTs creative
   audience once the shared inventory engine is stable.

## What not to build first

- a generic chatbot wrapper
- a full CleanMyMac clone
- another terminal emulator
- a cloud dashboard before the local event model works
- 20 package-manager adapters before cancellation/resume is reliable
- autonomous deletion or autonomous shell execution

## Success metrics

The first product should measure real utility:

- percentage of interrupted runs successfully resumed
- false-positive stall rate
- median time to understand a failure
- bytes reclaimed with no recovery incident
- percentage of steps with verified outcomes
- number of supported providers actually used
- conversion from free CLI to paid Pro
- repeat runs per user per month
