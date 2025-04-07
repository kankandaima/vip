import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/', // 部署到根目录
  build: {
    outDir: 'dist', // 输出目录
    assetsDir: 'assets', // 静态资源目录
    sourcemap: false, // 不生成 sourcemap
    minify: 'terser', // 使用 terser 进行压缩
    chunkSizeWarningLimit: 1500, // 文件大小警告的限制 (kb)
  },
  server: {
    host: '0.0.0.0', // 允许外部访问
    port: 3000, // 端口号
  }
})
