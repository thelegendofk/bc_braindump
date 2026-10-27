---
name: arc42-docs-viewer
description: Create a browsable web-based documentation viewer for arc42 architecture docs. Renders markdown files at runtime (no rebuild on doc changes) with live Mermaid diagram rendering. Use when the user asks for a documentation site, docs viewer, browsable docs, or shareable architecture documentation.
---

# Arc42 Documentation Viewer Skill

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

- **Inception**: Scaffold the viewer early so the growing architecture docs are browsable from day one.
- **Build**: Keep the viewer running against the live docs. Updating a markdown file needs no rebuild.
- **Run**: Use the viewer as the shared, always-current reference for operations and stakeholders.

## Purpose

Build a lightweight, shareable web application that serves arc42 architecture documentation as a browsable site. The viewer loads markdown files at runtime via API and renders them client-side, so documentation updates never require a rebuild.

## When to Use

- The user wants to share architecture documentation with team members
- The user asks for a "docs site", "documentation viewer", or "browsable documentation"
- The project has arc42 markdown files in a `docs/arc42/` directory
- The user wants Mermaid diagrams rendered in the browser

## Architecture

The viewer has two parts:

1. **API routes** on the project's backend server that serve raw markdown files from disk
2. **Frontend application** that fetches and renders the markdown client-side

### Why This Architecture

- **Runtime loading**: Markdown files are read from disk on each API request. Updating a `.md` file is immediately reflected without rebuilding.
- **Client-side rendering**: `marked.js` converts markdown to HTML; `mermaid.js` renders diagram code blocks as SVG. Both run in the browser.
- **No content bundling**: The frontend build contains only the viewer shell, not the documentation content.

## Implementation Steps

### Step 1: Create the API Routes

Add a docs router to the project's backend server. Create two endpoints:

| Endpoint | Purpose |
|----------|---------|
| `GET /api/docs` | Lists available markdown files with display titles, ordered by section number |
| `GET /api/docs/:filename` | Returns raw markdown content as `text/plain` |

**Key implementation details:**

- Resolve the docs directory relative to the server's file location, pointing to the project's `docs/arc42/` directory.
- Define a `SECTION_ORDER` array to sort files in arc42 order: README first, then sections 01-12, then companion documents.
- Generate display titles from filenames: strip `.md`, split on the first hyphen for numbered sections (e.g., `01-introduction-and-goals.md` becomes `01. Introduction And Goals`), use "Overview" for `README.md`.
- Validate the `:filename` parameter: must end with `.md`, must not contain `..` or `/` (path traversal prevention).
- Return 404 for missing files, 400 for invalid filenames.
- These routes do NOT require authentication, documentation should be publicly accessible within the deployment.

Register the router in the server's route configuration.

### Step 2: Create the Frontend Application

Create a frontend application for the documentation viewer. Install the rendering dependencies:

```bash
install marked mermaid
```

### Step 3: Build the Viewer Frontend

The frontend is a single-page application with these components:

#### App (root component)

- Fetches the document list from `GET /api/docs` on mount
- Maintains state for: active document filename, raw markdown content, rendered HTML
- Loads markdown content from `GET /api/docs/:filename` when the user selects a section
- Converts markdown to HTML with `marked`, then post-processes:
  - Adds `id` attributes to `<h2>` and `<h3>` tags for anchor linking
  - Rewrites internal `.md` links (e.g., `href="05-building-block-view.md"`) to in-app navigation via `data-doc-link` attributes
- After HTML is set, scans for `<code class="language-mermaid">` blocks and replaces them with rendered SVG using `mermaid.render()`

#### Sidebar

- Fixed left panel with project branding (name, subtitle)
- Navigation grouped into:
  - **Overview** (README.md)
  - **Sections** (numbered 01-12)
  - **Companions** (functional-decomposition.md and any other non-numbered, non-README files)
- Active section highlighted
- Responsive: hidden on mobile, toggled via hamburger button

#### TableOfContents

- Right-side panel (visible on wide screens only)
- Extracts `<h2>` and `<h3>` headings from rendered HTML
- Renders as anchor links with indentation for h3
- Sticky positioning

#### SearchBar

- Filters the document list by title/filename
- Dropdown results navigate to the selected section

#### Styling

- Use the project's existing design tokens (colors, fonts) for consistency. For an Inacta-branded project, take the palette and typography from the `inacta-brand` skill
- Apply Tailwind's `@tailwindcss/typography` plugin for the `prose` class on rendered content
- Style tables with borders, code blocks with background color
- Mermaid diagrams centered in a `.mermaid-container` wrapper

### Step 4: Initialize Mermaid

Configure mermaid at module level (before any rendering):

```typescript
import mermaid from "mermaid";

mermaid.initialize({
  startOnLoad: false,    // we render manually
  theme: "neutral",
  securityLevel: "loose",
  fontFamily: "Inter, system-ui, sans-serif",
});
```

Use `mermaid.render(id, code)` for each code block. Each render call needs a unique DOM ID, use a counter or timestamp.

### Step 5: Internal Link Navigation

Markdown files cross-reference each other with relative links like `[see Section 05](05-building-block-view.md)`. These must navigate within the viewer, not trigger a page reload.

Approach:
1. After `marked` generates HTML, regex-replace `href="*.md"` with `href="#" data-doc-link="filename.md"`
2. Attach a click handler on the content container that intercepts clicks on `[data-doc-link]` elements and calls the document loader

### Step 6: Link from Main Application (Optional)

Add a discreet "System documentation" link on the main app's login or landing page pointing to the docs viewer path. This lets users access documentation without authentication.

### Step 7: Restart and Verify

1. Restart the server to pick up the new routes
2. Start the docs viewer
3. Verify: all sections load, mermaid diagrams render as SVG, internal links navigate correctly, search filters work

## Adapting to Other Projects

This skill works for any project with markdown documentation:

1. **Different docs directory**: Change the `DOCS_DIR` path in the API route to point to wherever the markdown files live.
2. **Different section ordering**: Update the `SECTION_ORDER` array to match the project's file naming convention.
3. **Different title generation**: Adjust the filename-to-title logic in the API route.
4. **No mermaid diagrams**: Skip the mermaid dependency and the diagram rendering code if the docs don't use mermaid.
5. **Different branding**: Update the sidebar colors and project name to match the host application.

## Relationship to Other Skills

- **arc42-documentation**: Produces the markdown files that this viewer displays. The viewer's section ordering and title generation assume arc42 naming conventions.
- **arc42-risk-audit**: May add entries to Section 11 that appear in the viewer automatically.
- **arc42-design-by-contract**: May add component specifications to Section 05 that appear in the viewer automatically.

## Production Considerations

- The API routes serve files from the local filesystem. In a deployed environment, the docs directory must be included in the deployment package.
- The docs endpoints are unauthenticated by design. If documentation should be restricted, add authentication middleware to the docs router.
- For static deployment (no API server), an alternative approach would be to copy markdown files into the frontend's `public/` directory and fetch them as static assets. This eliminates the API dependency but requires a rebuild when docs change.

## Portability

This skill is stack-neutral. It resolves everything project-specific, the language,
frameworks, database, test and deploy commands, ID prefixes, and the current
lifecycle phase, from `.vmodel.yml` and `docs/project-context.md` (see "Project
Context" above). To adopt it in a new project, run the `vmodel-setup` skill to scaffold the two
context files, fill in the stack and the current phase, and the skill adapts
automatically. It carries no assumption about any specific platform or vendor.
