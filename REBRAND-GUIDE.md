# 🛡️ Drain Flow - Mascot Rebrand Guide

**Branch:** `feature/mascot-rebrand`  
**Status:** Ready for preview

---

## 🎨 What's Changed

I've rebranded the website to match your friend's awesome "Drain Warrior" mascot aesthetic:

### Visual Updates:
- **New Color Scheme:** Green/blue armor colors matching the mascot (neon green accents, deep blues, metallic touches)
- **Hero Section:** "Defending Your Drains. One Pipe at a Time." with drain warrior theme
- **About Section:** The empty photo placeholder now looks intentional — styled like a shield/badge with "Father & Son Drain Defense Force" text
- **Services:** Renamed to "Our Drain-Fighting Arsenal" with themed icons and descriptions
- **Hover Effects:** Service cards now glow with neon green on hover

### What Still Needs Images:
The mascot images your friend created should be added to make this really pop:

1. **Logo (Shield Crest)** → Replace `images/logo.jpg` with the DF shield image
2. **Hero Mascot** → Add as `images/mascot-hero.png` (the main drain warrior with hose/shield)
3. **About Section** → Optionally add `images/dwayne-and-son.jpg` if they want to add a real photo later

---

## 📸 How to Add the Mascot Images

### Step 1: Save the Images
Save these files to the `images/` folder:
- `mascot-hero.png` - The main drain warrior (for hero section)
- `shield-crest.png` - The DF shield logo (to replace logo.jpg)
- Any other mascot variations you want to use

### Step 2: Update the Logo
In `index.html`, the logo currently references `images/logo.jpg`. Replace that file with the shield crest, or update the HTML:
```html
<img src="images/shield-crest.png" alt="Drain Flow Shield Logo" class="logo-img">
```

### Step 3: Add Mascot to Hero (Optional)
To add the mascot image to the hero section, add this after the hero content:
```html
<div class="hero-mascot-image">
    <img src="images/mascot-hero.png" alt="Drain Flow Mascot" class="mascot-img">
</div>
```

And add this CSS to `styles.css`:
```css
.hero-mascot-image {
    position: absolute;
    right: 5%;
    bottom: 10%;
    width: 300px;
    opacity: 0.9;
    z-index: 1;
}

.mascot-img {
    width: 100%;
    filter: drop-shadow(0 0 30px rgba(57, 255, 20, 0.3));
}
```

---

## 👁️ How to Preview

### Option 1: GitHub Pages (Private Branch Preview)
Since this is on a feature branch, you can:
1. Go to repo Settings → Pages
2. Change source from `main` to `feature/mascot-rebrand`
3. GitHub will deploy it to: `https://briannulf79-cell.github.io/Drainflow/`
4. Share the URL with your friend for feedback
5. **Don't forget to switch back to `main` after!**

### Option 2: Netlify Drop (Easiest for Private Sharing)
1. Download/zip the `drainflow-rebrand` folder
2. Go to [netlify.com/drop](https://app.netlify.com/drop)
3. Drag and drop the folder
4. Netlify gives you a private preview URL (like `random-name.netlify.app`)
5. Share that URL with your friend

### Option 3: Local Preview
1. Open `index.html` in your browser
2. Or use VS Code Live Server extension for hot reload

---

## 🚀 Next Steps

1. **Preview the site** using one of the methods above
2. **Add the mascot images** your friend created
3. **Get feedback** from your friend
4. **Iterate** — I can make more changes based on what he likes
5. **Merge to main** when ready to go live

---

## 📝 Files Modified

- `index.html` - Updated copy and theme
- `styles.css` - New color scheme, mascot-themed styling
- `REBRAND-GUIDE.md` - This file

**Branch:** `feature/mascot-rebrand`  
**Not pushed yet** — waiting for your approval

---

## 💡 Design Notes

The rebrand leans into the superhero/drain warrior aesthetic:
- **Colors:** Neon green (energy glow), deep blue (armor), metallic silver (industrial)
- **Theme:** "Drain Defense Force" — positioning Dwayne & Son as heroes who battle clogs
- **Vibe:** Fun but professional — the mascot makes it memorable without being cheesy

The empty photo placeholder in the About section now looks like an intentional design element (shield/badge style) instead of a missing image. When your friend is ready to add a real photo of him and his son, we can easily swap it in.

---

**Questions?** Just ask! I can tweak colors, copy, layout, or add the actual mascot images wherever you want them.
