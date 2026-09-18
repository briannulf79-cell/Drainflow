# DRAIN FLOW SERVICE ICONS — SESSION STATE (2026-09-18)

Authoritative resume doc. Status: **approved direction, NOT yet live.**

## What's done
- 6 generative shield emblems (Rambo, via ChatGPT image gen) received as phone screenshots,
  cropped + white-knocked-out, saved at 2x retina:
  `images/icons/icon-{hydro-jetting,power-rodding-and-snaking,sewer-line-repair,camera-inspection,preventive-maintenance,emergency-backup-defense}.png`
- Mapping (services.html): ⚡hydro 🐍rodding 🔧sewer-repair 📹camera 🛡️clean-out-station 🚨emergency.
  `preventive-maintenance.png` is actually used for Clean Out Station (pipe junction + check fits).
- Tile size spec: artwork renders **48×48px** inside ~84px tile (`.service-icon`, 3rem emoji box).
  Source images ≥512px, 2x (96px+) versions kept for retina.
- Preview page live & Brian-approved look: **https://drainflowpro.com/icon-preview-services.html**
  (unlinked page on GitHub Pages repo briannulf79-cell/Drainflow, main pages untouched,
  green PREVIEW banner at top). Pushed via SSH remote (https token lacks push).
- Local files also at `~/projects/drainflow/images/icons/`; processing scripts saved in `tools/`
  (icons_pipeline.py = crop→knockout→tile-render for all 6; make_preview.py = services.html swap).

## Pending / next session
0c. **DONE (same day, per ChatGPT-suggested plan):** (1) Hydro Jetting v2 — Rambo's revised badge
   (viewed down the pipe mouth, nozzle inside, matches camera badge composition) found in
   ~/.hermes/cache/images/img_956569f87afb.jpg (1254x1254, sent 22:58 Sep 17), processed via
   icons_pipeline.process() → images/icons/icon-hydro-jetting-v2.png at 320x320 transparent.
   NEW FILENAME (cache-bust); preview page references -v2; old side-view PNG kept for reference.
   (2) Rooter mascot mobile-first: width clamp(220px,72vw,300px) default, clamp(260px,24vw,360px)
   at ≥769px, centered, header gap 48→24px, mobile header stacks at ≤768px breakpoint now.
   Verified live: hydroV2 loads (natural 320), mascot 307px @1440 / 281px @390. Commit 256fdf7.
0b. **DONE (same day):** Full-Detail Arsenal icons now fixed 80x80 desktop / 64x64 mobile —
   84px/68px `.service-icon` wrapper (padding 0, box-sizing border-box, flex-centered),
   img fills wrapper with width/height 100% + object-fit:contain. Old 48px rule removed.
   Verified: DOM measures all six img = 80px in 84px tile (mobile 64px), alpha-scan of all 6 PNGs
   shows uniform ~92% fill (6-7px side margins) so visual size is consistent — no re-crop needed.
   Live on preview (5946d93).
0. **DONE (same day):** preview-page refactored per Brian's plan — Flood Prevention section is now a
   full-width header row (heading+copy left, Rooter mascot right, decorative) with an independent
   full-width 2x2 service grid below (80px icon tiles desktop / 64px mobile; emoji placeholders
   sized ready for custom artwork swap). Verified desktop+mobile screenshots, pushed to live/main
   (0c9332b) and confirmed live. Full-Detail Arsenal layout untouched; live services.html untouched.
1. **Brian has a REFACTORING PLAN for the preview page** — get it first, apply before any live swap.
2. Rambo may replace the hydro-jetting emblem (he's remaking it; remade image sent but not yet processed).
3. Brian said there are **4 more emoji needing swapped** (likely on other pages — grep all pages for
   emoji in icon boxes; home page has the same six service icons).
4. ChatGPT (Rambo's generator) got the 48px design brief: ONE bold subject, ~8 shapes max, no
   thin lines/text, transparent PNG ≥512px, match shield style family.
5. When approved: swap icons into real services.html + index.html (and any other pages), rebuild
   (`python3 build.py` from _pages/_partials if partials changed), remove preview page from repo,
   show Brian before final push.

## Environment facts
- trycloudflare quick tunnels BROKEN from Monster PC (edge-404, verified 3 URLs + http2/quic + GX10).
- Temp/preview links: use Brian's BUSINESS Cloudflare or GitHub Pages; NEVER Rambo's Cloudflare account.
- gh token can't create repos; SSH remote git@github.com works for pushes.
- drainflow_api_token reads drainflowpro.com zone, no Pages perm.
