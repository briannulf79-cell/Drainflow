#!/usr/bin/env python3
"""Generate a polished, branded PDF report for Drain Flow visibility baseline."""
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, ListFlowable, ListItem, HRFlowable)

OUT = "Drain-Flow-Visibility-Report-2026-08-23.pdf"

# ---- Brand palette ----
ACCENT   = colors.HexColor("#0B5FA5")   # professional blue
DARK     = colors.HexColor("#1A2430")
LIGHTBG  = colors.HexColor("#F0F5FA")
GREY     = colors.HexColor("#5A6B7B")
GREEN    = colors.HexColor("#1E7A4C")
AMBER    = colors.HexColor("#B57A1E")
RED      = colors.HexColor("#B03A2E")

styles = getSampleStyleSheet()

def S(name, **kw):
    base = dict(leading=15, spaceAfter=8, textColor=DARK)
    base.update(kw)
    return ParagraphStyle(name, **base)

st_title   = S("title", fontName="Helvetica-Bold", fontSize=26, leading=30, textColor=ACCENT, alignment=TA_LEFT)
st_sub     = S("sub", fontSize=13, leading=18, textColor=GREY)
st_h1      = S("h1", fontName="Helvetica-Bold", fontSize=17, leading=20, textColor=ACCENT, spaceBefore=14, spaceAfter=8)
st_h2      = S("h2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=DARK, spaceBefore=10, spaceAfter=4)
st_body    = S("body", fontSize=10.5, alignment=TA_JUSTIFY)
st_label   = S("label", fontName="Helvetica-Bold", fontSize=10.5, spaceAfter=2)
st_meta    = S("meta", fontSize=10, leading=14, textColor=GREY, spaceAfter=1)
st_status  = S("status", fontSize=10.5)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    canvas.drawString(0.75*inch, 0.5*inch, "Drain Flow Sewer & Plumbing — Digital Visibility Report (Confidential)")
    canvas.drawRightString(letter[0]-0.75*inch, 0.5*inch, f"Page {doc.page}")
    canvas.setStrokeColor(LIGHTBG); canvas.setLineWidth(1)
    canvas.line(0.75*inch, 0.72*inch, letter[0]-0.75*inch, 0.72*inch)
    canvas.restoreState()

story = []

def heading(t): story.append(Paragraph(t, st_h1))
def sub(t):     story.append(Paragraph(t, st_h2))
def body(t):
    story.append(Paragraph(t, st_body))
    story.append(Spacer(1, 4))

# ============================ TITLE PAGE ============================
story.append(Spacer(1, 2.0*inch))
story.append(Paragraph("Digital Visibility", st_title))
story.append(Paragraph("Readiness Report", st_title))
story.append(Spacer(1, 0.15*inch))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=14))
story.append(Paragraph("Search Engine (SEO) & AI-Assisted Search (GEO) Baseline", st_sub))
story.append(Spacer(1, 0.6*inch))

info = Table([
    ["CLIENT", ""],
    ["Drain Flow Sewer and Plumbing", ""],
    ["Address", "5543 Babette Ct, Oak Forest, IL 60452"],
    ["Phone", "(773) 451-6767"],
    ["Service area", "All of Chicago and surrounding suburbs"],
    ["Website", "drainflowpro.com"],
    ["Prepared by", "Entrepreneur Avenues — Digital Visibility Services"],
    ["Date", "August 23, 2026"],
], colWidths=[1.5*inch, 4.6*inch])
info.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"Helvetica"),
    ("FONTSIZE",(0,0),(-1,-1),10.5),
    ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
    ("TEXTCOLOR",(0,0),(0,-1),ACCENT),
    ("TEXTCOLOR",(1,0),(1,0),DARK),
    ("FONTNAME",(1,0),(1,0),"Helvetica-Bold"),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("TOPPADDING",(0,0),(-1,-1),6),
    ("LINEBELOW",(0,0),(-1,-2),0.5,LIGHTBG),
]))
story.append(info)
story.append(Spacer(1, 0.5*inch))
body("This report establishes a transparent baseline of the business's current online "
     "visibility and documents the optimization work completed on a rebuilt website. "
     "It is designed to be re-run after launch so results can be measured honestly.")
