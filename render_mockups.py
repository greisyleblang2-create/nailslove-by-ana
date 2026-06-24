#!/usr/bin/env python3
# Render LEBLANG Automatisierung brand mockups (Option 1: Taupe & Kohle) to PNG.
import base64, os, cairosvg

CREAM="#EFEAE1"; KOHLE="#38352F"; TAUPE="#9E8467"
FONT="Liberation Sans"
OUT="/home/user/nailslove-by-ana/previews"
os.makedirs(OUT, exist_ok=True)

def b64(path):
    with open(path,"rb") as f:
        return "data:image/jpeg;base64,"+base64.b64encode(f.read()).decode()

HERO=b64("/home/user/nailslove-by-ana/hero.jpg")
LINKEDIN=b64("/home/user/nailslove-by-ana/linkedin.jpg")

def logo(tx,ty,scale,box_fill,box_stroke,w1col,w2col,words=True):
    g=[f'<g transform="translate({tx},{ty}) scale({scale})">']
    # boxes
    g.append(f'<g fill="{box_fill}" stroke="{box_stroke}" stroke-width="4">')
    for y in (18,61.5,105):
        g.append(f'<rect x="28" y="{y}" width="40" height="22" rx="6"/>')
    g.append('</g>')
    # thread
    g.append(f'<g stroke="{TAUPE}" stroke-width="3.5" fill="none" stroke-linecap="round">')
    g.append('<line x1="6" y1="29" x2="24.5" y2="29"/>')
    g.append('<path d="M71.5 29 A13 21.75 0 0 1 71.5 72.5"/>')
    g.append('<path d="M24.5 72.5 A13 21.75 0 0 0 24.5 116"/>')
    g.append('<line x1="71.5" y1="116" x2="461" y2="116"/>')
    g.append('</g>')
    g.append(f'<polygon points="461,111.5 461,120.5 470,116" fill="{TAUPE}"/>')
    if words:
        g.append(f'<text x="98" y="50" font-family="{FONT}" font-size="44" font-weight="bold" letter-spacing="0.5" fill="{w1col}">LEBLANG</text>')
        g.append(f'<text x="98" y="96" font-family="{FONT}" font-size="44" font-weight="bold" fill="{w2col}" textLength="372" lengthAdjust="spacing">Automatisierung</text>')
    g.append('</g>')
    return "".join(g)

def T(x,y,s,size,fill,weight="normal",ls=None,anchor="start",opacity=None):
    s=s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    a=f' letter-spacing="{ls}"' if ls else ""
    o=f' fill-opacity="{opacity}"' if opacity else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{a}{o}>{s}</text>')

def render(name,w,h,body):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
    cairosvg.svg2png(bytestring=svg.encode(),write_to=f"{OUT}/{name}.png",output_width=w,output_height=h)
    print("rendered",name,f"{w}x{h}")

# ---------- SLIDE 1 — Web Hero 1440x720 ----------
b=[f'<rect width="1440" height="720" fill="{CREAM}"/>']
b.append(f'<image x="700" y="0" width="740" height="720" href="{HERO}" preserveAspectRatio="xMidYMid slice"/>')
# nav bar over everything
b.append(f'<rect x="0" y="0" width="1440" height="70" fill="{CREAM}"/>')
b.append(f'<rect x="0" y="69" width="1440" height="1" fill="{KOHLE}" fill-opacity="0.12"/>')
b.append(logo(64,7,170/484,CREAM,KOHLE,TAUPE,KOHLE))
b.append(T(980,45,"Leistungen",14,KOHLE))
b.append(T(1086,45,"Über uns",14,KOHLE))
b.append(T(1172,45,"Referenzen",14,KOHLE))
b.append(f'<rect x="1270" y="22" width="106" height="34" rx="5" fill="{TAUPE}"/>')
b.append(T(1323,44,"Anfrage stellen",13,CREAM,anchor="middle"))
# left content
b.append(T(72,232,"PROZESSAUTOMATISIERUNG · MÜNCHEN",12,TAUPE,ls="3"))
b.append(T(72,300,"Mehr Zeit für das,",58,KOHLE,weight="bold"))
b.append(T(72,362,"was wirklich zählt.",58,KOHLE,weight="bold"))
b.append(T(72,410,"Wir automatisieren Ihre wiederkehrenden",18,KOHLE,opacity="0.6"))
b.append(T(72,436,"Prozesse — damit Sie sich auf das",18,KOHLE,opacity="0.6"))
b.append(T(72,462,"Wesentliche konzentrieren können.",18,KOHLE,opacity="0.6"))
b.append(f'<rect x="72" y="500" width="200" height="52" rx="6" fill="{KOHLE}"/>')
b.append(T(172,532,"Kostenlos beraten",14,CREAM,anchor="middle"))
b.append(T(296,532,"Mehr erfahren →",14,TAUPE))
b.append(f'<rect x="72" y="600" width="556" height="1" fill="{KOHLE}" fill-opacity="0.1"/>')
trust=[("50+","PROJEKTE"),("30%","ZEITERSPARNIS Ø"),("5,0","BEWERTUNG")]
tx=72
for num,lab in trust:
    b.append(T(tx,656,num,26,KOHLE,weight="bold"))
    b.append(T(tx,678,lab,11,KOHLE,ls="1",opacity="0.5"))
    tx+=190
