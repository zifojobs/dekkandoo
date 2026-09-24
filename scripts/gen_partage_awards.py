# -*- coding: utf-8 -*-
"""Carte de partage de la page /ndieumbeutt-awards/ (24/09).

Le logo de l'evenement est pris dans le film officiel (image a 4 s,
public/awards/film-affiche.jpg), recadre sur le logo, pose sur le noir du film.
Sous le logo : la date et le lieu, ce que le destinataire WhatsApp doit lire
avant meme d'ouvrir le lien. Polices identiques a gen_partage.py.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

RACINE = pathlib.Path(__file__).resolve().parent.parent
W, H = 1200, 630
PAPER = (244, 246, 241)
MUET = (170, 190, 178)
F = "C:/Windows/Fonts/"

img = Image.new("RGB", (W, H), (0, 0, 0))
affiche = Image.open(RACINE / "public" / "awards" / "film-affiche.jpg").convert("RGB")
logo = affiche.crop((84, 100, 1232, 580))           # boite d'encre mesuree : x 104-1212, y 119-561
e = 860 / logo.width
logo = logo.resize((860, round(logo.height * e)), Image.LANCZOS)
img.paste(logo, ((W - 860) // 2, 60))

d = ImageDraw.Draw(img)
def centre(y, texte, font, fill):
    d.text(((W - d.textlength(texte, font=font)) / 2, y), texte, font=font, fill=fill)
centre(500, "JEUDI 17 DÉCEMBRE 2026  ·  RAO", ImageFont.truetype(F + "consola.ttf", 34), PAPER)
centre(556, "Consortium Dëkkandoo & E4Y  —  dekkandoo.com", ImageFont.truetype(F + "pala.ttf", 28), MUET)

out = RACINE / "public" / "partage" / "ndieumbeutt-awards.png"
img.save(out, optimize=True)
print(out, img.size)
