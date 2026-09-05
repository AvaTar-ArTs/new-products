# AvaTar-ArTs Product Ecosystem
## Comprehensive Product, App, Software, and Marketplace Handoff

Observed: 2026-09-05 UTC
Canonical workspace: `/Users/steven/iterm2/new-products`

## 1. Purpose of this handoff

This document records the current interpretation, evidence boundary, product architecture, candidate products, application formats, distribution channels, safety requirements, packaging state, and recommended next actions for the AvaTar-ArTs product ecosystem.

It is intended for:

- Steven;
- a future coding or product agent;
- an independent reviewer;
- a launch or packaging workflow;
- a later session that needs to continue without reconstructing the conversation.

This is a product and implementation handoff. It does not include raw conversation exports, credentials, private prompts, complete personal inventories, hidden chain-of-thought, or unreviewed source trees.

## 2. Core interpretation of “products/apps/software”

The ecosystem is not being treated as only a collection of GitHub repositories or downloadable source-code bundles. It has several customer-facing renderings.

### 2.1 Developer/package products

These are CLI tools, libraries, schemas, fixtures, and source packages distributed through GitHub, PyPI, Homebrew, or a paid download channel.

The buyer may need to:

- install Python or other dependencies;
- use a terminal;
- configure paths and providers;
- understand reports and manifests;
- maintain the tool in their environment.

Examples:

- WorkVault Control CLI;
- Python Portfolio Forge CLI;
- Archive Atlas CLI;
- Agent Workspace Bridge CLI.

These are valid products, but they are developer editions—not equivalent to a plug-and-play Mac application.

### 2.2 Plug-and-play desktop applications

These are real macOS applications that a customer can install and use through a GUI without understanding the underlying scripts or repository layout.

The expected product experience includes:

- onboarding;
- folder and volume selection;
- permissions explanation;
- visual progress and status;
- preview-before-change;
- approval gates;
- cancellation;
- resume;
- rollback or restore;
- reports and exports;
- privacy controls;
- signed and notarized releases;
- clean-Mac testing.

This is the primary interpretation for a future Setapp product. A CLI inside a ZIP is not a Setapp-ready application.

Strong desktop candidates:

- WorkVault Control.app;
- Archive Atlas.app;
- Creator Asset Intelligence.app;
- Local AI Fleet.app;
- Agent Workspace Bridge.app.

### 2.3 SaaS and hosted products

These are browser-based or API-based services with accounts, workspaces, billing, team access, and recurring infrastructure.

Potential SaaS surfaces include:

- shared archive reports;
- consultant/client workspaces;
- creator product pipelines;
- shared agent configuration governance;
- fleet dashboards across multiple machines;
- revenue and marketplace analytics.

SaaS is not the default implementation for private local archives. It introduces data-upload, retention, authentication, security, billing, and tenant-isolation requirements. A SaaS edition should be created only where collaboration or remote access is a genuine customer need.

### 2.4 Productized services

A customer can also purchase an outcome rather than software:

- Python portfolio audit;
- multi-volume archive comparison;
- creator asset audit;
- local-AI workstation assessment;
- automation offer packaging;
- marketplace-ready product-kit preparation.

These can be sold as consultant packages through direct sales, Fiverr, or a storefront. They are separate from software release claims.

## 3. Product architecture

The recommended architecture is:

```text
AvaTar-ArTs Studio Core
├── local inventory and indexing
├── content hashing and duplicate evidence
├── media metadata extraction
├── workflow runs and checkpoints
├── cancellation and resume
├── preview and approval gates
├── durable changesets
├── rollback and verification
├── path privacy and redaction
├── provider adapters
├── report generation
├── product packaging
└── marketplace/content export adapters
        │
        ├── WorkVault Control
        ├── Archive Atlas
        ├── Python Portfolio Forge
        ├── Creator Asset Intelligence
        ├── Creator Commerce Foundry
        ├── Local AI Fleet
        └── Agent Workspace Bridge
```

