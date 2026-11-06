# @signoz/design-tokens

## 2.6.0

### Minor Changes

- 3617f90: Add `avatar-{color}-background` and `avatar-{color}-foreground` for the reworked Avatar, in both themes,
  for primary, secondary, danger, warning, success, info, archive and highlight-danger. The avatar initials
  sit on one of eight colors. Seven of them match the solid Badge palette, and secondary matches the secondary
  Button. The values are copied from those tokens, so the avatar can diverge later.

## 2.5.0

### Minor Changes

- 69ab8b6: Add an opt-in stylesheet that loads Inter, `dist/fonts/inter.css`, with the font files next to it.

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

- dd2180f: Add a `pagination-*` set for the reworked Pagination, in both themes. `pagination-label` is the
  text of the bar (`l2-foreground`) and `pagination-label-hover` a hovered page or arrow
  (`l2-foreground-hover`). The current page is `pagination-page-current-background` (`primary-background`)
  with `pagination-page-current-label` (`primary-foreground`). `pagination-separator` is the line
  for the skipped pages (`l1-foreground`), `pagination-divider` the rule between Previous and Next
  (`secondary-border`) and `pagination-focus-ring` the focus ring (`ring`).
- 6585b48: Remove the typography primitives and the theme font families. The 33 text styles are the only
  typography tokens left.

  Every text takes its font from one style, so a component sets
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

- 13edb5d: Add `skeleton-background` and `skeleton-highlight` for the reworked Skeleton, in both themes. Both are
  translucent, black in light and white in dark, so a skeleton bar reads on any surface it sits on.
  The alphas match the Ant Design 5 skeleton the app renders today: the fill is 6% black in light and
  12% white in dark, the shimmer band 15% black in light and 18% white in dark.
- 6585b48: Align the 33 text styles with the Periscope type tokens page, and add a `typography-*` set for the
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

### Patch Changes

- dd2180f: Add the `popover-background`, `popover-border` and `popover-shadow` entries to `Style` and
  `StyleTailwind`. 2.4.0 shipped the CSS variables without regenerating the type files, so they had
  no `Style.POPOVER_*` constant or Tailwind key.

## 2.4.0

### Minor Changes

- 5212b82: Add a `popover-*` set for the reworked Popover, in both themes. `popover-background` is the
  translucent shell (`surface-3`), `popover-border` its hairline (`l2-border`) and `popover-shadow`
  the lift (`shadow-dropdown`), which is the dropdown shadow rather than the tooltip one. `popover`
  itself is untouched, since `calendar-select-background` reads it.

  `popover-foreground` is repointed to `l1-foreground`, so it follows the level scale like every
  other foreground instead of naming a primitive. That moves it one step for anything already using
  it: `#121317` to `#1e1f24` in light, and pure white to `#eceef2` in dark.

## 2.3.0

### Minor Changes

