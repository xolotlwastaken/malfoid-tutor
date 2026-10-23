---
name: Malfoid Study
description: A quiet place for algorithm explanations and thoughtful practice.
colors:
  paper: "#fafaf9"
  surface: "#fff"
  ink: "#202321"
  muted: "#646a66"
  line: "#e3e6e2"
  green: "#244f3e"
  green-soft: "#edf3ee"
  red: "#9c3636"
  red-soft: "#fbefed"
  focus: "#47836a"
typography:
  display:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif'
    fontSize: "clamp(48px, 5.5vw, 72px)"
    fontWeight: 630
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  headline:
    fontSize: "48px"
    fontWeight: 620
    lineHeight: 1.12
    letterSpacing: "-1.7px"
  title:
    fontSize: "19px"
    fontWeight: 600
    letterSpacing: "-0.4px"
  body:
    fontSize: "13px"
    lineHeight: 1.6
  label:
    fontSize: "11px"
rounded:
  control: "999px"
  surface: "16px"
  answer: "11px"
  compact-surface: "12px"
  hero: "24px"
spacing:
  mobile-gutter: "22px"
  desktop-gutter: "40px"
  action-gap: "22px"
  option-gap: "10px"
components:
  button-primary:
    backgroundColor: "{colors.green}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "12px 22px"
  button-secondary:
    backgroundColor: "#edf0eb"
    textColor: "{colors.green}"
    rounded: "{rounded.control}"
    padding: "12px 22px"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.green}"
    padding: "10px 0"
  filter-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
  quiz-option:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.answer}"
    padding: "14px 16px"
---

# Design System: Malfoid Study

## Overview

**Creative North Star: "User-pinned Apple-like restraint"**

User-pinned Apple-like restraint: white, graphite, forest green, system type, exact diagrams, generous space and quiet controls. Malfoid’s existing portrait supplies character; the interface keeps explanations, algorithm states and practice prominent.

The implementation opens with a spacious subject chooser, then uses a light study library, open lesson cards and compact contextual navigation. Its signature interaction is a checked choice resolving into a worked explanation in the same question.

**Key Characteristics:**

- System typography with large, tightly spaced headings.
- Forest-green actions and diagrams on warm white surfaces.
- Flat content, rounded controls and fine dividers.
- Responsive study layouts with visible answer feedback.

This captures the implemented local vanilla HTML/CSS/JavaScript interface. Sources: `web/public/style.css`, `web/public/index.html` and `web/public/app.mjs`; durable direction: `PRODUCT.md`. Reviewed desktop, mobile, lesson and submitted-answer screenshots are in `web/.impeccable/review/`.

## Colors

A restrained forest-green accent sits within warm white and graphite neutrals.

### Primary

- **Forest Green** (`green`): primary actions, active navigation underline, diagram emphasis, selected answers and positive feedback.
- **Soft Green** (`green-soft`): selected answers, active chapters and the resume banner.

### Neutral

- **Warm Paper** (`paper`): page and header.
- **White** (`surface`): answer options and inset controls.
- **Graphite** (`ink`): headings, body text and selected topic filters.
- **Muted Graphite** (`muted`): descriptions, timestamps and metadata.
- **Fine Divider** (`line`): section separators and header/footer rules.

### Semantic States

- **Answer Red** (`red`) and **Soft Red** (`red-soft`): incorrect answers and video errors.
- **Focus Green** (`focus`): the global keyboard outline, 3px with a 4px offset.
- Difficulty labels use green (`#edf3ee` / `#365b40`), ochre (`#f3eddf` / `#715722`) and rust (`#f5e8e5` / `#934533`). These are compact semantic labels, not extra brand accents.
- Lesson thumbnails alternate `#eff2ec`, `#f0f0f3` and `#f3f0e9`; diagrams retain the green family.

## Typography

All roles inherit the native system sans-serif stack in the frontmatter; no webfont is loaded. Headings use tight tracking and medium-to-semibold weights. Metadata stays compact and sentence case. Timestamps and array values use tabular numerals.

- **Display:** hero title; 630 weight, clamp 48–72px, 1.05 line height. At 1050px it is 58px, at 760px 56px, and at 375px 49px.
- **Headline:** page introduction, 48px / 620 / 1.12; 39px on mobile. Library section headings are 30px, reducing to 27px.
- **Title:** lesson card, 19px / 600; 17px on mobile and 15px at 375px.
- **Body:** lesson descriptions 13px / 1.6; hero description 18px / 1.6, reducing to 16px. Quiz stems are 23px / 1.45, reducing to 21px.
- **Label:** metadata generally 11–13px; mobile lesson metadata 10px. Buttons are 14px / 550.

## Layout

The main wrapper and header have a 1232px maximum outer width and 40px horizontal padding. At 760px and below, padding becomes 22px. The desktop hero uses a 1.18fr / 1fr grid with a 44px gap; it stacks on mobile. The library has three columns with 32px row and 25px column gaps, changing to two columns with 28px / 17px gaps on mobile.

Lesson playback uses a flexible video column plus a 290px chapter sidebar (250px below 1050px); these stack below 760px. The quiz uses .88fr / 1.12fr columns and a 55px gap (30px below 1050px), stacking below 760px. Topic filters scroll horizontally on mobile; search becomes full width. Quiz keyboard hints disappear on mobile.

The footer stacks on mobile. Lesson card footers wrap at 760px, with 10px / 12px gaps and practice links at least 30px tall, so counts and actions remain distinct at 390px and 375px. Additional breakpoints are 1400px for hero sizing and 375px for narrow-screen type/navigation adjustments.

