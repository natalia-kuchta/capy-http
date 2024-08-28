import { defineCollection, z } from "astro:content";

const posts = defineCollection({
  type: "content",
  schema: ({image}) => z.object({
    title: z.string(),
    cover: image(),
    code: z.number(),

    pubDate: z.date(),
    description: z.string(),

    coverAlt: z.string(),
    category: z.array(z.string()),
    tags: z.array(z.string()),
  }),
});

export const collections = { posts };
