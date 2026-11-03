---
'@signozhq/design-tokens': patch
---

Add the `popover-background`, `popover-border` and `popover-shadow` entries to `Style` and
`StyleTailwind`. 2.4.0 shipped the CSS variables without regenerating the type files, so they had
no `Style.POPOVER_*` constant or Tailwind key.
