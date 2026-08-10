/**
 * Les comptes officiels du Consortium et de sa sous-marque Ndieumbeutt.
 *
 * Source unique : FICHE-CLIENT.md, section « Presence reseaux sociaux ». Cette
 * liste alimente a la fois le pied de page, la section Contact et le `sameAs`
 * du schema.org — d'ou le fichier separe : trois copies d'une meme adresse
 * finissent toujours par diverger.
 *
 * Les cinq URL ont ete verifiees le 10/08/2026, profil ouvert dans un vrai
 * navigateur et identite lue a l'ecran.
 *
 * 🔴 Deux pieges, tous deux rencontres pour de vrai :
 *
 * 1. `FICHE-CLIENT.md` donnait le TikTok `@consortium.dkkand` — ce compte
 *    N'EXISTE PAS (« Couldn't find this account »). Le bon est
 *    `@consortium.dekkandoo`, corrige par Saibo. Un simple controle de code
 *    HTTP ne l'aurait jamais vu : TikTok repond 200 sur un profil absent et
 *    n'affiche l'erreur qu'apres execution du JavaScript. ⇒ Pour un profil
 *    social, verifier l'IDENTITE AFFICHEE, jamais le code de reponse.
 * 2. Le handle YouTube du Consortium contient un trema : il DOIT rester encode
 *    en %C3%AB, faute de quoi certains clients mail et messageries tronquent
 *    le lien.
 */
export type Compte = {
  reseau: 'facebook' | 'youtube' | 'tiktok';
  nom: string;
  url: string;
};

export const CONSORTIUM: Compte[] = [
  {
    reseau: 'facebook',
    nom: 'Facebook',
    url: 'https://www.facebook.com/profile.php?id=61575892094019',
  },
  {
    reseau: 'youtube',
    nom: 'YouTube',
    url: 'https://www.youtube.com/@ConsortiumD%C3%ABkkandoo-v1m',
  },
  {
    reseau: 'tiktok',
    nom: 'TikTok',
    // Confirme par le client le 10/08. Le parametre `?_r=1` de son lien vient
    // de l'application TikTok : il n'a rien a faire dans une URL publiee.
    url: 'https://www.tiktok.com/@consortium.dekkandoo',
  },
];

export const NDIEUMBEUTT: Compte[] = [
  {
    reseau: 'facebook',
    nom: 'Facebook',
    url: 'https://www.facebook.com/profile.php?id=61577473989197',
  },
  {
    reseau: 'youtube',
    nom: 'YouTube',
    url: 'https://www.youtube.com/@Ndieumbeutt',
  },
];

/** Pour le `sameAs` de schema.org : tous les comptes, sans doublon. */
export const TOUS = [...CONSORTIUM, ...NDIEUMBEUTT].map((c) => c.url);
