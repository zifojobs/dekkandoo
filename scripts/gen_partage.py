# -*- coding: utf-8 -*-
"""Genere site/public/partage.png — la carte affichee quand le lien du site circule.

C'est le levier n.1 identifie dans SEO-A-INTEGRER.md : le lien de Dekkandoo
circulera sur WhatsApp, d'un charge de programme a son collegue. Ce que voit le
destinataire, c'est cette carte — pas un resultat Google.

Regle appliquee : elle porte LE LOGO ET UN CHIFFRE, jamais une photo decorative.
Palette et polices identiques au site (Palatino en serif, Consolas en chasse fixe,
les memes que --font-serif et --font-mono de global.css).
"""
import pathlib
# Chemins calcules depuis l'emplacement du script : il tourne indifferemment
# depuis la racine du depot ou depuis scripts/.
RACINE = pathlib.Path(__file__).resolve().parent.parent      # .../site
SOURCES = RACINE.parent / "img"   # HORS DEPOT — photos originales du client
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
FOREST = (22, 90, 45)      # --color-forest — recale sur la teinte du logo le 11/08
PAPER = (244, 246, 241)    # --color-paper
MUET = (160, 195, 175)     # sur-titres et domaine, sur le vert

# L'OR A DISPARU DE CETTE CARTE, et il fallait le faire : il avait ete ecarte du
# site le 11/08 au motif qu'il n'appartient a aucune des deux couleurs de la
# marque. La carte, elle, le portait encore — c'est-a-dire l'image meme qui
# circule sur WhatsApp, la premiere chose qu'un charge de programme voit du
# Consortium. Il mesurait en plus 2,92 de contraste sur le vert.
#
# Ce qui le remplace suit la regle ecrite dans global.css : sur un fond SOMBRE,
# pas d'accent colore, on passe au creme. Le « 6 » ne perd rien — c'est sa
# taille qui le fait lire, pas sa couleur.

F = "C:/Windows/Fonts/"
serif = lambda s: ImageFont.truetype(F + "pala.ttf", s)
serif_g = lambda s: ImageFont.truetype(F + "palab.ttf", s)
mono = lambda s: ImageFont.truetype(F + "consola.ttf", s)

img = Image.new("RGB", (W, H), FOREST)
d = ImageDraw.Draw(img)

# Meme motif vegetal que le heros du site, dessine a la main : une feuille
# repetee en grille. Tres discret (alpha ~ 10 %), il donne la texture sans
# jamais concurrencer le texte.
motif = Image.new("RGBA", (W, H), (0, 0, 0, 0))
md = ImageDraw.Draw(motif)
for y in range(-30, H + 120, 150):
    for x in range(-30, W + 120, 150):
        md.ellipse([x, y, x + 66, y + 108], outline=(255, 255, 255, 26), width=3)
        md.line([x + 33, y + 54, x + 33, y + 150], fill=(255, 255, 255, 20), width=3)
img = Image.alpha_composite(img.convert("RGBA"), motif).convert("RGB")
d = ImageDraw.Draw(img)

# Logo en version blanche : le fond est vert profond.
logo = Image.open(str(RACINE / "public" / "logo" / "logo-dekkandoo-blanc-512.png")).convert("RGBA")
ratio = 108 / logo.height
logo = logo.resize((round(logo.width * ratio), 108), Image.LANCZOS)
img.paste(logo, (72, 68), logo)

d.text((72, 232), "CONSORTIUM DËKKANDOO", font=serif_g(58), fill=PAPER)
d.text((72, 306), "Santé  ·  Nutrition  ·  Autonomisation", font=mono(25), fill=MUET)

d.line([(72, 372), (330, 372)], fill=MUET, width=3)

# LE chiffre. Un seul, celui qui situe l'organisation sur un territoire — c'est
# ce qu'un bailleur reconnait.
d.text((72, 410), "6", font=mono(96), fill=PAPER)
d.text((176, 432), "communes du département", font=serif(38), fill=PAPER)
d.text((176, 484), "de Saint-Louis, Sénégal", font=serif(38), fill=PAPER)