The shared engine is an internal technology base. Customers should buy focused products with a single problem and a single primary workflow.

A capability is not identical to a product format. For example, content-based duplicate analysis can render as:

- a CLI report;
- a desktop visual review queue;
- a consultant deliverable;
- a shared SaaS catalog.

The behavior contract should remain stable while the host rendering changes.

## 4. Observed scope

The current metadata-first scope includes:

- `/Users/steven`;
- `/Users/steven/pythons`;
- `/Volumes/bakUp`;
- `/Volumes/2T-Xx`;
- `/Volumes/DeVonDaTa`.

The live system check identified these mounted external APFS volumes:

| Volume | Observed role |
|---|---|
| `/Volumes/bakUp` | historical backups, scripts, Python, iCloud, marketplace roots, media, agent ecosystems |
| `/Volumes/2T-Xx` | active projects, repositories, AI runtime trees, Etsy material, media, reports |
| `/Volumes/DeVonDaTa` | archive collections, MP3/Suno material, PDFs, media caches, Etsy assets |

`/Volumes/newCho` is intentionally excluded because it is a symlink resolving to `/`. Following it would effectively traverse the root filesystem and create duplicate or unsafe evidence.

A volume is evidence for a product family, not a product boundary. No entire volume should be packaged or shipped.

## 5. Evidence boundary

### Observed evidence

The following are observed or previously generated local artifacts:

- a WorkVault Maintenance CLI and tests;
- scanner and content-hash duplicate-analysis code;
- a 19,244-row enriched Python ecosystem scan;
- 5,404 content-hash duplicate groups from an earlier review artifact;
- cross-volume comparison reports;
- media inventory and metadata tooling;
- local AI/Ollama-related tooling;
- agent operation, skills, profiles, and runtime-configuration structures;
- creator, Etsy, SEO, music, and product-bundle scripts;
- three external mounted volumes and a backup volume;
- an installed-app landscape containing competing or adjacent utilities.

### Declared product hypotheses

These are proposed product directions, not proven market outcomes:

- a native WorkVault Control application;
- a native Archive Atlas comparison application;
- a native Creator Asset Intelligence catalog;
- a Local AI Fleet dashboard;
- an Agent Workspace Bridge inspector;
- a Creator Commerce Foundry desktop or SaaS workflow.

### Not established by local evidence

Local inventories do not prove:

- current buyer demand;
- revenue potential;
- Product Hunt ranking;
- Setapp acceptance;
- Gumroad sales;
- customer retention;
- willingness to pay;
- marketplace policy approval;
- third-party licensing rights;
- commercial rights to generated or archived media.

All pricing, demand, launch order, and channel-fit statements remain hypotheses until externally validated.

## 6. Product family catalog

### 6.1 WorkVault Control

Buyer:

- AI-heavy Mac developers;
- consultants;
- solo founders;
- users running long maintenance or package-manager workflows.

Problem:

> A long-running Mac operation can stall, become opaque, leave child processes behind, or make it unclear what happened after interruption.

Primary workflow:

```text
inspect → plan → approve → run → monitor → cancel/resume → report
```

Product forms:

- free/community CLI;
- paid downloadable Pro application;
- native Setapp candidate;
- consultant onboarding and support package;
- future team operations edition.

Differentiator:

- observable operations;
- process-group-aware cancellation;
- durable event history;
- resumable runs;
- approval boundaries;
- evidence-backed reports.

Current state:

- CLI foundation exists;
- package manifest says `public-cli` / `ready-to-prepare`;
- native GUI does not yet exist;
- Setapp-ready status is not established.

Required gates:

- stable release contract;
- timeout and cancellation regression tests;
- signed release artifacts;
- native GUI;
- notarization;
- clean-Mac test matrix;
- privacy and permission review.

### 6.2 Archive Atlas

Buyer:

- power users with multiple drives;
- consultants;
- studios;
- families or teams with live and backup collections.

Problem:

> People need to understand which files exist across multiple volumes before consolidating, restoring, or deleting anything.

Product forms:

- local comparison CLI;
- desktop visual archive map;
- consultant archive-audit service;
- future shared archive-report SaaS.

Core workflow:

```text
select volumes → inventory → compare content identity → review differences → approve exact changeset → apply/restore
```

Differentiator:

- content identity rather than filenames;
- backup-aware comparison;
- missing/found/unlisted evidence;
- explicit restore manifests;
- no destructive default.

Current state:

- prototype;
- prior comparison reports exist;
- cross-volume evidence is mapped;
- complete desktop workflow and restore layer remain to be built.

Required gates:

- synthetic multi-volume fixtures;
- root and symlink policy tests;
- path normalization tests;
- full changeset and rollback contract;
- report privacy controls;
- repeatable comparison outputs.

### 6.3 Python Portfolio Forge

Buyer:

- Python consultants;
- agencies;
- maintainers;
- technical founders;
- teams inheriting script-heavy repositories.

Problem:

> A large Python ecosystem can contain valuable tools, duplicates, stale reports, unknown dependencies, and product candidates that are difficult to evaluate safely.

Product forms:

- bounded CLI;
- desktop review application;
- consultant audit package;
- paid report templates and onboarding kit;
- future client workspace SaaS.

Core workflow:

```text
scan → classify → hash → group duplicates → inspect evidence → rank candidates → export portfolio backlog
```

Evidence:

- 19,244-file enriched scan;
- approximately 12,000 Python files in the reviewed inventory;
- 5,404 content-hash duplicate groups in the earlier review artifact;
- 8,890 extra copies in that artifact;
- existing scanner, CSV, JSON, and report workflows.

Important limitation:

Duplicate hashes prove byte equality, not which copy should be kept. Business, maturity, ROI, and product scores are heuristic signals unless independently validated.

Current state:

- private beta concept;
- strongest unique case-study material;
- bounded standalone CLI still required;
- private source and raw inventory must not ship.

### 6.4 Creator Asset Intelligence

Buyer:

- independent creators;
- video editors;
- musicians;
- small media teams;
- agencies with mixed media archives.

Problem:

> Creative archives contain audio, video, images, transcripts, metadata, exports, and duplicates without one trustworthy review surface.

Product forms:

- local media inventory CLI;
- native visual catalog application;
- Gumroad/direct-download beta;
- consultant archive-audit service;
- future team catalog.

Core workflow:

```text
select archive → extract metadata → hash → create contact sheets → review duplicates → approve recovery actions → export catalog
```

Potential metadata:

- duration;
- dimensions;
- codecs;
- file size;
- timestamps;
- full content hash;
- transcript linkage;
- license/provenance fields.

Current state:

- prototype;
- media inventory and scanner evidence exist;
- stable ffprobe/MediaInfo adapter and polished GUI remain required.

### 6.5 Creator Commerce Foundry

Buyer:

- digital-product creators;
- Etsy sellers;
- visual brands;
- independent musicians;
- automation consultants.

Problem:

> Scattered assets and metadata must be turned into consistent, reviewable product kits without accidentally publishing, misrepresenting rights, or making unsupported SEO claims.

Product forms:

- export-only desktop generator;
- Gumroad/Lemon Squeezy template and workflow package;
- productized consulting service;
- future SaaS batch pipeline.

Core workflow:

```text
select assets → verify provenance → build bundle → draft listing metadata → review → export launch kit
```

Hard boundaries:

- no automatic marketplace publishing;
- no credential storage in exports;
- no use of uncleared assets;
- no guarantees of sales, rankings, or conversion;
- every external submission remains manual approval.

Current state:

- private beta concept;
- scripts and asset evidence exist;
- licensing, provenance, and reproducible bundle validation remain required.

### 6.6 Local AI Fleet

Buyer:

- Ollama users;
- local-model developers;
- AI consultants;
- users managing several local runtimes or older Macs.

Problem:

