---
name: inacta-brand
description: "Inacta AG corporate identity (CI) reference. Use when building any UI, document, or visual asset for Inacta or projects branded under Inacta. Contains the official color palette, typography, logo SVG, and design principles."
---

# Inacta Brand Identity

## Project Context (read first)

Before doing anything, read the project context so this skill adapts to the target
project instead of assuming a stack:

- `.vmodel.yml` at the project root: machine-readable stack and command hooks (language, frameworks, database, `test-command`, `security-scan-command`, `deploy-command`), the ID prefixes, the docs path, and the current `lifecycle-phase`.
- `docs/project-context.md`: the human-readable brief and house rules (no em-dashes, Swiss German spelling).

If neither file exists, use the `vmodel-setup` skill, which scaffolds both files from
its bundled templates. If that skill is not installed, ask the user for the stack and the
current lifecycle phase and write the two files by hand. Never hardcode a stack, a
platform, or a test or deploy command. Always resolve them from the context.

## Phase Adaptation (Inception / Build / Run)

This skill runs in every lifecycle phase but shifts its depth and output focus
based on `lifecycle-phase` in `.vmodel.yml`:

- **Inception**: Brand the early artifacts (concept decks, context diagrams) for a consistent first impression.
- **Build**: Apply the palette and typography to the product user interface.
- **Run**: Style operational dashboards and shared documents consistently.

Inacta AG is a Swiss blockchain/DLT consulting and technology firm based in Zug, Switzerland. Their visual identity follows Swiss minimalist design principles, clean, precise, and functional.

## Color Palette

### Primary Colors

| Name | Hex | HSL | Usage |
|------|-----|-----|-------|
| Inacta Red | `#E50051` | `hsl(340, 96%, 45%)` | Primary accent, links, CTAs, active indicators, logo dot |
| Inacta Navy | `#10173a` | `hsl(230, 56%, 15%)` | Headings, body text, primary text color |

### Neutral Colors

| Name | Hex | Usage |
|------|-----|-------|
| Warm Gray | `#f3f2f1` | Backgrounds, hover states, code blocks, input fields |
| Light Background | `#fafaf9` | Page background, content area canvas |
| Mid Gray | `#e5e3e1` | Borders, dividers, table borders |
| Muted Text | `#6b6b78` | Secondary text, descriptions, labels |
| Light Muted | `#b0afad` | Tertiary text, timestamps, very subtle labels |
| White | `#ffffff` | Cards, sidebar, content panels |

### CSS Custom Properties

```css
:root {
  --inacta-navy: #10173a;
  --inacta-red: #E50051;
  --inacta-warm-gray: #f3f2f1;
  --inacta-mid-gray: #e5e3e1;
  --inacta-text: #10173a;
  --inacta-text-muted: #6b6b78;
  --inacta-light-bg: #fafaf9;
}
```

### Tailwind/shadcn Theme Variables (HSL format)

```css
:root {
  --background: 30 5% 95%;
  --foreground: 230 56% 15%;
  --border: 30 5% 88%;
  --card: 0 0% 100%;
  --card-foreground: 230 56% 15%;
  --primary: 340 96% 45%;
  --primary-foreground: 0 0% 100%;
  --secondary: 30 5% 95%;
  --secondary-foreground: 230 56% 15%;
  --muted: 30 5% 93%;
  --muted-foreground: 240 5% 46%;
  --accent: 340 96% 45%;
  --accent-foreground: 0 0% 100%;
  --ring: 340 96% 45%;
}
```

## Typography

### Font Stack

| Role | Font | Fallback |
|------|------|----------|
| Body / UI | Inter | system-ui, sans-serif |
| Headings | Inter (semibold/bold) | system-ui, sans-serif |
| Code | JetBrains Mono | Fira Code, monospace |

```css
:root {
  --app-font-sans: "Inter", system-ui, sans-serif;
  --app-font-mono: "JetBrains Mono", "Fira Code", monospace;
}
```

### Heading Styles

- **H1**: 1.75rem, bold, navy, red underline (`border-bottom: 2px solid #E50051`)
- **H2**: 1.25rem (xl), semibold, navy, gray underline (`border-bottom: 1px solid #e5e3e1`)
- **H3**: 1rem (base), semibold, navy, no underline
- **Body**: 0.875rem (sm) or 1rem, regular weight, navy text

