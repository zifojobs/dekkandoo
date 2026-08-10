// Tailwind est branche via PostCSS, pas via @tailwindcss/vite : au 09/08/2026 ce plugin
// est incompatible avec le moteur rolldown de Vite 8 embarque par Astro 6
// (erreur "Missing field `tsconfigPaths`"). Les deux voies produisent le meme CSS.
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
};
