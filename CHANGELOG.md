# @signoz/design-tokens

## 2.2.0

### Minor Changes

- 784fc7f: Add semantic tokens for badges and pills. Badges get a background, border, label and icon for each of the five outlined intents. Pills get a background, border, label and hover label for the primary, secondary, success, warning, danger, info, archive and highlight danger variants, plus the outlined and rect solid treatments with their dismiss icon. Also adds the `radius_1_5` step at 3px.
- 784fc7f: Add semantic tokens for the button group: the fill, label, border and disabled hatch of an outlined secondary member in its default and hover states, and the focus ring around a member.
- 784fc7f: Add semantic tokens for the calendar: the grid's fill, a month arrow and a date cell in their default, hover, pressed and focused states, a selected day and both ends and the middle of a range with their hover fills, today's cell, days outside the month and days that cannot be picked, the weekday and week-number labels, and the caption dropdowns' fill, border, marker and shadows.
- 784fc7f: Add semantic tokens for the colours the button, badge, tooltip, breadcrumb, tabs, pill and dropdown still read from shared tokens or the raw palette, and a focus ring token for the button, breadcrumb, tabs, pill, checkbox, switch, toggle group and radio group.
- 784fc7f: Correct the dropdown colours against the Figma spec and rename two token groups.

  The row icon now tracks the label at `--l2-foreground` instead of sitting a step dimmer at `--l3-foreground`, and gains a `--dropdown-item-icon-hover` companion so the glyph follows the label to the hover foreground. The danger row's label moves from `--destructive` to `--danger-background-hover`, which is the shade the design actually uses, and its hover fill now aliases the existing `--callout-error-background` rather than deriving the same colour a second time. The search row gains `--dropdown-search-icon` so the glyph and the placeholder are addressable apart, and the spinner row gains `--dropdown-loading-label` at `--l1-foreground`, which is a step brighter than the rows it replaces.

  `--dropdown-item-indicator` is removed. The selection check sits inside a slot, so it is an icon and takes `--dropdown-item-icon` through every state the slot already answers for; a second token for it only let the two drift apart.

  `--dropdown-focus-ring` is renamed `--dropdown-item-focus-ring`, since the ring is only ever drawn on a row, and it now reads `--primary-background` rather than the legacy `--primary` alias.

  The calendar's month and year selects move from `--calendar-dropdown-*` to `--calendar-select-*`, so the `dropdown-` prefix names one component.

- 784fc7f: Add semantic tokens for the dropdown: the popup's fill, border and shadow, the row label in its default, hover and disabled states, the row fill and its hover, the destructive row's label and fill, the row icon and selection indicator, the group label, the separator, the search row's placeholder and rule, the focus ring and the scroll fade.
- 784fc7f: Add link tokens with a resting and hover value for each intent: `primary-link`, `secondary-link`, `success-link`, `warning-link` and `danger-link`.
- 784fc7f: Add semantic tokens for the radio group: a shared border and label pair, plus a fill, hover border and inner dot for each of the eight colors.
- 784fc7f: Add the missing elevation shadows: `shadow-dialog`, `shadow-drawer`, `shadow-dropdown`, `shadow-sidebar`, `shadow-toast` and `shadow-tooltip`.
- 784fc7f: Add the surface scale (`surface-1`, `surface-2`, `surface-3`, `surface-static`) and an `l3-background-30` layer tint. The 60 variants of the layer backgrounds now mix 20% transparency instead of 40%, and the primary callout icon, title and description were retuned in both themes.
- 784fc7f: Add semantic tokens for the switch: a track, thumb and track hover, a label and description color, and a background and hover background for each of the nine colors.
- 784fc7f: Add semantic tokens for tabs: a shared border, the label, hover label, hover background, indicator and radius of the primary treatment, and the background, hover background, label, hover, active and disabled label plus disabled stripe of the secondary treatment.
- 784fc7f: Add semantic tokens for the toggle group: a shared bar border, the background and label of an unpressed, hovered, pressed and disabled segment in the secondary outlined treatment, and the surface, chevron and shadow of the overflow arrow.

### Patch Changes

- 784fc7f: Point the secondary background, foreground and border at the layer tokens instead of raw neutral ramps, so they follow the surface scale. Hover backgrounds for primary, warning and danger now darken (600) rather than lighten (400), and the light warning background moves to amber 500.

## 2.1.7

### Patch Changes

- 2af04a5: Expose semantic tokens with docs

## 2.1.1

### Patch Changes

- added spacing variables from figma table

## 2.1.0

### Minor Changes

- added semantics tokens with default theme and typography styles

## 1.2.0

### Minor Changes

- added support for generating tailwind theme tokens i.e. @theme { ... }

## 1.1.4

### Patch Changes

- improve backward compatibility to fix the failing build

## 1.1.3

### Patch Changes

- design tokens backward compatibility

## 1.1.2

### Patch Changes

- extract design tokens json files

## 1.1.1

### Patch Changes

- fix the issue for consumers (unable to find type declarations)

## 1.1.2

### Patch Changes

- extract design tokens json files

## 1.1.1

### Patch Changes

- fix the issue for consumers (unable to find type declarations)

## 1.1.1

### Patch Changes

- fix the issue for consumers (unable to find type declarations)

## 1.1.0

### Minor Changes

- generate design tokens from json and overall improvements

## 1.0.0

### Major Changes

- Signoz Design Tokens first release
