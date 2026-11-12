---
'@signozhq/design-tokens': minor
---

Remove `select-trigger-label-disabled` and `combobox-trigger-label-disabled`, with
`Style.SELECT_TRIGGER_LABEL_DISABLED`, `Style.COMBOBOX_TRIGGER_LABEL_DISABLED` and their
`StyleTailwind` keys. A disabled Select or Combobox trigger now fades as a whole, like a disabled
Input, and keeps its normal label colour. Use `var(--select-trigger-label)` or
`var(--combobox-trigger-label)` if you referenced them.
