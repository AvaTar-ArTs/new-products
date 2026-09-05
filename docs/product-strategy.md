# Product Strategy

`new-products` is the commercialization layer above the AvaTar-ArTs project
ecosystem. Source repositories remain responsible for their own code. This
repository answers what can be packaged, who buys it, how it is distributed,
what proof exists, and what remains before launch.

The operating loop is:

```text
inventory → score → select launch cohort → productize → distribute → measure → revise
```

The shared technical foundation is `workvault-core`: durable runs, structured
events, provider adapters, policies, reports, and renderers. Products should
reuse it rather than fork their own update, cleanup, logging, and cancellation
systems.

The first launch cohort is `DevAI Cleanroom` and `WorkVault Control`. They share
the same buyer, local-first privacy position, and strongest evidence from the
existing Mac workstation.
