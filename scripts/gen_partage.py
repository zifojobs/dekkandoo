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
FOREST = (31, 81, 56)      # --color-forest
PAPER = (244, 246, 241)    # --color-paper
GOLD = (200, 143, 34)      # --color-gold

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
d.text((72, 306), "Santé  ·  Nutrition  ·  Autonomisation", font=mono(25), fill=(160, 195, 175))

d.line([(72, 372), (330, 372)], fill=GOLD, width=3)

# LE chiffre. Un seul, celui qui situe l'organisation sur un territoire — c'est
# ce qu'un bailleur reconnait.
d.text((72, 410), "6", font=mono(96), fill=GOLD)
d.text((176, 432), "communes du département", font=serif(38), fill=PAPER)
d.text((176, 484), "de Saint-Louis, Sénégal", font=serif(38), fill=PAPER)

d.text((72, 556), "dekkandoo.com", font=mono(24), fill=(160, 195, 175))

img.save(str(RACINE / "public" / "partage.png"), optimize=True)
print(str(RACINE / "public" / "partage.png"), img.size)