## Elevation & Depth

The interface is predominantly flat. Background tones, thin dividers and whitespace separate content. The insertion-sort inset is the sole recurring shadowed surface: `0 8px 24px #223a2310`. Primary buttons move up 1px on hover; lesson thumbnail diagrams scale to 1.035. The hero portrait sits over a soft circular backdrop.

Motion uses `cubic-bezier(.16,1,.3,1)` where specified: button transform 250ms, thumbnail transform 500ms, answer feedback reveal 300ms and the repeating insertion-sort demonstration 5s (a 3px vertical lift of the already-placed key). Background transitions use ordinary `ease`. `prefers-reduced-motion: reduce` disables animations and transitions and restores automatic scrolling. The mobile sort demonstration is static.

## Shapes

Pill buttons and filters use 999px radii. Main thumbnails, video stages and quiz setup panels use 16px; mobile thumbnails and setup panels use 12px. The hero artwork uses 24px, sort inset 14px, answers 11px, chapter controls 9px and option letters 7px. Answer options use a 1px border; open lesson cards have no outer box or border. Icons are small inline SVG strokes with round caps and joins.

## Components

### Buttons

Primary buttons are green with white text, 12px / 22px padding and a 44px minimum height. Hover darkens to `#173d2d`; active returns the 1px hover lift to zero. Secondary buttons use `#edf0eb` with green text and hover `#e0e7df`. Text buttons have transparent backgrounds and 10px / 0 padding. Disabled buttons use `#e8ebe7` and `#747b74`, with no transform. All keep the global keyboard outline.

### Search and filters

Search is an unboxed 13px field with a bottom rule (`#bac2ba`) and an inline search icon; focus-within changes the rule to green. Topic filters are muted transparent pills, hover `#eef1ec`, selected graphite with white text via `aria-pressed`. Difficulty badges are 11px with 6px radii and 4px / 7px padding.

### Navigation

The 82px header contains the wordmark, Library/Practice links and progress link. Active links have a 2px green bottom rule and 600 weight. Below 760px the header is 72px; navigation gaps shrink, and progress shortens to “Progress” plus its dot. The skip link appears on focus.

### Lesson cards and chapters

Cards pair a rounded 1.65-aspect diagram thumbnail with metadata, a linked title, description and practice footer. A circular play control and duration badge sit inside the thumbnail; saved playback adds a 3px progress strip. Mobile thumbnails use aspect ratio 1.38. Chapter buttons are transparent until hover or active, when they use the soft-green surface and green text. Transcripts use native disclosure with timestamp links and fine row dividers.

### Answer and explanation

Options have a 59px minimum height, a compact letter box and a 1px `#daddd7` border. Hover changes border to `#6e8d77` and background to `#f4f7f2`. Selection applies green border/soft-green fill and reverses the letter box. Submitted correct answers use `#4b7958` / `#edf5ed`; incorrect answers use `#b66b65` / soft red. Locked options retain full opacity. Check/cross icons reinforce status.

Feedback appears below a fine divider in the same question, with a green or red heading and 13px / 1.8 explanation. Source details remain a compact native disclosure. A 3px green progress strip tracks the quiz.


### Expanded practice bank

Difficulty controls end with Baka, using a restrained violet accent to distinguish the extreme tier. The five controls wrap on narrow screens. Counts derive from the catalog (390 questions); each question supplies its own setup and optional graph, also available in results review. Graph edge-weight labels use an optional position fraction to avoid collisions on denser inputs. Original PDF is explicitly labelled as the 90-question edition.

### Subject home and contextual navigation

The root route is a subject chooser with a 40–64px system heading: a large two-line heading, a quiet introduction, and two generous subject panels with course codes, accurate lesson counts and precise algorithm/process-state diagrams. The panels use softly tinted backgrounds, 16px corners, 36px desktop padding and a fine footer rule. Their 24px column gap becomes a 20px vertical gap when two columns become one at 760px; mobile panel padding is 28px 25px 24px. The whole panel is a native link with a visible focus state; its subtle 3px arrow motion and background transition respect reduced motion.

Inside a course, All subjects and the current subject name replace the dropdown. Library and Practice remain local to that course, while the brand always returns to the chooser. The subject context moves to a second header row on mobile. Global progress retains a Subjects link.


## Do's and Don'ts

### Do:

- Do use forest green for primary actions, active diagrams and positive feedback.
- Do keep lesson card text on the page surface and diagrams inside rounded thumbnails.
- Do preserve the 22px mobile gutters and wrapping card footers.
- Do show selection, correctness and explanations together after submission.
- Do retain visible keyboard focus and reduced-motion support.

### Don't:

- Don’t replace the pinned minimal Apple-like direction with a new visual identity.
- Don’t introduce a separate display font, heavy card shadows or dashboard-style metric tiles.
- Don’t communicate an answer result through color alone; retain the status icon and explanation.
- Don’t force practice links and question counts onto one narrow mobile row.

### Malfoid home reaction

The subject-home introduction pairs its text with the original smug Malfoid pose. Hover or visible keyboard focus crossfades to the flustered pose; tapping toggles it for touch input. A native, labelled button retains the global focus ring. The original transparent sprite sheets are served as WebP and selected using CSS background positioning, preserving the source artwork. The portrait stacks beneath the introduction on mobile; reduced motion removes the crossfade.
