---
'@signozhq/design-tokens': minor
---

Add a `drawer-*` set for the reworked Drawer, in both themes. `drawer-background` is the panel
fill (`surface-2`), `drawer-border` its hairline and the lines under its header and over its footer
(`l2-border`), and `drawer-shadow` the lift (`shadow-drawer`). `drawer-backdrop` is the scrim
behind a task drawer, black at 40% in both themes, the value the Dialog backdrop hard-codes today.

The dark `shadow-drawer` is repointed to the Figma `dark/shadow-drawer` effect, a shadow cast to the
left of the panel. It was the light value's vertical shape with heavier alphas, which no
component read. The light value is unchanged.
