// Cấu hình Astro 7: xuất HTML tĩnh vào dist/ (thư mục đưa lên mạng). Trợ lý AI: đọc docs.astro.build bản 7, không viết theo cú pháp Astro 4-5.
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: '{{URL_HOP_LE}}',            // SỬA Ở ĐÂY khi đã có tên miền (tools/dua-len.py --ten-mien làm giúp)
  output: 'static',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
  // tắt đổi dấu tự động: giữ nháy thẳng "..." và ba chấm gõ tay (...), đúng quy ước chữ Việt của xưởng
  markdown: { smartypants: false },
});