story.append(PageBreak())

# ============================ 1. EXEC SUMMARY ============================
heading("1. Executive Summary")
body("Drain Flow Sewer and Plumbing is a fourth-generation, family-run drain and sewer "
     "company serving all of Chicago and the surrounding suburbs. The business holds a "
     "verified Google Business Profile (4.9 stars, 55+ reviews) and maintains an active "
     "Facebook page and YouTube channel. The previous website was a basic single-page site "
     "with no structured data, which limited how well search engines and AI assistants "
     "could understand and cite the business.")
body("A fully rebuilt, multi-page website has been completed and reviewed. It adds "
     "structured data (schema) that helps Google and AI search engines identify the "
     "business, its services, service area, and hours — the foundation of local ranking "
     "and AI-assisted search (GEO). This report establishes an honest baseline so future "
     "results can be measured transparently.")
story.append(PageBreak())

# ============================ 2. BUSINESS PROFILE ============================
heading("2. Business Profile (Verified Facts)")
profile = [
    ["Business name", "Drain Flow Sewer and Plumbing"],
    ["Google rating", "4.9 / 5 stars (verified Google Business Profile)"],
    ["Google reviews", "69 real reviews (4-9 rating)"],
    ["Hours", "24/7 emergency availability"],
    ["Facebook", "active"],
    ["YouTube", "@drainflowpro"],
]
def fact_table(rows, widths=(2.1*inch, 4.0*inch)):
    t = Table([["<b>%s</b>" % k, v] for k, v in rows], colWidths=widths)
    t.setStyle(TableStyle([
        ("FONTNAME",(0,0),(-1,-1),"Helvetica"),
        ("FONTSIZE",(0,0),(-1,-1),10.5),
        ("FONTNAME",(0,0),(0,-1),"Helvetica-Bold"),
        ("TEXTCOLOR",(0,0),(0,-1),DARK),
        ("BACKGROUND",(0,0),(-1,-1),LIGHTBG),
        ("GRID",(0,0),(-1,-1),0.5,colors.white),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),7),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("LEFTPADDING",(0,0),(-1,-1),10),
    ]))
    return t

story.append(fact_table(profile))
story.append(Spacer(1, 8))
story.append(PageBreak())

# ============================ 3. BASELINE ============================
heading("3. Baseline Visibility Assessment")
body("This section reflects the business's standing as of August 23, 2026, before the rebuilt "
     "website goes live. Any item marked 'To verify' is an honest gap we will confirm after "
     "launch with real browser searches — we do not report unverified rankings as fact.")
baseline = [
    ["Check", "Status", "Notes"],
    ["Findable by name", "PASS", "Searching 'drain flow oak forest il' surfaces the profile and site"],
    ["Google Business Profile live", "PASS", "4.9 stars, 55+ reviews; maps link verified"],
    ["Domain resolves", "PASS", "drainflowpro.com returns HTTP 200"],
    ["Ambiguous term ('drainflow plumbing')", "NOT VISIBLE", "Other 'Drain Flow' businesses rank instead (CA, NY, AL, AU)"],
    ["Local service-query ranking", "TO VERIFY", "Re-check after launch in a real browser"],
    ["AI-assistant citations", "TO VERIFY", "Test ChatGPT/Perplexity/Gemini for citations"],
]
t = Table(baseline, colWidths=[2.2*inch, 1.5*inch, 2.5*inch])
def cell_color(v):
    v = v.lower()
    if "pass" in v: return GREEN
    if "not visible" in v: return RED
    return AMBER
style = TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"Helvetica"),
    ("FONTSIZE",(0,0),(-1,-1),9.5),
    ("BACKGROUND",(0,0),(-1,0),ACCENT),
    ("TEXTCOLOR",(0,0),(-1,0),colors.white),
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("GRID",(0,0),(-1,-1),0.5,LIGHTBG),
    ("TOPPADDING",(0,0),(-1,-1),6),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("LEFTPADDING",(0,0),(-1,-1),8),
])
for i in range(1, len(baseline)):
    style.add("TEXTCOLOR",(1,i),(1,i),cell_color(baseline[i][1]))
t.setStyle(style)
story.append(t)
story.append(Spacer(1, 8))
sub("Targeted money queries")
body("Queries a real customer types, to be logged on launch day: drain cleaning near me, "
     "sewer backup repair oak forest, hydro jetting chicago, sewer camera inspection oak "
     "forest, emergency plumber oak forest, sump pump repair tinley park, and backed-up "
     "basement floor drain chicago.")
story.append(PageBreak())

# ============================ 3b. GBP PERFORMANCE BASELINE ============================
heading("3b. Google Business Profile — Performance Baseline")
body("Captured August 24, 2026 from the business's real Google Business Profile manager "
     "(six-month window, March–August 2026). These are verified profile metrics, not estimates. "
     "The profile is the primary way local customers find the business, so these are the core "
     "baseline numbers to compare against after launch.")
gp = [
    ["Metric", "6-mo total"],
    ["Profile views", "4,361"],
    ["Profile interactions", "546"],
    ["Search appearances (queries)", "389"],
    ["Calls made from profile", "87"],
    ["Direction requests", "326"],
    ["Website clicks from profile", "133"],
]
gt = Table(gp, colWidths=[3.4*inch, 2.8*inch])
gstyle = TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"Helvetica"),
    ("FONTSIZE",(0,0),(-1,-1),10.5),
    ("BACKGROUND",(0,0),(-1,0),ACCENT),
    ("TEXTCOLOR",(0,0),(-1,0),colors.white),
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("GRID",(0,0),(-1,-1),0.5,LIGHTBG),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("LEFTPADDING",(0,0),(-1,-1),10),
])
for i in range(1, len(gp)):
    gstyle.add("FONTNAME",(0,i),(0,i),"Helvetica-Bold")
gt.setStyle(gstyle)
story.append(gt)
story.append(Spacer(1, 10))

sub("Monthly trend (March–August 2026)")
body("Profile interactions: Mar 78, Apr 83, May 95, Jun 90, Jul 135, Aug 65. "
     "Calls: Mar 11, Apr 17, May 11, Jun 16, Jul 22, Aug 10. "
     "Direction requests: Mar 39, Apr 52, May 58, Jun 52, Jul 84, Aug 41. "
     "Website clicks: Mar 28, Apr 14, May 26, Jun 22, Jul 29, Aug 14.")
body("The pattern is a clear July peak followed by an August decline across every metric. "
     "Per the owner, heavy rainfall drives calls when sewers are overwhelmed, so the July peak "
     "likely reflects demand (wet-weather overflow calls) rather than a change in the business "
     "itself. August's lower numbers should therefore be read as returning to a normal baseline, "
     "not a decline in ranking — weather is a known external variable in this trade.")
sub("Top search queries (how customers find the profile)")
body("drain cleaner (177), sump pump (79), plumbers near me (39), french drain (21), "
     "emergency plumber near me (20). The volume on sump pumps and french drains — higher-ticket "
     "service terms — is a strong signal to feature these services prominently on the rebuilt site.")
body("Note: 'Bookings' was 0 across the board, but the business has no online booking scheduler — "
     "customers call and the owner takes the job. So the 0 is a baseline-of-absence (no feature "
     "yet), not a performance shortfall; it becomes a meaningful metric only if booking is added.")
story.append(PageBreak())

# ============================ 4. OPTIMIZATION ============================
heading("4. Optimization Completed (Rebuilt Website)")
sub("4.1 Pages")
body("The single-page site was rebuilt into 10 pages: Home, Services, About, Media, Reviews, "
     "Blog (3 articles), Contact, and a new FAQ page.")
