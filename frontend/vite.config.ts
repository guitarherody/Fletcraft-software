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
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['gsap', 'three'],
          svelte: ['svelte']
        }
      }
    }
  },
  optimizeDeps: {
    include: ['gsap', 'howler', 'chart.js']
  }
})
