# AvaTar-ArTs Product Line — Packaging and Sales Boundary

## Product thesis

Creators and developers do not need another generic cleanup script. They need
local tools that explain a messy workspace, show evidence, preserve recovery,
and turn useful work into repeatable deliverables. The portfolio is a family
of focused products built on one local-first engine.

## What can be sold

### WorkVault Control

Sell the CLI as an open-source trust-building product. Sell Pro as an
onboarding bundle and later as a signed macOS control room. The demo shows a
plan, run ID, event log, cancellation, and resume behavior in one session.

### Python Portfolio Forge

Sell to people with script sprawl, inherited repositories, or client codebases.
The paid outcome is a redacted portfolio report with evidence, risk tiers,
reusable components, and a product backlog—not merely a duplicate list.

### Creator Asset Intelligence

Sell to media-heavy users who need to understand an archive before changing it.
The paid wedge is visual review plus a recovery manifest, not a faster `find`.

## Channel fit

| Channel | Best package | Required work |
|---|---|---|
| GitHub | WorkVault CLI, Portfolio Forge community | public docs, tests, license, sample data |
| PyPI/Homebrew | focused CLI editions | stable command contract, CI, release automation |
| Gumroad/Lemon Squeezy | Pro bundles and consultant kits | license delivery, onboarding, support, update policy |
| Setapp | native WorkVault/Creator apps | GUI, signed/notarized app, privacy/permission review, polished onboarding |
| Product Hunt | one focused launch at a time | demo video, landing page, maker story, feedback loop |

## Keep separate

- Do not market social automation as part of the core product; it creates
  platform-policy and credential risk.
- Do not ship the whole Python directory as a toolkit; it weakens trust,
  increases support cost, and creates license ambiguity.
- Do not call a CLI Setapp-ready. Use `native-candidate` until the app exists,
  is signed, notarized, and tested on a clean Mac.

## Recommended order

1. Release WorkVault Control 0.1.0 as the trust and orchestration layer.
2. Extract Python Portfolio Forge into a bounded CLI using sanitized fixtures.
3. Build Creator Asset Intelligence on the same report, hashing, and approval
   contracts.
4. Build one native macOS shell after a CLI has repeat users and retention
   evidence.

Every listing should include a 60-second demo, example report, privacy model,
restore story, changelog, support boundary, and one inspect-before-purchase
command.