render("1_web_hero",1440,720,"".join(b))

# ---------- SLIDE 2 — Visitenkarte Vorderseite 850x480 ----------
b=[f'<rect width="850" height="480" fill="{CREAM}"/>']
b.append(f'<rect x="650" y="0" width="200" height="480" fill="{TAUPE}"/>')
b.append(logo(56,70,230/484,CREAM,KOHLE,TAUPE,KOHLE))
b.append(T(56,230,"Greisyle Leblang",22,KOHLE,weight="bold"))
b.append(T(56,254,"GRÜNDERIN & AUTOMATISIERUNGSEXPERTIN",11,TAUPE,ls="1"))
b.append(T(56,300,"greisyle@leblang-automatisierung.de",13,KOHLE,opacity="0.65"))
b.append(T(56,324,"+49 89 123 456 789",13,KOHLE,opacity="0.65"))
b.append(T(56,348,"leblang-automatisierung.de",13,KOHLE,opacity="0.65"))
b.append(f'<text x="750" y="240" font-family="{FONT}" font-size="11" fill="{CREAM}" fill-opacity="0.9" text-anchor="middle" letter-spacing="3" transform="rotate(-90 750 240)">PROZESSE AUTOMATISIEREN. ZEIT GEWINNEN.</text>')
render("2_visitenkarte_vorne",850,480,"".join(b))

# ---------- SLIDE 3 — Visitenkarte Rückseite 850x480 ----------
b=[f'<rect width="850" height="480" fill="{KOHLE}"/>']
b.append(logo((850-320)/2,150,320/484,"#EFEAE11F",TAUPE,TAUPE,CREAM))
b.append(T(425,330,"PROZESSE AUTOMATISIEREN. ZEIT GEWINNEN.",11,CREAM,ls="4",anchor="middle",opacity="0.4"))
render("3_visitenkarte_hinten",850,480,"".join(b))

# ---------- SLIDE 4 — LinkedIn Banner 1584x396 ----------
b=[f'<rect width="1584" height="396" fill="{CREAM}"/>']
b.append(f'<image x="960" y="0" width="624" height="396" href="{LINKEDIN}" preserveAspectRatio="xMidYMid slice"/>')
b.append(f'<polygon points="940,0 1000,0 1000,396 880,396" fill="{CREAM}"/>')
b.append(logo(72,40,220/484,CREAM,KOHLE,TAUPE,KOHLE))
b.append(T(72,200,"Deine Zeit ist zu wertvoll",38,KOHLE,weight="bold"))
b.append(T(72,244,"für manuelle Prozesse.",38,KOHLE,weight="bold"))
b.append(T(72,295,"Automatisierungslösungen für kleine und mittlere Unternehmen · München",15,KOHLE,opacity="0.55"))
render("4_linkedin_banner",1584,396,"".join(b))

# ---------- SLIDE 5 — Instagram Post 1080x1080 ----------
b=[f'<rect width="1080" height="1080" fill="{CREAM}"/>']
b.append(logo(80,72,220/484,CREAM,KOHLE,TAUPE,KOHLE))
b.append(T(1000,108,"MÜNCHEN · DE",11,KOHLE,ls="2",anchor="end",opacity="0.4"))
b.append(f'<rect x="80" y="438" width="52" height="4" rx="2" fill="{TAUPE}"/>')
b.append(T(80,540,"Automatisierung",74,KOHLE,weight="bold"))
b.append(T(80,620,"leicht gemacht.",74,KOHLE,weight="bold"))
b.append(T(80,700,"Schluss mit manuellen Aufgaben. Wir bauen",20,KOHLE,opacity="0.58"))
b.append(T(80,730,"Ihnen Prozesse, die selbst laufen — sicher,",20,KOHLE,opacity="0.58"))
b.append(T(80,760,"schnell und skalierbar.",20,KOHLE,opacity="0.58"))
b.append(f'<rect x="0" y="984" width="1080" height="96" fill="{TAUPE}"/>')
b.append(T(80,1040,"PROZESSE AUTOMATISIEREN. ZEIT GEWINNEN.",14,CREAM,ls="2",opacity="0.9"))
b.append(f'<rect x="836" y="1012" width="164" height="40" rx="4" fill="none" stroke="{CREAM}" stroke-opacity="0.6" stroke-width="1.5"/>')
b.append(T(918,1038,"Jetzt anfragen →",14,CREAM,anchor="middle",opacity="0.9"))
render("5_instagram_post",1080,1080,"".join(b))

print("DONE ->", OUT)
