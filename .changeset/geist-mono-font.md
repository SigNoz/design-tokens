---
'@signozhq/design-tokens': minor
---

The code text styles now use `Geist Mono` instead of `SF Mono`, and the package ships it as an
opt-in stylesheet, `dist/fonts/geist-mono.css`, next to `inter.css`.

```css
@import '@signozhq/design-tokens/dist/fonts/geist-mono.css';
```

SF Mono cannot be shipped (Apple's license does not allow redistribution), so the code styles
rendered a different mono font on macOS, Windows and Linux. The `code-*` font family stack is now
`'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace`.

The stylesheet declares two upright faces of `Geist Mono` 1.9.2, `latin` (37 KB) and `rest`
(41 KB), each a variable weight face from 100 to 900 with `font-display: swap`. The `rest` file
loads only for text outside the `latin` unicode range. There is no italic face.

Geist Mono has no ⌃ ⌘ ⌥ ⎋, so a third `Geist Mono` face draws those four key symbols from
`InterVariable-keys.woff2` (3 KB), an Inter subset. Without it a shortcut such as ⌘ ⇧ P drew ⌘ in
the platform fallback font and ⇧ in Geist Mono.
`dist/fonts/LICENSE-GeistMono.txt` is the SIL Open Font License 1.1 text of Geist. The files are
regenerated with `uv run scripts/subset-geist-mono.py`.
