---
'@signozhq/design-tokens': patch
---

Mark the shipped `Inter` subsets as unhinted by adding the `gasp` and `prep` tables Google Fonts gives its unhinted fonts. Without them FreeType autohints the files on Linux, in headless Chromium and in Chromatic, which shrinks the word spaces and the width of small labels. Glyphs, layout features and names are unchanged.
