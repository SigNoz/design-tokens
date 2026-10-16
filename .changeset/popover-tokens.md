---
'@signozhq/design-tokens': minor
---

Add a `popover-*` set for the reworked Popover, in both themes. `popover-background` is the
translucent shell (`surface-3`), `popover-border` its hairline (`l2-border`) and `popover-shadow`
the lift (`shadow-dropdown`), which is the dropdown shadow rather than the tooltip one. `popover`
itself is untouched, since `calendar-select-background` reads it.

`popover-foreground` is repointed to `l1-foreground`, so it follows the level scale like every
other foreground instead of naming a primitive. That moves it one step for anything already using
it: `#121317` to `#1e1f24` in light, and pure white to `#eceef2` in dark.
