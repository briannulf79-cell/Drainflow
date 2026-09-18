src = open('/home/monster-pc/projects/drainflow/services.html').read()
swap = {
    '⚡': 'images/icons/icon-hydro-jetting.png',
    '🐍': 'images/icons/icon-power-rodding-and-snaking.png',
    '🔧': 'images/icons/icon-sewer-line-repair.png',
    '📹': 'images/icons/icon-camera-inspection.png',
    '🛡️': 'images/icons/icon-preventive-maintenance.png',
    '🚨': 'images/icons/icon-emergency-backup-defense.png',
}
for emoji, path in swap.items():
    src = src.replace(f'<div class="service-icon">{emoji}</div>',
                      f'<div class="service-icon"><img src="{path}" alt=""></div>')
style = ('<style>\n.service-icon img { width: 48px; height: 48px; display: block; }\n'
         '.preview-banner { background:#22cc00; color:#06110a; text-align:center; padding:8px; font-weight:700; }\n'
         '</style>')
src = src.replace('</head>', style + '</head>')
banner = '<div class="preview-banner">PREVIEW — new service icons (not live)</div>'
src = src.replace('<body>', '<body>' + banner, 1)
src = src.replace('<title>', '<title>[PREVIEW] ', 1)
open('/home/monster-pc/projects/drainflow/icon-preview-services.html', 'w').write(src)
print('written', len(src))
