---
'@signozhq/design-tokens': major
---

Remove the typography primitives and the theme font families. The 33 text styles are the only
typography tokens left.

Breaking: every text takes its font from one style, so a component sets
`var(--label-base-500-font-size)` and the other five properties of the same style (font family,
weight, line height, letter spacing and text transform). Removed:

- the Periscope primitives: `--periscope-font-size-*`, `--periscope-font-weight-*`,
  `--periscope-line-height-*` and `--periscope-font-family-*`;
- the older scale: `--font-family-inter`, `--font-family-sf-mono`, `--font-size-xs` to
  `--font-size-9xl`, `--font-weight-thin` to `--font-weight-black`, `--line-height-*` and
  `--letter-spacing-*`;
- the same keys in `Typography`, in `typographyTokens`, and the matching `--text-*` variables of
  `tailwind-theme.css`;
- the theme font families `--font-sans`, `--font-serif` and `--font-mono` (`Style.FONT_SANS`,
  `FONT_SERIF`, `FONT_MONO` and the `font-*` keys of `StyleTailwind`). Read the family from a text
  style, `--paragraph-base-400-font-family` for text and `--code-base-400-font-family` for code.
