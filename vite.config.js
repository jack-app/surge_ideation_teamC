import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueEnvPlugin from 'vite-plugin-vue-env'

// envファイルを読み込む
import { config } from 'dotenv'
config({ path: '.env.dev' })

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueEnvPlugin()],
  build: {
    outDir: 'docs',
  },
  resolve: {
    alias: {
      //vueのルートの簡略表現を定義
      '@': fileURLToPath(new URL('./frontend', import.meta.url))
    }
  },
  /*
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // FastAPIバックエンドのURLを指定
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  */
})
