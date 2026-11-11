---
'@signozhq/design-tokens': minor
---

Remove the legacy `--card` and `--card-foreground` tokens, with `Style.CARD`,
`Style.CARD_FOREGROUND` and the `card` and `card-foreground` keys of `StyleTailwind`. Replace them
with the current semantic tokens:

- `var(--card)` with `var(--surface-2)`, or `var(--card-background)` on a card. Dark is unchanged
  (`#121317`); light moves from `#ffffff` to `#fcfcfd`.
- `var(--card-foreground)` with `var(--l1-foreground)`.
