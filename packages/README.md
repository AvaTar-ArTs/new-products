# AvaTar-ArTs Product Packages

This directory is the release boundary between internal capabilities and
buyer-facing products. A package is not a dump of the whole workspace: it has
a named buyer, a bounded promise, a source map, proof, a distribution route,
and an explicit release state.

## Initial package family

| Package | Buyer | First channel | Edition path |
|---|---|---|---|
| WorkVault Control | AI-heavy Mac developers and consultants | GitHub/Homebrew + direct download | Setapp-ready native control room |
| Python Portfolio Forge | Python consultants, agencies, and maintainers | PyPI/GitHub/Gumroad | Setapp companion app later |
| Creator Asset Intelligence | creators and small media teams | direct download/Gumroad | Setapp native media catalog later |

CLI packages can ship independently. A Setapp submission is a signed,
notarized macOS app with a GUI, permission review, and documented privacy
model; these manifests do not pretend a CLI is already a Setapp app.

## Release states

- `prototype`: useful internal capability; not sold yet
- `private-beta`: bounded external test with support and feedback loop
- `public-cli`: reproducible CLI release
- `native-candidate`: enough evidence to build a macOS app wrapper
- `setapp-ready`: signed, notarized, reviewed, and submitted

## Package contract

Every manifest identifies the buyer/job, inputs/outputs/non-goals, source
capabilities and licenses, proof assets, distribution/pricing hypothesis,
privacy and recovery behavior, and validation gates before sales claims.