### Section Numbers

When displaying numbered sections or list items with numeric identifiers:
- Use monospace font (`font-mono`)
- 11px size, semibold
- Color: muted gray (`#b0afad`) by default, Inacta red (`#E50051`) on hover/active

## Logo

### Verbindliche Dateien

Das Logo wird als Datei eingesetzt, nicht nachgebaut. Quelle:

```
99 Methods/Brand Assets/Logo/inacta-logo.svg           helle Flächen, Standard
99 Methods/Brand Assets/Logo/inacta-logo.png           Fallback, transparent, 2000 px
99 Methods/Brand Assets/Logo/inacta-logo-negativ.svg   dunkle Flächen, vor allem Navy 10173A
99 Methods/Brand Assets/Logo/inacta-logo-negativ.png   Fallback für dunkle Flächen
99 Methods/Brand Assets/Logo/inacta-logo-schutzraum.pdf
```

Regeln und Herkunft in `99 Methods/Brand Assets/BRAND_ASSETS.md`. Der Punkt im Logo ist
`E60050`. Der Schriftzug ist schwarz, in der Negativvariante weiss, er ist nicht navy.
Seitenverhältnis 2.635 zu 1, nur proportional skalieren.

Das folgende Inline-SVG ist nur für Web-Oberflächen gedacht, in denen keine Datei geladen
werden kann. Wo eine Datei möglich ist, gilt die Datei.

### SVG Wordmark

The Inacta logo is a wordmark ("INACTA") with a distinctive red dot at the end. The dot uses the primary Inacta Red (`#E50051`), and the wordmark text uses Inacta Navy (`#10173a`).

```tsx
function InactaLogo({ className }: { className?: string }) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 32" className={className}>
      <g fill="none">
        <path fill="#E50051" d="M175.12847 31.37536c2.453 0 4.441-1.9852 4.441-4.4341s-1.988-4.4341-4.441-4.4341c-2.452 0-4.44 1.9852-4.44 4.4341s1.988 4.4341 4.44 4.4341Z"/>
        <path fill="#10173a" d="M75.53847 30.90676h-5.074c-.108 0-.203-.0633-.241-.1583l-2.8948-6.8286h-14.6643l-2.8822 6.8349c-.038.095-.133.1584-.2407.1584h-4.9029c-.19 0-.3167-.1901-.2407-.3674L57.54827.48875c.0443-.0951.133-.1584.2407-.1584h4.6115c.1013 0 .1963.0633.2407.1584l13.1503 30.057c.063.171-.063.361-.253.361ZM59.79697 7.17155l-5.0549 11.7188c-.0633.1457.0443.304.2027.304h10.0971c.1584 0 .2597-.1583.2027-.304l-5.0422-11.7188c-.076-.1774-.3294-.1774-.4054 0Zm64.1175 23.7352h-4.865c-.146 0-.26-.114-.26-.2597V5.70828c0-.1203-.095-.2153-.215-.2153h-9.47c-.146 0-.26-.1141-.26-.2598V.81177c0-.1457.114-.2597.26-.2597h24.755c.146 0 .26.114.26.2597v4.4214c0 .1457-.114.2598-.26.2598h-9.47c-.12 0-.215.095-.215.2153v24.93879c0 .1457-.121.2597-.26.2597Zm-119.19527 0H.5385c-.2978 0-.5385-.2407-.5385-.5384V1.08416c0-.2978.2407-.5385.5385-.5385h4.1807c.2977 0 .5384.2407.5384.5385v29.2842c0 .2977-.2407.5384-.5384.5384Zm88.51727-4.3836c-6.214 0-11.205-5.2449-10.768-11.5477.373-5.4097 4.833-9.7551 10.255-10.0085 3.25-.152 6.208 1.1402 8.279 3.2813.102.1077.266.1077.374.0063l3.123-3.1229c.101-.1013.101-.266.006-.3674-3.021-3.1102-7.322-4.9789-12.061-4.7445-8.063.3991-14.575 6.9679-14.898 15.019-.361 8.9569 6.803 16.3303 15.69 16.3303 4.58 0 8.697-1.9574 11.567-5.0803.095-.1013.089-.266-.006-.361l-3.079-3.0786c-.108-.1077-.279-.1013-.38.0127-1.983 2.2487-4.878 3.6613-8.102 3.6613Zm70.56 4.3836h-5.074c-.108 0-.203-.0633-.241-.1583l-2.895-6.8286h-14.664l-2.882 6.8349c-.038.095-.133.1584-.241.1584h-4.903c-.19 0-.316-.1901-.24-.3674l13.15-30.057c.044-.0951.133-.1584.241-.1584h4.611c.102 0 .197.0633.241.1584l13.15 30.057c.064.171-.063.361-.253.361Zm-15.741-23.7352-5.055 11.7188c-.063.1457.044.304.203.304h10.097c.158 0 .259-.1583.202-.304l-5.042-11.7188c-.076-.1774-.329-.1774-.405 0ZM35.56807.54565h4.7318c.1457 0 .2597.114.2597.2597v29.8417c0 .1457-.114.2597-.2597.2597h-3.4713c-.0823 0-.1583-.038-.209-.1014l-17.7492-21.1381c-.152-.1963-.4687-.0886-.4687.1584v20.815c0 .1457-.114.2597-.2597.2597h-4.5372c-.1457 0-.2597-.114-.2597-.2597V.80545c0-.1457.114-.2597.2597-.2597h3.4776c.0824 0 .1584.038.209.1013L35.3516 21.7852c.152.1964.4687.0887.4687-.1583V.80545c0-.1457.114-.2597.2597-.2597Z"/>
      </g>
    </svg>
  );
}
```

