import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte({
    hot: {
      preserveLocalState: true,
      noPreserveStateKey: ['@hmr:reset', '@!hmr'],
    }
  })],
  server: {
    port: 3000,
    strictPort: false,
    host: true,
    cors: true,
    hmr: {
      port: 3000,
      host: 'localhost',
      overlay: false // Reduce overlay refreshes
    }
  },
  resolve: {
    alias: {
      '$lib': '/src/lib'
    },
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.svelte']
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['gsap'],
          svelte: ['svelte']
        }
      }
    },
    sourcemap: false,
    minify: 'esbuild'
  },
  optimizeDeps: {
    include: ['gsap', 'howler', 'chart.js']
  }
})
