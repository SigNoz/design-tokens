---
'@signozhq/design-tokens': minor
---

Correct the dropdown colours against the Figma spec and rename two token groups.

The row icon now tracks the label at `--l2-foreground` instead of sitting a step dimmer at `--l3-foreground`, and gains a `--dropdown-item-icon-hover` companion so the glyph follows the label to the hover foreground. The danger row's label moves from `--destructive` to `--danger-background-hover`, which is the shade the design actually uses, and its hover fill now aliases the existing `--callout-error-background` rather than deriving the same colour a second time. The search row gains `--dropdown-search-icon` so the glyph and the placeholder are addressable apart, and the spinner row gains `--dropdown-loading-label` at `--l1-foreground`, which is a step brighter than the rows it replaces.

`--dropdown-item-indicator` is removed. The selection check sits inside a slot, so it is an icon and takes `--dropdown-item-icon` through every state the slot already answers for; a second token for it only let the two drift apart.

`--dropdown-focus-ring` is renamed `--dropdown-item-focus-ring`, since the ring is only ever drawn on a row, and it now reads `--primary-background` rather than the legacy `--primary` alias.

The calendar's month and year selects move from `--calendar-dropdown-*` to `--calendar-select-*`, so the `dropdown-` prefix names one component.