### Logo Usage Guidelines

- Minimum height: 24px (`h-6`)
- Prefer the file from `99 Methods/Brand Assets/Logo/` over any redrawn wordmark
- Always place on white or light backgrounds
- The red dot is integral, never remove or recolor it
- Do not stretch or distort proportions
- Provide adequate clear space around the logo

## Design Principles

### Swiss Minimalist Aesthetic

1. **Clean whitespace**: Generous padding and margins. Content breathes.
2. **Flat design**: No shadows on cards or panels. Use borders (`border border-border`) for containment.
3. **Precision**: Exact alignment, consistent spacing, mathematical grid.
4. **Functional**: Every element serves a purpose. No decorative elements.
5. **Typography-driven**: Hierarchy communicated through size, weight, and color, not decoration.

### Component Patterns

- **Cards**: `bg-white rounded-md border border-border`, no shadows
- **Active states**: `bg-[#f3f2f1]` warm gray background
- **Hover states**: `hover:bg-[#f9f8f7]` subtle warm tint
- **Buttons (primary)**: `bg-[#E50051] text-white` rounded
- **Links**: `text-[#E50051]` with `hover:underline`
- **Inputs**: `bg-[#f3f2f1] border-0 rounded-md focus:ring-2 focus:ring-[#E50051]/20`
- **Labels/captions**: `text-[10px] font-semibold uppercase tracking-[0.12em] text-[#b0afad]`
- **Section headers**: `text-[#10173a]` with bottom border in red (h1) or mid-gray (h2)

### Prose/Content Styling

```css
.prose {
  --tw-prose-body: #10173a;
  --tw-prose-headings: #10173a;
  --tw-prose-links: #E50051;
}

.prose a { color: #E50051; text-decoration: none; font-weight: 500; }
.prose a:hover { text-decoration: underline; }
.prose pre { background: #f8f7f6; border: 1px solid #e5e3e1; border-radius: 0.375rem; font-size: 13px; }
.prose code:not(pre code) { background: #f3f2f1; padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #10173a; }
.prose th { background: #f3f2f1; font-weight: 600; color: #10173a; }
.prose blockquote { border-left: 2px solid #E50051; color: #6b6b78; }
.prose h1 { border-bottom: 2px solid #E50051; }
.prose h2 { border-bottom: 1px solid #e5e3e1; }
```

## Brand Context

- **Company**: Inacta AG
- **Location**: Zug, Switzerland
- **Industry**: Blockchain, DLT, digital transformation consulting
- **Website**: inacta.ch
- **Tone**: Professional, precise, trustworthy, Swiss quality
- **Currency**: CHF (Swiss Franc)
- **Language**: Professional English (Swiss market)

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
