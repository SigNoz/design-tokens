---
'@signozhq/design-tokens': minor
---

Retune dark-mode borders, control fills and hover states so they stay visible on every surface, including the translucent `surface-3` of popovers, menus, selects and tooltips. Only dark values change; names and the light theme are untouched.

- `l1-border`, `l2-border` and `l3-border` are now translucent white steps (4.5%, 9.3% and 13%), so one border reads the same on the page, a card or a popover.
- `secondary-background` and `secondary-background-hover` are translucent (4% and 7%), so secondary buttons, callouts and radio cards no longer match `surface-3` inside a floating layer.
- Fields get a 3.5% fill: `input-background`, and `select-trigger-background`, `combobox-trigger-background` and `toggle-group-secondary-outlined-background` now point at it.
- Menu row hovers (`dropdown-`, `select-`, `combobox-` and `command-item-background-hover`) use a 7% step, so a hovered row sits above the menu instead of matching it. The same step applies to `pill-outlined-background-hover` and `tabs-primary-background-hover`.
- `badge-secondary-background` uses the 9.3% step instead of `surface-3`, so a secondary badge stays visible inside a popover.
- `tabs-secondary-background` and its hover follow the secondary fills; on the page, the old hover was almost the same colour as the resting state.
- `switch-track-background` and its hover are 20% and 28% white.
- `input-foreground` is `l1-foreground` and `input-placeholder` is `l3-foreground`, matching Select and Combobox.
- `calendar-select-border` uses `l2-border` instead of the legacy `input` colour.
