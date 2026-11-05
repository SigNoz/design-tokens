---
'@signozhq/design-tokens': minor
---

Add an opt-in stylesheet that loads Inter, `dist/fonts/inter.css`, with the font files next to it.

```css
@import '@signozhq/design-tokens/dist/fonts/inter.css';
```

The text styles name `Inter` as their font family but the package did not ship the font, so each
app loaded its own build and the digits and features differed between them. The stylesheet declares
two upright faces of `Inter` (Inter 4.1), `latin` and `rest` (Cyrillic, Greek, Vietnamese and the
rest), each a variable weight face from 100 to 900 with `font-display: swap`. A browser downloads
the `rest` file only for text outside the `latin` unicode range, and nothing loads unless the
stylesheet is imported. The files keep the OpenType features that Google Fonts drops (`ss01`,
`zero`, `case`, `tnum`) and have the optical size axis pinned at 14, so every size renders the
same as the Figma text styles.

There is no italic face. `dist/fonts/LICENSE.txt` is the SIL Open Font License 1.1 text of Inter.
The files are regenerated with `uv run scripts/subset-inter.py`.

The package now declares `"license": "MIT AND OFL-1.1"` in `package.json`: MIT for the package, the
SIL Open Font License 1.1 for the files in `dist/fonts/`.
