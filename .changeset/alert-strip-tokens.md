---
'@signozhq/design-tokens': minor
---

Add the `alert-strip-*` set for Alert Strip, in both themes and on primitive colours only. Each colour of the Badge union gets a fill (`alert-strip-{color}-background`), a text colour (`alert-strip-{color}-foreground`) and a link hover step (`alert-strip-{color}-link-hover`), with the same values the solid badge of that colour resolves to today, except the light secondary fill, which is `bg-neutral-light-700` so the strip stands apart from the page background. The action and close buttons share `alert-strip-button-background` (now described), `alert-strip-button-background-hover` and `alert-strip-button-foreground` on every colour, and `alert-strip-decoration` paints the dots on the tapered ends.
