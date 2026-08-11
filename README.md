# Drain Flow Sewer and Plumbing Website

A professional, mobile-responsive website for Drain Flow Sewer and Plumbing - a family-run plumbing business in Oak Forest, IL.

**Multi-page build (Aug 2026).** 7 pages sharing one nav/footer + one branding theme:

| Route | Page |
|-------|------|
| `index.html` | Home |
| `services.html` | Services |
| `about.html` | About |
| `media.html` | Media — YouTube videos + job & equipment gallery |
| `blog.html` | Blog — educational articles |
| `reviews.html` | Reviews |
| `contact.html` | Contact |

## 🚀 Quick Start

**To edit the site**, edit the *source* files, NOT the built HTML in the repo root:

- `_partials/head.html` — shared header + nav (edit once, every page updates)
- `_partials/foot.html` — shared footer + footer script
- `_pages/*.html` — each page's body content
- `styles.css` — original theme · `styles.multipage.css` — media/blog/interior styles

**Rebuild after any edit:**

```bash
python3 build.py
```

This wraps `_pages/*.html` bodies in the shared head/foot and writes the final
`*.html` files to the repo root — so header/footer/nav only ever need to be
changed in ONE place and branding stays consistent across every page. It's a
plain static site with no other build step; just ship the repo root.

To add a new page: create `_pages/<name>.html` (start with the `{{ title: ... }}
{{ desc: ... }}` header lines), add a nav link in `_partials/head.html`, re-run
`build.py`.

## 🔧 Content Rambo Still Needs to Supply

- **Media page:** his real YouTube channel/thumbnail links (currently a placeholder
  `@drainflow` handle) and real job + equipment photos (placeholder tiles are in place).
- **Blog page:** the article bodies (cards are starter education topics he can
  edit or replace).

## 📁 Files

## 🌐 Deployment Options (Ranked by Cost & Ease)

### Option 1: GitHub Pages (FREE - Recommended)

**Best for:** Free hosting with custom domain support

1. Create a GitHub account (if you don't have one)
2. Create a new repository named `drainflow-website` (or any name)
3. Upload these files to the repository
4. Go to **Settings** → **Pages**
5. Under "Source", select **main** branch
6. Click Save
7. Your site will be live at: `https://yourusername.github.io/drainflow-website`

**Custom Domain:** You can connect a custom domain (like `drainflowplumbing.com`) for free in the Pages settings.

### Option 2: Netlify (FREE)

**Best for:** Easy drag-and-drop deployment

1. Go to [netlify.com](https://netlify.com) and sign up
2. Drag and drop this entire folder onto the Netlify dashboard
3. Done! You'll get a URL like `random-name.netlify.app`
4. Rename it or add a custom domain in settings

### Option 3: Cloudflare Pages (FREE)

**Best for:** Fast global CDN, great performance

1. Sign up at [pages.cloudflare.com](https://pages.cloudflare.com)
2. Connect your GitHub repository
3. Deploy with one click

### Option 4: Vercel (FREE)

**Best for:** Easy GitHub integration

1. Sign up at [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Deploy automatically

---

## 🔑 Domain Name Options

The site will need a domain name. Options:

| Provider | Typical Cost | Notes |
|----------|--------------|-------|
| Namecheap | ~$10-15/year | Good prices, easy to use |
| Google Domains | ~$12/year | Simple, integrates well |
| Cloudflare | ~$9/year | At-cost pricing, no markup |
| GoDaddy | ~$15-20/year | Popular but often more expensive |

**Suggested domains to check:**
- drainflowplumbing.com
- drainflowsewer.com
- drainflowchicago.com

---

## 🤝 Transferring Ownership to Your Friend

### Method 1: Have Them Create Everything (Cleanest)

1. Have your friend create their own:
   - GitHub account
   - Hosting account (Netlify/GitHub Pages)
   - Domain registration

2. Send them these files (zip them up)

3. Walk them through the deployment steps

**Pros:** They own everything from day one, no transfer needed

### Method 2: Create & Transfer

1. Create a GitHub repository with these files
2. Go to **Settings** → **General** → scroll to "Danger Zone"
3. Click **Transfer ownership**
4. Enter their GitHub username
5. They accept the transfer

For domain: Most registrars have a "change registrant" or "transfer" option.

### Method 3: Add as Collaborator (Temporary Shared Access)

1. In GitHub repo: **Settings** → **Collaborators**
2. Add their GitHub username
3. They can now edit and manage the site
4. Later, transfer full ownership when ready

---

## ✏️ Making Changes

### Updating Business Info

All business information is in `index.html`. Search for these to update:

- **Phone:** Search for `773-451-6767`
- **Address:** Search for `5543 Babette Ct`
- **Hours:** Search for `24 hours`
- **Service area cities:** In the contact section

### Adding Real Photos

Replace the placeholder in the About section by:

1. Add images to the folder (e.g., `images/team.jpg`)
2. In `index.html`, replace the `.about-image-placeholder` div with:
```html
<img src="images/team.jpg" alt="Drain Flow team" class="about-img">
```

### Updating Reviews

In `index.html`, find the `.review-card` sections and update the text.

---

## 📱 Features

- ✅ Mobile responsive design
- ✅ Click-to-call phone links
- ✅ SEO-optimized meta tags
- ✅ Fast loading (no frameworks, pure HTML/CSS)
- ✅ Professional, modern design
- ✅ 24/7 emergency service emphasis
- ✅ Google reviews integration link

---

## 💰 Total Cost Summary

| Item | Cost |
|------|------|
| Hosting (GitHub Pages/Netlify/Cloudflare) | **FREE** |
| Domain name | ~$10-15/year |
| **Total** | **~$10-15/year** |

---

## 🆘 Need Help?

If your friend needs help maintaining the site later:
- GitHub has great documentation at [docs.github.com](https://docs.github.com)
- Netlify has tutorials at [docs.netlify.com](https://docs.netlify.com)
- Or they can hire a local web developer for updates


