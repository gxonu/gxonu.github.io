# Geonwoo Kim — personal website

Research, projects, experience and awards: <https://gxonu.github.io/>.

## Editing

- `content/profile.json`: reviewed project descriptions, resources and awards.
- `tools/build.py`: homepage and project-page templates, biography and experience.
- `assets/site.css`: responsive layout.
- `assets/GeonwooKim_CV.pdf`: public CV.
- `assets/certificates/`: public certificate copies with personal identifiers removed.

Build with Python 3 (standard library only):

```sh
python3 tools/build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

The generated `index.html` and `projects/*/index.html` are committed and served by GitHub Pages from the `main` branch. No browser JavaScript or client-side build is required.

Only publicly releasable content belongs in this repository. Unpublished manuscripts, application documents, private company metrics and original unredacted certificates are kept out of the website.