sub("4.2 Structured Data (Schema)")
body("Added schema.org markup so search engines and AI assistants can read the business cleanly:")
story.append(ListFlowable([
    ListItem(Paragraph("Plumber / LocalBusiness schema on every page (NAP, hours, service area, services, rating)", st_body), leftIndent=10),
    ListItem(Paragraph("WebSite schema with publisher linkage", st_body), leftIndent=10),
    ListItem(Paragraph("FAQPage schema on the FAQ page (auto-generated from visible content)", st_body), leftIndent=10),
    ListItem(Paragraph("BlogPosting schema on all 3 articles (author: Dwayne Rambo)", st_body), leftIndent=10),
    ListItem(Paragraph("sameAs entity links: Google Business Profile, Facebook, YouTube", st_body), leftIndent=10),
], bulletType="bullet"))
story.append(Spacer(1, 6))
sub("4.3 Technical SEO")
story.append(ListFlowable([
    ListItem(Paragraph("Unique descriptive titles and meta descriptions per page", st_body), leftIndent=10),
    ListItem(Paragraph("Per-page canonical URLs", st_body), leftIndent=10),
    ListItem(Paragraph("Open Graph + Twitter Card meta for social sharing", st_body), leftIndent=10),
    ListItem(Paragraph("sitemap.xml listing all pages and robots.txt pointing to it", st_body), leftIndent=10),
    ListItem(Paragraph("A dedicated FAQ page with customer-rated Q&A crafted to be AI-citable", st_body), leftIndent=10),
], bulletType="bullet"))
story.append(Spacer(1, 6))
sub("4.4 Content & Honesty Standards")
body("Copy was aligned to the owner's direction: no pricing posted, no insurance/license detail, "
     "no fabricated testimonials, no invented statistics, and unsupported superlatives were removed. "
     "The FAQ reflects the owner's real expertise (e.g., floor-drain water during rain indicating a "
     "backed-up sewer main). Only verified business facts are used.")
story.append(PageBreak())

# ============================ 5. ROADMAP ============================
heading("5. SEO & GEO Roadmap (Ongoing)")
story.append(ListFlowable([
    ListItem(Paragraph("Google Business Profile: keep exact name/address/phone (NAP), add website link, hours, services, and real photos", st_body), leftIndent=10),
    ListItem(Paragraph("Consistent citations across Bing Places, Apple Business Connect, and local directories", st_body), leftIndent=10),
    ListItem(Paragraph("Regular honest blog content targeting service and area keywords", st_body), leftIndent=10),
    ListItem(Paragraph("Internal links between services, FAQ, blog, and contact pages", st_body), leftIndent=10),
    ListItem(Paragraph("Post-launch: log target-query rankings and AI citations, then re-measure into a comparison report", st_body), leftIndent=10),
], bulletType="bullet"))
story.append(Spacer(1, 10))

# ============================ 6. MEASURING ============================
heading("6. Measuring Results (Transparency)")
body("Two to four weeks after the new site goes live, the same queries and checks in Section 3 "
     "will be re-run from a real browser. A follow-up report will compare against this baseline — "
     "page by page and query by query — so we can see honestly whether visibility improved. "
     "If a metric did not move, we report that too.")
body("This baseline is deliberately conservative. No unverified rankings are claimed. Where a "
     "ranking is not yet visible or not yet checked, this report says so.")
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=LIGHTBG, spaceAfter=6))
story.append(Paragraph(
    "<i>Prepared with honesty as the core principle: we report what is true, and we label "
    "unknown items as unknown.</i>", st_meta))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.9*inch, rightMargin=0.9*inch,
                        topMargin=0.8*inch, bottomMargin=0.9*inch,
                        title="Drain Flow Visibility & Readiness Report",
                        author="Entrepreneur Avenues · Digital Visibility")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("OK:", OUT)