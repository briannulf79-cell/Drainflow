#!/usr/bin/env python3
"""
Drain Flow SEO/GEO rank baseline logger.

Runs a fixed set of local drain/sewer/plumber queries and logs whether
Rambo's business (Drain Flow Sewer and Plumbing, Oak Forest IL 60452)
surfaces — plus which domains show. Snapshot is timestamped and re-runnable
after go-live to measure real movement.

Usage:  python3 rank_baseline.py [label]
Writes: ~/projects/drainflow/rank-reports/<label>-<stamp>.md   (and history.csv)
"""
import datetime, os, re, sys, csv, urllib.request, urllib.parse

OUT = os.path.expanduser("~/projects/drainflow/rank-reports")
os.makedirs(OUT, exist_ok=True)

TARGET_MARKERS = [
    "Drain Flow Sewer and Plumbing",
    "Drainflow Sewer",
    "Babette Ct",
    "5543 Babette",
    "451-6767",
    "drainflowpro",
]

QUERIES = [
    "drain cleaning plumber near me",
    "sewer backup repair near me oak forest il",
    "hydro jetting chicago il",
    "sewer camera inspection oak forest il",
    "emergency plumber oak forest il",
    "drain line repair oak forest il",
    "sump pump repair oak forest il",
    "24/7 sewer and drain service chicago",
    "backed up basement floor drain chicago",
    "drainflowpro.com",
    "drain cleaning tinley park il",
    "plumber orland park il",
    "sewer backup chicago suburbs",
    "drain rooter service chicagoland",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        return urllib.request.urlopen(req, timeout=18).read().decode("utf-8", "ignore")
    except Exception:
        return ""

def google(query):
    """Return (found_target, [domains]) for one query."""
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query) + "&num=20&hl=en"
    html = fetch(url)
    if not html:
        return None, []
    # crude strip to text for marker detection
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    found = any(m.lower() in text.lower() for m in TARGET_MARKERS)
    # collect domains cited
    domains = []
    for pat in re.findall(r"https?://(?:www\.)?([A-Za-z0-9.-]+\.(?:com|net|org|io))", html):
        if pat not in domains:
            domains.append(pat)
    return (1 if found else 0), domains[:12]

def run(label="baseline"):
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    rows = []
    md = [f"# Drain Flow SEO/GEO Baseline", f"Generated: {datetime.datetime.now():%Y-%m-%d %H:%M}", ""]
    total = 0
    for q in QUERIES:
        hit, doms = google(q)
        if hit is None:
            status = "engine-blocked/no-data"
            present = 0
        else:
            present = hit
            status = "HIT" if hit else "miss"
        total += present
        rows.append((stamp, q, status, "; ".join(doms)))
        md.append(f"## {q}")
        md.append(f"- our listing: **{status}**")
        md.append(f"- domains seen: {', '.join(doms) if doms else 'none captured'}")
        md.append("")
    md.append(f"## Summary: our listing present in {total}/{len(QUERIES)} queries observed.")
    path = os.path.join(OUT, f"{label}-{stamp}.md")
    with open(path, "w") as f:
        f.write("\n".join(md))

    hist = os.path.join(OUT, "history.csv")
    fresh = not os.path.exists(hist)
    with open(hist, "a", newline="") as fh:
        w = csv.writer(fh)
        if fresh:
            w.writerow(["timestamp", "query", "status", "domains"])
        for r in rows:
            w.writerow(r)

    print(f"Wrote: {path}")
    print(f"Summary: our listing present in {total}/{len(QUERIES)} queries.")

if __name__ == "__main__":
    run("baseline")