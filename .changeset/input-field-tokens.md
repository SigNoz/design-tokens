---
'@signozhq/design-tokens': minor
---

Add an `input-*` set for the reworked Input: `input-background` (transparent, so the field sits on any surface), `input-border` / `input-border-hover` on `l2-border` / `l3-border`, `input-foreground`, `input-placeholder` / `input-placeholder-hover` and `input-icon` on the `l1`/`l2` foregrounds, `input-focus-ring` on `primary-background`, and per status (`success`, `warning`, `danger`) a tinted `input-{status}-background` / `input-{status}-border` (the callout `color-mix` recipe over forest/amber/cherry 500) and an `input-{status}-icon` aliasing the semantic background. Also a `field-*` set for the new Field wrapper: `field-label` / `field-label-hover` / `field-label-icon` on the `l1`/`l2` foregrounds, `field-required-marker` on `danger-background`, and per status a `field-{status}-label` / `field-{status}-message` text color (the callout description shade per mode) and `field-{status}-icon`.
