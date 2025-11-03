# lit-agent Documentation

Reference extraction agent for analyzing Deepsearch results.

## Project Aim

**Reference Extraction**: Analyse Deepsearch results to extract references in various formats and intelligently resolve reference identifiers.

### Reference Types Supported
- Conventional academic references
- Plain URLs
- Numbered citations ([1], [2], etc.)
- Author-year citations (Osumi et al., 2025)
- Bibliography with miniref style citations

### Key Features
- Generate key-value pairs linking references to citations in text
- Intelligent extraction of reference identifiers
- URL resolution and page scraping for reference validation
- Handle various citation formats found in academic literature

## API Reference

```{toctree}
:maxdepth: 2

api/modules
```

## Development

This project follows strict test-driven development practices. See the development section for guidelines.

```{toctree}
:maxdepth: 2

development
```