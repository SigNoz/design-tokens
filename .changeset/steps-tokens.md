---
'@signozhq/design-tokens': minor
---

Add a `steps-*` set for the Steps component, in both themes. `steps-marker-{waiting,current,done}-*`
colour the marker of each status, `steps-label-*-foreground` its label, `steps-description-foreground`
the text under it, `steps-connector` and `steps-connector-done` the line between steps, and
`steps-text-focus-ring` the focus ring of a truncated text. `steps-list-*` colour the vertical list:
its markers, connector, label, content and the dot before the footer. They alias the existing layer
and primary tokens, so nothing changes on screen. `Style` and `StyleTailwind` get the matching keys.