d.text((72, 556), "dekkandoo.com", font=mono(24), fill=MUET)

img.save(str(RACINE / "public" / "partage.png"), optimize=True)
print(str(RACINE / "public" / "partage.png"), img.size)


# --------------------------------------------------------------------------
# Cartes de partage des actualites — une par article.
#
# Meme raison que la carte du site : le lien circulera sur WhatsApp, et c'est
# la carte qui se voit avant le texte. Ici la photo de l'article sert de fond,
# avec un voile vert qui monte du bas pour porter le titre : le texte ne repose
# jamais sur une zone claire de l'image.
#
# Les titres sont LUS dans src/actualites.ts plutot que recopies ici : deux
# copies d'un meme titre finissent toujours par diverger.
# --------------------------------------------------------------------------
import json
import re

ts = (RACINE / "src" / "actualites.ts").read_text(encoding="utf-8")
articles = list(zip(re.findall(r"slug:\s*'([^']+)'", ts),
                    re.findall(r"titre:\s*'([^']+)'", ts),
                    re.findall(r"photo:\s*'([^']+)'", ts),
                    re.findall(r"date:\s*'([^']+)'", ts)))
assert articles, "aucune actualite lue dans actualites.ts"

manifeste = json.loads((RACINE / "src" / "photos.json").read_text(encoding="utf-8"))
dossier = RACINE / "public" / "partage"
dossier.mkdir(exist_ok=True)


def coupe(d, texte, font, largeur):
    """Retourne les lignes de `texte` tenant dans `largeur`."""
    lignes, courante = [], ""
    for mot in texte.split():
        essai = f"{courante} {mot}".strip()
        if d.textlength(essai, font=font) <= largeur:
            courante = essai
        else:
            lignes.append(courante)
            courante = mot
    if courante:
        lignes.append(courante)
    return lignes


for slug, titre, cle, date in articles:
    src = RACINE / "public" / manifeste[cle]["variantes"][0]["url"].lstrip("/")
    fond = Image.open(src).convert("RGB")

    # Recadrage centre au format 1200x630, apres mise a l'echelle par le cote
    # le plus contraignant — l'equivalent de object-fit: cover.
    e = max(W / fond.width, H / fond.height)
    fond = fond.resize((round(fond.width * e), round(fond.height * e)), Image.LANCZOS)
    g = (fond.width - W) // 2
    h = round((fond.height - H) * 0.30)   # legerement vers le haut : les visages
    carte = fond.crop((g, h, g + W, h + H))

    # Voile vert montant du bas. Il doit devenir OPAQUE bien avant le texte :
    # une premiere version s'arretait a mi-hauteur et le titre se posait sur un
    # cheque blanc — illisible. La zone de texte se lit donc sur du vert plein,
    # jamais sur l'image, meme si la photo est claire a cet endroit.
    voile = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(voile)
    for y in range(H):
        t = min(1.0, max(0.0, (y - H * 0.10) / (H * 0.42)))
        vd.line([(0, y), (W, y)], fill=FOREST + (int(255 * t ** 1.2),))
    carte = Image.alpha_composite(carte.convert("RGBA"), voile).convert("RGB")

    d = ImageDraw.Draw(carte)
    logo = Image.open(RACINE / "public" / "logo" / "logo-dekkandoo-blanc-512.png").convert("RGBA")
    r = 62 / logo.height
    logo = logo.resize((round(logo.width * r), 62), Image.LANCZOS)
    carte.paste(logo, (64, 42), logo)

    lignes = coupe(d, titre, serif_g(50), W - 128)[:3]
    y = H - 78 - len(lignes) * 62
    d.text((64, y - 46), date.upper(), font=mono(22), fill=MUET)
    for ligne in lignes:
        d.text((64, y), ligne, font=serif_g(50), fill=PAPER)
        y += 62

    carte.save(dossier / f"{slug}.png", optimize=True)
    print("partage/" + slug + ".png")
