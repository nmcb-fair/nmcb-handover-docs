# NMCB hand-over documentation

This repository contains the GitHub Markdown source for the **NMCB data management and data infrastructure hand-over**.

It is designed to be published with **MkDocs Material** as a documentation website (top-level **tabs** for Workflows / Systems / FAIR / Tasks, navy–teal palette, custom sidebar hierarchy).

## Run locally

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

## Build static site

```bash
mkdocs build
```

## Publish with GitHub Pages

This repository includes a GitHub Actions workflow in `.github/workflows/deploy.yml`.

After pushing to GitHub:

1. Go to **Settings > Pages**
2. Set **Source** to **GitHub Actions**
3. Push to the default branch
4. The documentation site will be deployed automatically
```
