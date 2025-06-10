import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte({
    compilerOptions: {
      dev: false
    }
  })],
  resolve: {
    extensions: ['.ts', '.js', '.svelte', '.json']
  },
  build: {
    target: 'esnext',
    outDir: 'dist',
    sourcemap: false,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['gsap'],
          charts: ['chart.js'],
          audio: ['howler']
        }
      }
    }
  },
  optimizeDeps: {
    include: ['gsap', 'chart.js', 'howler'],
    force: true
  },
  server: {
    hmr: {
      overlay: false
    }
  }
})
