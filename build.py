"""Builds the deployable site from src/.
   src/home.html       -> index.html
   src/maxwell-3d.html -> maxwell-3d.html
   Everything (pages and images) sits at the top level of the repository.
   Each page in src/ is a fragment (title, styles, body). This adds the <head> boilerplate."""
import re, pathlib
ROOT = pathlib.Path(__file__).parent
SITE_URL = ""   # set to e.g. "https://lightuponlight.org" once you have a domain (used for social previews)

def wrap(fragment, depth, desc, title_override=None):
    up = ""
    i = fragment.find("</style>") + len("</style>")
    head, body = fragment[:i], fragment[i:]
    og_img = (SITE_URL + "/social-card.jpg") if SITE_URL else "social-card.jpg"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0b0f17">
<link rel="icon" type="image/png" sizes="32x32" href="{up}logo-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{up}logo-192.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<meta property="og:site_name" content="Light upon Light">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<style>html,body{{margin:0}}[hidden]{{display:none!important}}img{{max-width:100%}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""

pages = [
  ("src/home.html", "index.html", 0, "Interactive physics of light, optics and electromagnetism."),
  ("src/maxwell-3d.html", "maxwell-3d.html", 0, "Maxwell's equations as an interactive 3D lab: 13 animated steps with live SI readouts."),
]
for src, out, depth, desc in pages:
    frag = (ROOT/src).read_text()
    (ROOT/out).parent.mkdir(parents=True, exist_ok=True)
    (ROOT/out).write_text(wrap(frag, depth, desc))
    print("built", out)
