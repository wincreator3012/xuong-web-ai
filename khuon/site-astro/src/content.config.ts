// Bộ sưu tập bài viết: mỗi bài là một tệp .md trong src/content/bai-viet/. Thiếu tiêu đề hay ngày là báo lỗi lúc dựng.
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const baiViet = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/bai-viet' }),
  schema: z.object({
    tieuDe: z.string(),
    moTa: z.string().max(155),
    ngay: z.coerce.date(),
    nhap: z.boolean().default(false),   // true: chưa đăng
  }),
});

export const collections = { 'bai-viet': baiViet };