> Local models, endpoints, runtimes, disk usage, and compatibility signals are difficult to inventory and manage across machines.

Product forms:

- local CLI;
- native model dashboard;
- consultant support bundle;
- future multi-machine team SaaS.

Core workflow:

```text
inspect runtime → inventory models → check health → assess disk/compatibility → recommend → approve downloads/removals
```

Current state:

- prototype;
- Ollama-related workflow evidence exists;
- model metadata schema, health fixtures, cancellation tests, and Apple Silicon/Intel matrix remain required.

### 6.7 Agent Workspace Bridge

Buyer:

- multi-agent developers;
- small AI teams;
- consultants using Claude, Codex, Cursor, Gemini, Qwen, iTerm2, Kitty, Ghostty, or related tools.

Problem:

> Multiple agent environments can drift in skills, agents, hooks, profiles, prompts, and runtime configuration, making parity difficult to understand.

Product forms:

- local drift scanner;
- native workspace inspector;
- Product Hunt demonstration;
- Gumroad starter kit;
- future team governance service.

Core workflow:

```text
inventory runtimes → compare capabilities → redact sensitive fields → show drift → propose translation → approve changes
```

Hard boundaries:

- no silent synchronization;
- no uploading private prompts or credentials;
- no claimed behavioral parity without tests;
- no overwriting canonical configuration by default.

Current state:

- prototype;
- capability-atlas translation contract exists;
- sanitized fixtures and parity tests remain required.

## 7. Installed application landscape

The installed applications provide competitive and integration context, not proof of customer demand.

### Existing adjacent categories

- storage and cleanup: CleanMyMac, App Cleaner, DaisyDisk, MacBooster, OnyX, Maintenance;
- file and archive tools: Path Finder, Tidy Up, dupeGuru, DEVONthink, File Cabinet Pro, File Juicer;
- media tools: AudioRanger, ImageRanger, XnViewMP, Yate, MusicBrainz Picard, IINA, VLC, LosslessCut;
- AI tools: Ollama, OllaMan, ChatGPT, Claude, Cursor, Perplexity, MiniMax Design;
- agent and terminal tools: iTerm, iTermAI, Warp, Ghostty, Kitty, Hyper, Claude Terminal, Zed, Windsurf, Visual Studio Code;
- automation and launchers: Alfred, Raycast, Keyboard Maestro, LaunchBar, BetterTouchTool;
- creative and publishing tools: Canva, CapCut, Descript, Adobe-related tools, Notion, Airtable, Screenium, Movavi;
- archive and transfer tools: BetterZip, Keka, SiteSucker Pro, Transmission, LocalSend.

### Strategic implication

The products should operate across gaps between existing apps rather than becoming generic replacements:

- WorkVault does not need to be another cleaner;
- Archive Atlas does not need to be another file browser;
- Local AI Fleet does not need to be another model runner;
- Creator Asset Intelligence does not need to be another image viewer;
- Agent Workspace Bridge does not need to be another chat client.

Their value is orchestration, evidence, comparison, recovery, and review across tools that already exist.

## 8. Distribution model

### GitHub

Best for:

- transparent open-source cores;
- schemas;
- fixtures;
- safety code;
- reproducible CLI releases.

Required:

- tests and CI;
- license review;
- sanitized examples;
- documented privacy model;
- no private volume contents.

### PyPI and Homebrew

Best for stable CLI editions. Do not publish until command contracts, supported versions, failure modes, upgrades, and dependencies are tested.

### Gumroad or Lemon Squeezy

Best for:

- paid CLI editions;
- report templates;
- workflow kits;
- onboarding;
- support packages;
- productized services;
- export-only product builders.

Required:

- install guide;
- license terms;
- support policy;
- update policy;
- sample output;
- refund/contact process;
- signed or hash-pinned release artifact;
- no credentials or raw private inventories.

### Product Hunt

Use one product per campaign:

```text
one product
one buyer
one painful problem
one demo
one primary call to action
```

Strong candidate stories:

