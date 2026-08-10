# -*- coding: utf-8 -*-
"""Prepare les photos de terrain pour le site : JPEG Facebook -> WebP redimensionne.

Pourquoi : les 27 originaux pesent 8,8 Mo. Le public consulte depuis un telephone
Android sur reseau senegalais, et la regle n.5 du cahier de references est qu'aucun
effet ne vaut une page qui met huit secondes a s'afficher.

Deux largeurs par photo (1600 et 800) : le navigateur choisit via srcset. Les
dimensions exactes sont ecrites dans photos.json pour que chaque <img> porte son
width/height et ne fasse pas sauter la mise en page pendant le chargement.

Relancer apres tout ajout de photo :  python gen_photos_site.py
"""
import json
import os
import pathlib
# Chemins calcules depuis l'emplacement du script : il tourne indifferemment
# depuis la racine du depot ou depuis scripts/.
RACINE = pathlib.Path(__file__).resolve().parent.parent      # .../site
SOURCES = RACINE.parent / "img"   # HORS DEPOT — photos originales du client
from PIL import Image

SRC = str(SOURCES)
DST = str(RACINE / "public" / "photos")

# Le nom de fichier d'origine ne dit rien ; ce tableau est la seule trace de ce
# que montre chaque image. L'alt est ecrit d'apres ce qui est VISIBLE, sans
# affirmer un evenement invérifiable.
PHOTOS = [
    ("730381754_122185668656863069_4319426630476112951_n.jpg", "champ-equipe",
     "Membres du Consortium et productrices dans un champ maraîcher, récolte en cours"),
    ("733802301_122185668638863069_6257306046183209556_n.jpg", "champ-recolte",
     "Groupe de femmes et d'encadrants au milieu des cultures, bassines de récolte à la main"),
    ("734152439_122185668632863069_2813539541597187617_n.jpg", "recolte-tomates",
     "Deux productrices récoltant des tomates dans une parcelle maraîchère"),
    ("646549946_122169623588863069_6297091601554889768_n.jpg", "remise-poussins",
     "Cartons de poussins prêts pour la journée de remise aux bénéficiaires du projet Ndieumbeutt"),
    ("497634161_122105453972863069_6521396407542701227_n.jpg", "formation-femmes",
     "Session de formation : des femmes réunies autour des bassines de fabrication"),
    ("740334083_122186339258863069_5927519052001345340_n.jpg", "remise-financement",
     "Remise d'un financement de 3 000 000 FCFA à une association villageoise d'épargne et de crédit"),
    ("739231172_122186339096863069_770836326690210650_n.jpg", "beneficiaires-honorees",
     "Bénéficiaires mises à l'honneur lors de la cérémonie, écharpes remises"),
    ("659106565_122173021466863069_4926074023701701140_n.jpg", "remise-produits",
     "Bénéficiaires du projet Ndieumbeutt lors d'une remise de produits agricoles"),
    ("khaly.jpg", "khaly",
     "Abdou Khaly Mbodj, coordonnateur global du Consortium Dëkkandoo, s'adressant à la presse"),
]

# Recadrages avant redimensionnement, en fractions de l'image (gauche, haut,
# droite, bas). Sert quand une meme photo doit apparaitre a deux endroits : un
# cadrage serre donne une image distincte sans aller chercher un autre cliche,
# et sans rien affirmer que la photo ne montre pas.
CADRAGES = {
    # Le geste de travail — balance, gants, bassine — extrait de la scene de
    # formation qui occupe le heros.
    "formation-geste": ("497634161_122105453972863069_6521396407542701227_n.jpg",
                        (0.20, 0.38, 0.62, 0.86),
                        "Pesée et conditionnement pendant une session de formation"),
}
for cle, (fichier, _b, alt) in CADRAGES.items():
    PHOTOS.append((fichier, cle, alt))

# 2048 sert au plein cadre du heros sur grand ecran ; les originaux plus petits
# sont simplement ignores a cette largeur (on n'agrandit jamais).
LARGEURS = (2048, 1600, 800)

os.makedirs(DST, exist_ok=True)
manifeste = {}

for fichier, cle, alt in PHOTOS:
    im = Image.open(os.path.join(SRC, fichier)).convert("RGB")
    if cle in CADRAGES:
        g, h, d_, b = CADRAGES[cle][1]
        im = im.crop((round(g * im.width), round(h * im.height),
                      round(d_ * im.width), round(b * im.height)))
    variantes = []
    for w in LARGEURS:
        if w > im.width:          # ne jamais agrandir : ca ne cree que du poids
            continue
        h = round(im.height * w / im.width)
        sortie = f"{cle}-{w}.webp"
        im.resize((w, h), Image.LANCZOS).save(
            os.path.join(DST, sortie), "WEBP", quality=72, method=6
        )
        variantes.append({"url": f"/photos/{sortie}", "w": w, "h": h})
    manifeste[cle] = {"alt": alt, "variantes": variantes}

with open(str(RACINE / "src" / "photos.json"), "w", encoding="utf-8") as f:
    json.dump(manifeste, f, ensure_ascii=False, indent=2)

avant = sum(os.path.getsize(os.path.join(SRC, f)) for f, _, _ in PHOTOS)
apres = sum(os.path.getsize(os.path.join(DST, f)) for f in os.listdir(DST))
print(f"{len(PHOTOS)} photos -> {len(os.listdir(DST))} fichiers WebP")
print(f"{avant/1024/1024:.1f} Mo  ->  {apres/1024/1024:.1f} Mo")
