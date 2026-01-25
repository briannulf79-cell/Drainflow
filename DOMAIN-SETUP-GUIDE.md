# 🌐 How to Get and Connect Your Domain Name

## A Step-by-Step Guide for Drain Flow Sewer and Plumbing

This guide will walk you through purchasing a domain name (like `drainflowplumbing.com`) and connecting it to your free GitHub Pages website.

---

## Step 1: Choose Your Domain Name

**Recommended domain names to check:**
- `drainflowplumbing.com`
- `drainflowsewer.com`  
- `drainflowchicago.com`
- `drainflowil.com`

**Tips:**
- `.com` is the most trusted and memorable
- Keep it short and easy to spell
- Avoid hyphens if possible

---

## Step 2: Purchase Your Domain

### Option A: Namecheap (Recommended - ~$10-12/year)

1. Go to [namecheap.com](https://www.namecheap.com)
2. Search for your desired domain name
3. Click "Add to cart" if available
4. Create an account and complete purchase
5. **Important:** Turn OFF auto-renew for add-ons you don't need (like WhoisGuard is usually free though)

### Option B: Cloudflare (Cheapest - ~$9/year)

1. Go to [cloudflare.com](https://www.cloudflare.com)
2. Create a free account
3. Click "Domain Registration" → "Register Domain"
4. Search and purchase (Cloudflare sells at cost, no markup)

### Option C: Google Domains (Simple - ~$12/year)

1. Go to [domains.google.com](https://domains.google.com)
2. Search for your domain
3. Purchase with your Google account

---

## Step 3: Connect Your Domain to GitHub Pages

Once you have your domain, follow these steps:

### Part A: Configure GitHub Pages

1. Go to your GitHub repository
2. Click **Settings** (tab at the top)
3. Scroll down to **Pages** in the left sidebar
4. Under "Custom domain", enter your domain name (e.g., `drainflowplumbing.com`)
5. Click **Save**
6. Check the box for **"Enforce HTTPS"** (may take a few minutes to appear)

### Part B: Configure Your Domain's DNS

Go back to where you purchased your domain (Namecheap, Cloudflare, etc.) and update the DNS settings:

#### For an Apex Domain (drainflowplumbing.com):

Add these **A Records** pointing to GitHub's servers:

| Type | Host | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

#### For www subdomain (www.drainflowplumbing.com):

Add this **CNAME Record**:

| Type | Host | Value |
|------|------|-------|
| CNAME | www | YOUR-GITHUB-USERNAME.github.io |

Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username.

---

## Step 4: Wait for DNS to Propagate

- DNS changes can take **15 minutes to 48 hours** to fully work
- Usually it's much faster (15-30 minutes)
- You can check status at [dnschecker.org](https://dnschecker.org)

---

## Step 5: Verify Everything Works

1. Go to your domain in a web browser
2. Make sure it loads your website
3. Check that the URL shows `https://` (secure)
4. Try both `drainflowplumbing.com` and `www.drainflowplumbing.com`

---

## 🎉 You're Done!

Your website is now live at your custom domain!

---

## Troubleshooting

### "Site not found" or "DNS not configured"
- Wait longer (DNS can take up to 48 hours)
- Double-check DNS records are entered correctly
- Make sure there are no typos

### "Not Secure" warning
- In GitHub Pages settings, make sure "Enforce HTTPS" is checked
- Wait 15-30 minutes for the SSL certificate to be issued

### Website shows wrong content
- Make sure the CNAME file in your repository contains your domain name
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)

---

## Need Help?

- **GitHub Pages Documentation:** [docs.github.com/pages](https://docs.github.com/en/pages)
- **Namecheap DNS Help:** [namecheap.com/support](https://www.namecheap.com/support/)
- **Cloudflare DNS Help:** [developers.cloudflare.com/dns](https://developers.cloudflare.com/dns/)

---

## Quick Reference Card

| What | Where |
|------|-------|
| Your website files | GitHub repository |
| GitHub Pages settings | Repository → Settings → Pages |
| Domain DNS settings | Your domain registrar (Namecheap, Cloudflare, etc.) |
| GitHub's IP addresses | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |

---

*This guide was created for Drain Flow Sewer and Plumbing. Good luck with your new website!* 🔧