- “Stop a stuck Mac operation without losing the run.”
- “Compare every copy across three drives before consolidating.”
- “Turn a 19,000-file Python ecosystem into a reviewable portfolio.”
- “See drift across your AI workspaces before overwriting configuration.”

Local evidence may support the maker story and demo. It cannot establish current demand, ranking, revenue, or customer outcomes.

### Setapp

Setapp should be treated as a native-app channel, not a CLI channel.

Before a product can be called Setapp-ready, it needs:

- a real macOS GUI;
- signed application artifact;
- notarization;
- clean-machine testing;
- permission and privacy review;
- onboarding;
- reliable update behavior;
- documented support boundary;
- manual submission and approval.

Current candidates:

1. WorkVault Control;
2. Archive Atlas;
3. Creator Asset Intelligence;
4. Local AI Fleet;
5. Agent Workspace Bridge.

No candidate is currently represented as accepted or sold on Setapp.

## 9. Release-state vocabulary

| State | Meaning |
|---|---|
| `prototype` | Internal capability; not a finished product |
| `private-beta` | Bounded external evaluation with support and feedback |
| `packageable` | An allow-listed artifact can be built and inspected |
| `public-cli` | Reproducible CLI release with documented behavior |
| `launch-candidate` | Demo and release evidence assembled; response unverified |
| `native-candidate` | Enough evidence to justify building a native app |
| `submitted` | Manually submitted to a channel with a verifiable reference |
| `sold` | Real storefront/listing and verified transaction evidence |
| `setapp-ready` | Signed, notarized, tested, and ready to submit; not accepted or sold |

The word “sold” must never be inferred from a manifest, ZIP file, local catalog, or pricing hypothesis.

## 10. Current repository artifacts

Canonical workspace:

```text
/Users/steven/iterm2/new-products/
```

Relevant artifacts:

- `packages/package-index.json`
  - seven package manifests;
  - observed mounted-volume scope;
  - shared-engine definition;
  - explicit packageable-versus-sold rule.

- `packages/*/product.json`
  - WorkVault Control;
  - Python Portfolio Forge;
  - Creator Asset Intelligence;
  - Archive Atlas;
  - Creator Commerce Foundry;
  - Local AI Fleet;
  - Agent Workspace Bridge.

- `catalog/volume-product-map.json`
  - maps observed roots to product families;
  - records the `/Volumes/newCho` symlink exclusion.

- `marketplace/ALL-VOLUMES-PRODUCT-PORTFOLIO-2026-09-04.md`
  - broad portfolio map and channel strategy.

- `marketplace/PRODUCT-LINE-2026-09-04.md`
  - product-line boundaries and recommended order.

- `marketplace/CHANNEL-PACKAGING-MATRIX-2026-09-04.md`
  - buyer, artifact, channel, state, and missing proof for each product.

- `packaging/build_release.py`
  - allow-list release builder;
  - packages only selected manifests and explicitly approved files;
  - blocks secret-like filenames and sensitive key suffixes;
  - does not recursively package home directories or volumes.

- `packaging/README.md`
  - release-builder usage and Setapp boundary.

## 11. Packaging verification already completed

The package index was reconciled against all seven product manifests.

Validated package IDs:

```text
agent-workspace-bridge
archive-atlas
creator-asset-intelligence
creator-commerce-foundry
local-ai-fleet
python-portfolio-forge
workvault-control
```

Review ZIP artifacts were built outside the repository in `/tmp/avatararts-package-check/` and passed ZIP integrity checks. They contain metadata and explicitly approved files only.

The product workspace tests passed:

```text
3 passed
```

JSON validation and `git diff --check` passed.

These checks prove packaging mechanics and document consistency. They do not prove customer readiness or marketplace acceptance.

## 12. Safety and privacy requirements

### Never package

- credentials;
- `.env` files;
- private keys;
- tokens;
- raw private prompts;
- full home-directory inventories;
- unreviewed volume contents;
- customer data;
- uncleared third-party media.

