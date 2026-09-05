# AvaTar-ArTs Channel Packaging Matrix

Observed: 2026-09-05 UTC

This matrix describes packaging readiness, not marketplace publication. “Packageable” means a bounded local artifact can be built from an allow-list. It does not mean the product is listed, submitted, approved, or sold.

## Product channel matrix

| Product | Buyer/job | First artifact | Best first channel | Current state | Not yet proven |
|---|---|---|---|---|---|
| WorkVault Control | AI-heavy Mac developers who need visible, recoverable maintenance runs | CLI source/release ZIP | GitHub + Homebrew preparation | public-cli / ready-to-prepare | signed release, stable cancellation/timeout evidence, native Setapp app |
| Python Portfolio Forge | Python consultants and teams with script sprawl | bounded CLI plus redacted sample report | GitHub/PyPI preparation, then Gumroad templates | private-beta | reusable standalone CLI, license audit, buyer validation |
| Archive Atlas | power users and consultants comparing live and backup volumes | local comparison CLI plus report template | Gumroad or productized service | prototype | cross-volume fixtures, complete restore manifest, repeat-user evidence |
| Creator Asset Intelligence | creators and small media teams cataloging archives | media inventory CLI plus duplicate review report | direct download/Gumroad beta | prototype | stable media adapters, sample fixtures, quarantine workflow |
| Creator Commerce Foundry | digital-product creators preparing launch kits | export-only product-kit generator | Gumroad/Lemon Squeezy | private-beta | asset rights, reproducible bundles, marketplace policy review |
| Local AI Fleet | Ollama/local-model users managing models and endpoints | local inventory and health-check CLI | GitHub/Gumroad workflow pack | prototype | Intel/Apple Silicon matrix, cancellation tests, model lifecycle fixtures |
| Agent Workspace Bridge | multi-agent developers comparing local runtimes | drift report and capability matrix | GitHub/Product Hunt candidate | prototype | sanitized runtime fixtures, parity tests, canonical registry |

## Channel rules

### GitHub

Suitable for open-source CLI cores, fixtures, schemas, and transparent safety code.

Required before claiming a public release:

- reproducible build;
- tests and CI;
- license and provenance review;
- sanitized examples;
- documented privacy and non-goals;
- no private volume contents in the repository.

### PyPI and Homebrew

Suitable for stable CLI editions only. A package should not be published until its command contract, supported Python/macOS versions, failure behavior, and upgrade path are tested.

### Gumroad or Lemon Squeezy

Suitable for bounded paid bundles:

- signed or hash-pinned release artifact;
- install guide;
- license terms;
- support boundary;
- update policy;
- sample output;
- refund/contact process;
- no credentials or raw personal inventories.

### Product Hunt

Use one product, one buyer, one pain, one demo, and one feedback request per launch. Current local evidence can support a demo story; it cannot establish demand, revenue, ranking, or customer outcomes.

### Setapp

Setapp is a future native-app channel for these products, not a CLI channel. Each submission requires a real macOS GUI, signed and notarized artifact, clean-machine testing, permission review, privacy disclosures, onboarding, and Setapp approval. Current states remain `native-candidate` or `future` until those gates are met.

## Sale-state vocabulary

- `prototype`: internal capability; do not sell as a finished product.
- `private-beta`: bounded external evaluation with support and feedback.
- `packageable`: an allow-listed artifact can be built and inspected.
- `public-cli`: reproducible CLI release with documented behavior.
- `launch-candidate`: demo and release evidence are assembled; market response is unverified.
- `submitted`: manually submitted to a channel; requires a verifiable submission reference.
- `sold`: requires a real storefront/listing and verified transaction evidence.
- `setapp-ready`: signed, notarized, tested, and ready for Setapp submission; not equivalent to accepted or sold.

## Recommended order

1. WorkVault Control: finish release gates and keep the CLI as the trust layer.
2. Archive Atlas: build the cross-volume demo using synthetic fixtures and explicit restore manifests.
3. Python Portfolio Forge: extract a bounded scanner and use the 19,244-row inventory only as a redacted case-study input.
4. Creator Commerce Foundry: ship export-only kits after rights and provenance review.
5. Choose one native Setapp candidate only after repeat local usage and retention evidence.

## Explicit holds

No package in this matrix is represented as currently sold on Setapp, Product Hunt, Gumroad, PyPI, Homebrew, or another marketplace. Actual listing, submission, payment, buyer contact, and publication remain manual approval actions.
