# Light upon Light

A static website for interactive physics projects. No server code, no database: just HTML, CSS, JavaScript and images, so it can be hosted for free.

## Folder layout

```
lightuponlight/
├── index.html                      ← home page (built from src/home.html)
├── projects/
│   └── maxwell-3d/index.html       ← Maxwell in 3D (built from src/maxwell-3d.html)
├── assets/                         ← logo, icons, social preview image
│   ├── logo.png (1024 px)  logo-512.png  logo-192.png  logo-64.png  logo-32.png
│   ├── apple-touch-icon.png
│   └── social-card.jpg (1200×630, used when a link is shared)
├── src/                            ← the files you edit
│   ├── home.html
│   └── maxwell-3d.html
└── build.py                        ← turns src/ into the finished pages
```

You edit files in `src/`, run `python3 build.py`, and upload everything (except `src/` and `build.py` if you like).

## Put it online (free) with GitHub Pages

1. Create a free account at github.com.
2. Create a new public repository named `lightuponlight`.
3. Upload the contents of this folder (drag and drop on the repository page, then **Commit changes**).
4. In the repository: **Settings → Pages → Source: Deploy from a branch → Branch: main / (root) → Save**.
5. After about a minute the site is live at `https://YOUR-USERNAME.github.io/lightuponlight/`.

If you name the repository `YOUR-USERNAME.github.io` instead, the address becomes `https://YOUR-USERNAME.github.io/`.

Alternative without GitHub: go to app.netlify.com/drop and drag this folder onto the page. You get a link like `https://lightuponlight.netlify.app` immediately.

## Your own domain (e.g. lightuponlight.org)

1. Buy the domain from a registrar (e.g. Namecheap, Porkbun, Cloudflare, INWX). Usually about €10–20 per year.
2. GitHub: **Settings → Pages → Custom domain**, enter the domain, save.
3. At the registrar, add the DNS records GitHub shows you (four `A` records for the bare domain, and a `CNAME` record `www → YOUR-USERNAME.github.io`).
4. Back in GitHub Pages, tick **Enforce HTTPS** once it becomes available (can take up to a day).
5. Optional: set `SITE_URL` in `build.py` to the domain and rebuild, so shared links show the preview image.

## Add a new project

1. Put the project page at `src/my-project.html` (same style as `src/maxwell-3d.html`: a title, styles, then the page content).
2. In `build.py`, add a line to `pages`:
   `("src/my-project.html", "projects/my-project/index.html", 2, "One-sentence description."),`
3. In `src/home.html`, add an entry to the `PROJECTS` list near the top of the script:
   ```js
   {
     title: "My project",
     href: "projects/my-project/index.html",
     blurb: "What it does, in one or two sentences.",
     tags: ["Optics", "Interactive"],
     date: "Dec 2026",
     status: "Live",
     thumb: "assets/my-project.jpg"   // a 16:9 image you put in assets/
   },
   ```
   Delete or edit the "Your next project" placeholder entry.
4. Run `python3 build.py` and upload the changed files.

Inside a project page, link back home with `href="../../index.html"` and use the logo with `src="../../assets/logo-64.png"`.

## Notes

- Three.js and the fonts load from public CDNs (cdnjs, jsDelivr, Google Fonts), so visitors need an internet connection.
- The emblem is computed physics: white light (400–700 nm) from two coherent point sources, converted to colour with the CIE 1931 colour-matching functions. The animated version on the home page runs the same calculation live in a WebGL shader.