### Scanner requirements

- reject symlink roots by default;
- follow roots only with explicit opt-in;
- skip or record symlinked files according to policy;
- preserve original inventories unchanged;
- use full content hashing for duplicate identity;
- keep filename similarity diagnostic only;
- use relative or redacted report paths by default;
- make absolute paths explicit for private reports;
- bound hashing, line counting, and media inspection;
- preserve schema versions.

### Mutation requirements

No file should be moved or deleted without:

1. a durable changeset;
2. exact source and destination;
3. source SHA-256;
4. device and inode identity;
5. symlink check;
6. destination no-clobber check;
7. operation status;
8. rollback metadata;
9. verification after the mutation;
10. a human approval step.

### Marketplace and publishing requirements

External publishing, customer contact, credential use, marketplace automation, and submission require explicit human approval.

## 13. Recommended implementation sequence

### Phase 1: finish the shared safety engine

- migrate remaining legacy cleanup operations to the durable changeset model;
- remove path-based deletion races where possible;
- add subprocess tests for public CLI behavior;
- add timeout, stale-lock, and process identity tests;
- complete rollback verification;
- separate observed metadata from heuristic scores.

### Phase 2: build the first real desktop app

Recommended first native app: WorkVault Control.

Minimum usable GUI:

- provider selection;
- read-only plan;
- run ID;
- event timeline;
- live status;
- cancel;
- resume;
- report export;
- privacy and permission explanation.

Do not begin with a feature-heavy control room. Prove one reliable daily loop first.

### Phase 3: build Archive Atlas as the cross-volume differentiator

Use synthetic fixtures first. Then support user-selected roots with explicit policies.

Minimum usable GUI:

- volume picker;
- scan progress;
- content-identity groups;
- found/missing/unlisted views;
- relative/redacted reports;
- exact review queue;
- restore manifest.

### Phase 4: extract Python Portfolio Forge

- create a bounded standalone CLI;
- define a stable inventory schema;
- provide sanitized fixtures;
- add license/provenance checks;
- create a redacted case study;
- validate with a small number of external users.

### Phase 5: build creator and commerce surfaces

- media catalog first;
- product-kit export second;
- marketplace publishing remains manual;
- rights and provenance fields are mandatory;
- do not make SEO or sales claims without evidence.

### Phase 6: choose one Setapp candidate

Select based on:

- repeat local usage;
- retention or recurring use;
- low support burden;
- clear privacy story;
- stable GUI workflow;
- real user feedback.

Do not choose solely because a product has the largest feature list or the most local source files.

## 14. Current recommendation

The flagship ecosystem concept is:

> AvaTar-ArTs Studio Core: evidence-backed automation for messy creative and AI workspaces.

The first customer-facing desktop product should be:

> WorkVault Control.app — a local-first Mac operations application that lets users inspect, approve, run, monitor, stop, resume, and report on long-running maintenance and AI-workstation workflows.

The best second product is:

> Archive Atlas.app — a visual, content-based comparison tool for live and backup volumes with reviewable recovery manifests.

The best proof-led developer product is:

> Python Portfolio Forge — a bounded tool that maps a large Python ecosystem into evidence-backed duplicate groups, risks, reusable components, and a product backlog without deleting source code.

## 15. Explicit status statement

As of this handoff:

- the ecosystem has package manifests and release-planning artifacts;
- seven bounded product families are documented;
- review ZIPs can be built from allow-listed files;
- no product is proven sold;
- no product is accepted by Setapp;
- no Product Hunt launch has been completed by this handoff;
- no Gumroad/Lemon Squeezy transaction is established;
- no SaaS service is deployed;
- native `.app` products remain implementation work;
- current marketplace prices remain hypotheses;
- all-volume evidence remains local and privacy-bounded.

The next engineering objective is not to create more catalog entries. It is to turn WorkVault Control into one genuinely usable, signed desktop application while preserving the CLI and shared safety engine underneath.
