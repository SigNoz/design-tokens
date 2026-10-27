---
'@signozhq/design-tokens': minor
---

Align the 33 text styles with the Periscope type tokens page, and add a `typography-*` set for the
reworked Typography, in both themes.

The text styles change in four places:

- Letter spacing is a percent of the font size, as in Figma: `-0.5px` is now `-0.005em` (label base
  and paragraph base) and `4px` is now `0.04em` (uppercase). At 11px, uppercase text was about 9
  times wider than Figma. Paragraph small is now `0`.
- The font families have fallback stacks: Inter falls back to the system UI font, SF Mono to
  `ui-monospace`, Menlo, Consolas and Liberation Mono, and Lora to Georgia.
- `paragraph-medium-500` and `paragraph-medium-600` have a 26px line height, the same as
  `paragraph-medium-400`. They had 24px.
- Every style has a `text-transform`: `uppercase` on the six uppercase styles, `none` on the rest.
  The CSS classes and `TypographyStyles` carry it as well.

The new tokens are the text colors of Typography. `typography-main`, `typography-secondary` and
`typography-tertiary` follow the `l1` to `l3` foregrounds. The seven hues (`primary`, `success`,
`danger`, `warning`, `info`, `archive`, `highlight-danger`) take the label color of an outlined
badge of the same color, and `typography-link` the primary link color.
