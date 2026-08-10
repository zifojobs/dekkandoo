import type { APIRoute } from 'astro';

// Genere plutot que fige dans public/ : il doit annoncer le sitemap a l'adresse
// REELLE du deploiement. Un robots.txt qui renvoie vers un domaine qui ne
// repond pas envoie les moteurs dans le vide.
export const GET: APIRoute = ({ site }) => {
  const sitemap = new URL('sitemap-index.xml', site).href;
  return new Response(
    `User-agent: *\nAllow: /\n\nSitemap: ${sitemap}\n`,
    { headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
  );
};
