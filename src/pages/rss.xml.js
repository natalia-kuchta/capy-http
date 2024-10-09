import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { SITE_TITLE, SITE_DESCRIPTION } from "@consts";
import dayjs from "dayjs";

export async function GET(context) {
  let posts = await getCollection("posts");

  posts = posts
    .sort((a, b) => b.data.code - a.data.code);

  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: context.site,
    customData: `<language>en</language>`,
    trailingSlash: true,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      link: `/posts/${post.slug}`,
      pubDate: dayjs().toISOString(),
      content: post.body,
      customData: post.data.customData,
    })),
  });
}
