// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

/**
 * L'adresse publique du site. Elle sert aux URL canoniques, au sitemap et
 * surtout aux `og:image` — qui doivent etre ABSOLUES : une carte de partage
 * pointant vers un domaine qui ne repond pas ne s'affiche pas sur WhatsApp.
 *
 * D'ou ces trois niveaux, du plus explicite au plus general :
 *
 * 1. `SITE_URL` — a definir a la main si besoin de forcer une adresse.
 * 2. `VERCEL_PROJECT_PRODUCTION_URL` — fourni par Vercel. Il vaut le domaine
 *    `*.vercel.app` tant qu'aucun domaine personnalise n'est rattache, puis
 *    bascule tout seul sur le domaine des qu'il l'est. C'est ce qui permet de
 *    deployer AVANT que dekkandoo.com soit enregistre, sans rien casser et sans
 *    avoir a repasser derriere.
 * 3. `https://dekkandoo.com` — le repli, utilise en construction locale.
 */
const site =
  process.env.SITE_URL ||
  (process.env.VERCEL_PROJECT_PRODUCTION_URL
    ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
    : 'https://dekkandoo.com');

// Tailwind est configure dans postcss.config.mjs — voir le commentaire qui s'y trouve.
export default defineConfig({
  site,
  integrations: [sitemap()],
});
