# Site du Consortium Dëkkandoo

Site institutionnel du **Consortium Dëkkandoo** — ONG de santé communautaire, nutrition
infantile et autonomisation économique des femmes, basée à Saint-Louis (Sénégal).

Astro 6 · Tailwind 4 · statique · déployé sur Vercel.

## 🔴 Ce dépôt est public — ce qu'il ne doit jamais contenir

Le Consortium détient un registre de plusieurs centaines de femmes bénéficiaires, avec
**numéros de CNI et téléphones**. Ces fichiers vivent dans le dossier **parent** de ce dépôt
et n'en font délibérément pas partie. Il en va de même pour les photos originales, les
rapports bailleurs et les documents commerciaux.

**Règle : ce dépôt ne contient que ce qui est déjà servi publiquement par le site.**

## Démarrer

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # génère dist/
```

## Les images

Les photos servies par le site sont des **WebP dérivées**, produites par
`scripts/gen_photos_site.py` à partir des originaux du client, qui se trouvent **hors du
dépôt** (`../img/`). Le script écrit `public/photos/` et `src/photos.json` — ce dernier
portant l'`alt` et les dimensions exactes de chaque variante, pour que chaque `<img>` réserve
sa place et ne fasse pas sauter la mise en page.

```bash
python scripts/gen_photos_site.py    # photos du site
python scripts/gen_partage.py        # carte Open Graph
```

⚠️ Sans les originaux, ces scripts ne tournent pas — c'est voulu. Les WebP déjà produites
sont versionnées, le site se construit donc sans eux.

## Choix à ne pas défaire sans raison

- **Aucune police téléchargée.** Les polices sont celles présentes sur les appareils (serif
  Palatino/Georgia, mono Consolas), conformément à la maquette validée par le client.
- **Un seul thème, le clair.** La maquette embarquait une variante sombre automatique :
  écartée, beaucoup de téléphones Android sont en mode sombre par défaut et le client verrait
  une version qu'il n'a pas validée.
- **Tailwind passe par PostCSS**, pas par `@tailwindcss/vite` : ce dernier est incompatible
  avec le moteur rolldown de Vite 8 embarqué par Astro 6. Voir `postcss.config.mjs`.
- **L'animation d'apparition est conditionnée à la classe `js`** posée sur `<html>`. Écrire
  `.revele { opacity: 0 }` directement rendrait le site blanc sans JavaScript.
- **Les réseaux sociaux ont une source unique** (`src/reseaux.ts`). Le TikTok indiqué dans les
  documents de cadrage était erroné — un profil social se vérifie sur **l'identité affichée**,
  jamais sur le code HTTP : TikTok répond 200 sur un compte inexistant.

## Contenu

Textes, chiffres et formulations proviennent de la maquette validée par le client, de ses
documents et de la presse (Sud Quotidien, 28/02/2026). **Aucun chiffre n'est estimé.**
Les actualités marquées `aValider` dans `src/actualites.ts` n'ont pas encore été relues par
le Consortium.
