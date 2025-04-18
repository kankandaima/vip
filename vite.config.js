import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/', // 部署到根目录
  publicDir: 'src/jpg', // 将 src/jpg 目录作为公共资源目录
  build: {
    outDir: 'dist', // 输出目录
    assetsDir: 'assets', // 静态资源目录
    sourcemap: false, // 不生成 sourcemap
    minify: 'terser', // 使用 terser 进行压缩
    chunkSizeWarningLimit: 1500, // 文件大小警告的限制 (kb)
    target: 'esnext',
    rollupOptions: {
      output: {
        manualChunks: {
          'element-plus': ['element-plus'],
          'vue': ['vue']
        }
      }
    }
  },
  server: {
    host: '0.0.0.0', // 允许外部访问
    port: 3000, // 端口号
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
