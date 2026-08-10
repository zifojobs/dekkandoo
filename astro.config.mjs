// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// site : indispensable pour des URL canoniques et un sitemap absolus.
// Le domaine est commande chez wanekoo.sn mais PAS ENCORE ENREGISTRE au registre
// .com (RDAP 404 au 10/08). Verifier avant la mise en ligne — cf. MESSAGES-2026-08-10.md.
// Tailwind est configure dans postcss.config.mjs — voir le commentaire qui s'y trouve.
export default defineConfig({
  site: 'https://dekkandoo.com',
  integrations: [sitemap()],
});