- 9ebef52: Add the `alert-strip-*` set for Alert Strip, in both themes and on primitive colours only. Each colour of the Badge union gets a fill (`alert-strip-{color}-background`), a text colour (`alert-strip-{color}-foreground`) and a link hover step (`alert-strip-{color}-link-hover`), with the same values the solid badge of that colour resolves to today, except the light secondary fill, which is `bg-neutral-light-700` so the strip stands apart from the page background. The action and close buttons share `alert-strip-button-background` (now described), `alert-strip-button-background-hover` and `alert-strip-button-foreground` on every colour, and `alert-strip-decoration` paints the dots on the tapered ends.
- 9ebef52: Rename `callout-error-*` to `callout-danger-*`, to match the `danger` color of Callout. `callout-error-{background,border,title,description,icon}` stay as deprecated aliases of the new names. Add `kbd-active-background`, and `callout-{primary,success,warning,danger}-background-hover` for the controls inside a callout. Add `callout-{info,archive,highlight-danger}-*` sets (aqua, sienna and sakura, the hues Badge uses), a neutral `callout-secondary-*` set on the `secondary-*` and `l*-foreground` tokens, and the `{info,archive,highlight-danger}-link` and `-link-hover` pairs. Add `line-height-26`. `dropdown-item-danger-background-hover` now holds its own value instead of aliasing `callout-error-background`. `paragraph-medium-400` line height is 26px, as in Figma. Add `size-icon-callout-sm` and `size-icon-callout-md` (12 and 16px), the icon size of each Callout size. Light `callout-success-*` and `callout-warning-*` background, border and background hover use step 500, as in Figma. Remove the unused `callout-aqua-*` and `callout-sienna-*` sets; `callout-info-*` and `callout-archive-*` cover those hues.
- 9ebef52: Add a `combobox-*` set for Combobox. The popup, row, group, separator, search, loading and empty tokens copy the `dropdown-*` values, so the popup matches Dropdown. The chip tokens copy `pill-rect-solid-*`. The field uses `l2-border` (`l3-border` on hover), `l1-foreground` for the value, `l3-foreground` for the placeholder and icons, and `primary-background` for the focus ring.
- 9ebef52: Add a `command-*` set for the Command palette. The values copy the popup part of the `combobox-*` set, so the palette matches Dropdown, Combobox and Select. There are no trigger, chip, control or separator tokens, since the palette has none of them. `command-backdrop` dims the page behind the palette, with the overlay colour of `Dialog`.
- 9ebef52: Add a `divider-*` set for the Divider. `divider-border` is the line, `divider-label` is the label of a horizontal divider. Both keep the values Divider used before, so nothing changes on screen.
- 9ebef52: Add an `input-*` set for the reworked Input: `input-background` (transparent, so the field sits on any surface), `input-border` / `input-border-hover` on `l2-border` / `l3-border`, `input-foreground`, `input-placeholder` / `input-placeholder-hover` and `input-icon` on the `l1`/`l2` foregrounds, `input-focus-ring` on `primary-background`, and per status (`success`, `warning`, `danger`) a tinted `input-{status}-background` / `input-{status}-border` (the callout `color-mix` recipe over forest/amber/cherry 500) and an `input-{status}-icon` aliasing the semantic background. Also a `field-*` set for the new Field wrapper: `field-label` / `field-label-hover` / `field-label-icon` on the `l1`/`l2` foregrounds, `field-required-marker` on `danger-background`, and per status a `field-{status}-label` / `field-{status}-message` text color (the callout description shade per mode) and `field-{status}-icon`.
- 9ebef52: Add a `progress-*` set for Progress: `progress-track` and `progress-value` on `l3-background` and `l1-foreground`, a `progress-{color}-indicator` fill per Badge color (`primary`, `success`, `warning` and `danger` alias the semantic backgrounds, `info`, `archive` and `highlight-danger` the `500` step of aqua, sienna and sakura, `secondary` is `l3-foreground` for now), and `progress-active-stripe` for the stripes of an active bar.
- 9ebef52: Add a `radio-cards-*` set for Radio Cards. An unchecked card uses the secondary action colours (`radio-cards-background`, `-border`, `-label`, `-icon` and their `-hover` steps), a checked card uses the primary callout colours (`radio-cards-checked-background`, `-border`, `-label`, `-icon`), and `radio-cards-focus-ring` is the keyboard ring.
- 9ebef52: Add a `select-*` set for Select. The values copy the `combobox-*` set, so the field matches Combobox and the popup matches Dropdown. There are no search tokens and no clear icon hover token, since Select has neither.
- 9ebef52: Add a `slider-{color}-indicator` set for Slider, one per Badge color, for the fill, the thumb border and the active mark dots. The values copy `progress-{color}-indicator`: `primary`, `success`, `warning` and `danger` alias the semantic backgrounds, `info`, `archive` and `highlight-danger` the `500` step of aqua, sienna and sakura, and `secondary` is `l3-foreground` for now. The track and the other mark dots are tints of the same color.
- 9ebef52: Add a `toast-*` set for the Toast surface, title, description, per-variant icons (`info`, `success`, `warning`, `danger`, `loading`) and button (label, hover label, hover fill, divider), on the semantic tokens the Figma Toast binds, plus `toast-focus-ring` on `ring` and `size-icon-toast` (16px) for the toast icon.

### Patch Changes

- 9ebef52: Paint the check of the selected row in a single Combobox or Select in the first level foreground: `combobox-item-indicator` and `select-item-indicator` now read `l1-foreground` instead of `primary-background`, in both themes.
- 9ebef52: In the light theme, the hover fill of a checked switch now goes one shade darker for every colour. `switch-success-hover-background` moves to `forest-700`, and `switch-info-hover-background`, `switch-archive-hover-background` and `switch-highlight-danger-hover-background` move to the 600 shade; they used to go lighter. The dark theme already went one shade lighter and is unchanged.

## 2.2.1

### Patch Changes

- d90ee8e: Add `pill-invalid-background`, `pill-invalid-dismiss-icon` and `pill-invalid-dismiss-icon-hover` for invalid closeable pills. In the light theme, the success foreground, the info, archive and highlight-danger foregrounds of badges and checkboxes, and the info, archive and highlight-danger radio dots move to `neutral-light-950`, the white end of the light neutral ramp. In the dark theme, the primary, warning and danger switch hover tracks lighten to 400.

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
