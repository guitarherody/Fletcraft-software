import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte({
    hot: {
      preserveLocalState: true,
      noPreserveStateKey: ['@hmr:reset', '@!hmr'],
    },
    compilerOptions: {
      dev: false // Force dev to false for production builds
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
      '$lib': '/src/lib',
      '@': '/src'
    },
    extensions: ['.ts', '.js', '.svelte', '.json'],
    mainFields: ['svelte', 'browser', 'module', 'main']
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['gsap'],
          svelte: ['svelte']
        }
      },
      external: [],
      input: {
        main: './index.html'
      }
    },
    sourcemap: false,
    minify: 'esbuild',
    target: 'esnext',
    assetsDir: 'assets'
  },
  optimizeDeps: {
    include: ['gsap', 'howler', 'chart.js']
  },
  esbuild: {
    target: 'esnext'
  }
})
