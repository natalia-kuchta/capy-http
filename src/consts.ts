// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

// Base Page Metadata, src/layouts/BaseLayout.astro
export const BRAND_NAME = "Capy HTTP";
export const SITE_TITLE = "Capy HTTP";
export const SITE_DESCRIPTION = "A collection of HTTP status codes illustrated by capybaras.";

// Tags Page Metadata, src/pages/tags/index.astro
export const Tags_TITLE = "Capy HTTP - All Tags";
export const Tags_DESCRIPTION =
    "Capy HTTP - All tags and the count of status codes related to each tag";

// Tags Page Metadata, src/pages/tags/[tag]/[page].astro
export function getTagMetadata(tag: string) {
  return {
    title: `All HTTP statuses tagged with '${tag}' in Capy HTTP`,
    description: `Explore HTTP status codes related to ${tag} with capybaras for fun representation.`,
  };
}

// Category Page Metadata, src/pages/category/[category]/[page].astro
export function getCategoryMetadata(category: string) {
  return {
    title: `All HTTP statuses in '${category}' category in Capy HTTP`,
    description: `Browse all HTTP status codes under the ${category} category illustrated by capybaras`,
  };
}

// Header Links, src/components/Header.astro
export const HeaderLinks = [
  { href: "/category/1xx/1/", title: "1xx" },
  { href: "/category/2xx/1/", title: "2xx" },
  { href: "/category/3xx/1/", title: "3xx" },
  { href: "/category/4xx/1/", title: "4xx" },
  { href: "/category/5xx/1/", title: "5xx" },
];

// Footer Links, src/components/Footer.astro
export const FooterLinks = [
  // { href: "/posts/why-capy-http/", title: "Why Capy HTTP" },
  // { href: "/posts/tailwind-typography/", title: "Tailwind" },
  { href: "/tags/", title: "Tags" },
];

// Social Links, src/components/Footer.astro
export const SocialLinks = [
  // { href: "/rss.xml", icon: "tabler:rss", label: "RSS" },
  {
    href: "https://www.tiktok.com/@capy.http?_t=8qCikWtD5ta&_r=1",
    icon: "tabler:brand-tiktok",
    label: "Tiktok",
  },
  {
    href: "https://github.com/natalia-kuchta",
    icon: "tabler:brand-github",
    label: "GitHub",
  },
];

// Search Page Metadata, src/pages/search.astro
export const SEARCH_PAGE_TITLE = `${SITE_TITLE} - Site Search`;
export const SEARCH_PAGE_DESCRIPTION = `Search all content on ${SITE_TITLE}`;
