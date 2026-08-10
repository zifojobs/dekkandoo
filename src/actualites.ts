/**
 * Les actualites du Consortium.
 *
 * Source unique : alimente a la fois les cartes de la page d'accueil, les pages
 * individuelles et le sitemap. Une actualite ajoutee ici apparait partout.
 *
 * 🔑 Pourquoi une page par actualite, et pas seulement des cartes : c'est
 * l'arbitrage de Saibo du 01/08. Le Consortium publie deja sur 2 pages Facebook,
 * 2 chaines YouTube et TikTok. Sans adresse propre, Laye ne peut partager que le
 * site entier — toute leur communication existante perd son point d'atterrissage.
 *
 * ⚠️ ETAT DES TEXTES
 * - `diner-de-gala-2026` : texte repris a l'identique de MAQUETTE-SITE.html,
 *   donc DEJA VU PAR LE CLIENT.
 * - Les deux autres : rediges a partir des seuls faits documentes (FICHE-CLIENT,
 *   chiffres d'impact publics, resumes de la maquette). Rien n'y est invente,
 *   mais rien n'y a ete valide non plus. 🔴 A FAIRE RELIRE PAR LE CONSORTIUM
 *   AVANT MISE EN LIGNE — voir `aValider`.
 */
import type photos from './photos.json';

export type Bloc =
  | { type: 'p'; texte: string }
  | { type: 'citation'; texte: string };

export type Actualite = {
  slug: string;
  titre: string;
  /** Affiche a l'ecran. */
  date: string;
  /** Lisible par une machine, pour <time> et le schema.org. */
  dateIso: string;
  photo: keyof typeof photos;
  /** Point de recadrage de la vignette : les cartes sont des bandes courtes. */
  cadrage: string;
  /** Sert de resume sur la carte, de chapo sur la page, et de meta description. */
  chapo: string;
  corps: Bloc[];
  /** Vrai tant que le texte n'a pas ete relu par le Consortium. */
  aValider?: boolean;
};

export const ACTUALITES: Actualite[] = [
  {
    slug: 'diner-de-gala-2026',
    titre: '18,75 millions FCFA remis à 75 associations de Gandon',
    date: '4 juillet 2026',
    dateIso: '2026-07-04',
    // 🔑 Pas la photo de remise de cheque : celle-ci porte « 3.000.000 CFA —
    // FAVEC de RAO » en gros, alors que l'article parle de 18,75 M a Gandon.
    // Deux chiffres qui se contredisent dans la meme image ruinent la
    // credibilite de l'ensemble. Celle-ci montre la mise a l'honneur des
    // beneficiaires, ce que raconte le 2e paragraphe, et n'affiche aucun montant.
    photo: 'beneficiaires-honorees',
    cadrage: 'object-[50%_42%]',
    chapo:
      "Une soirée consacrée aux femmes qui font vivre l'épargne communautaire dans la commune de Gandon, et à celles et ceux que la formation a menés jusqu'à leur propre activité.",
    corps: [
      {
        type: 'p',
        texte:
          "Le Consortium Dëkkandoo a remis 18 750 000 FCFA à 75 associations villageoises d'épargne et de crédit de la commune de Gandon. Ces fonds viennent renforcer directement les capacités des groupements, qui décident eux-mêmes de l'affectation des montants selon les besoins de leurs membres.",
      },
      {
        type: 'p',
        texte:
          "La soirée a également mis à l'honneur 125 bénéficiaires ayant achevé leur parcours de formation dans le cadre du programme E4Y, conduit en partenariat avec l'École Supérieure Polytechnique. Chacune de ces personnes dispose désormais d'une compétence directement mobilisable dans son activité.",
      },
      {
        type: 'p',
        texte:
          "Ce sont ces associations qui portent le travail au quotidien : elles collectent l'épargne semaine après semaine, accordent les crédits, en suivent les remboursements. Le financement ne fait qu'amplifier une mécanique qui existe déjà et qui fonctionne.",
      },
      { type: 'citation', texte: 'Le développement se construit avec les communautés.' },
      {
        type: 'p',
        texte:
          "Nos remerciements vont à la Fondation Roi Baudouin et à Nous Cims, dont l'engagement rend ce programme possible, ainsi qu'aux autorités locales et aux notables qui ont honoré la soirée de leur présence.",
      },
    ],
  },
  {
    slug: 'lancement-aviculture-ndieumbeutt',
    titre: 'Lancement du volet aviculture du programme Ndieumbeutt',
    date: 'Juin 2026',
    dateIso: '2026-06-01',
    photo: 'remise-poussins',
    cadrage: 'object-[50%_50%]',
    chapo:
      "Journée de remise de poussins aux bénéficiaires, première étape d'un accompagnement qui se poursuit sur toute la campagne.",
    corps: [
      {
        type: 'p',
        texte:
          "Le programme Ndieumbeutt a ouvert son volet élevage par une journée de remise de poussins aux bénéficiaires. Chaque groupement repart avec de quoi démarrer une activité avicole, dans le prolongement des financements déjà accordés aux associations villageoises d'épargne et de crédit.",
      },
      {
        type: 'p',
        texte:
          "L'élevage figure, avec la production agricole, parmi les activités que le programme accompagne en priorité : elles produisent un revenu dans un délai court et se conduisent depuis le domicile, ce qui les rend accessibles aux femmes qui ne peuvent pas s'éloigner longtemps.",
      },
      {
        type: 'p',
        texte:
          "La remise n'est pas une fin en soi. L'accompagnement se poursuit sur toute la campagne : suivi des élevages, appui technique et point régulier avec les groupements — c'est la durée du suivi, et non le montant remis, qui décide du résultat.",
      },
    ],
    aValider: true,
  },
  {
    slug: 'formation-saponification',
    titre: 'Quatre groupements formés à la saponification',
    date: 'Mai 2026',
    dateIso: '2026-05-01',
    photo: 'formation-geste',
    cadrage: 'object-[50%_45%]',
    chapo:
      "Une compétence directement monétisable, qui a permis la fabrication de plus de 5 500 produits d'hygiène.",
    corps: [
      {
        type: 'p',
        texte:
          "Quatre groupements de femmes ont suivi une formation à la saponification — la fabrication de savons et de produits d'hygiène. La session a porté sur le dosage, la pesée, le conditionnement et le contrôle de la qualité, gestes que les participantes reproduisent ensuite au sein de leur groupement.",
      },
      {
        type: 'p',
        texte:
          "Le choix de cette activité tient à une raison simple : le produit se vend localement, toute l'année, et la matière première reste accessible. La compétence acquise est mobilisable immédiatement, sans attendre une récolte ni une saison.",
      },
      {
        type: 'p',
        texte:
          "À ce jour, 5 567 produits d'hygiène ont été fabriqués localement par les groupements accompagnés, et 250 femmes ont été formées à la transformation et à la production.",
      },
    ],
    aValider: true,
  },
];

export const parSlug = (slug: string) => ACTUALITES.find((a) => a.slug === slug);
