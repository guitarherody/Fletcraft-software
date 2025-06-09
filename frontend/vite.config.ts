import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from 'path'

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
    alias: [
      { find: '$lib', replacement: path.resolve('./src/lib') },
      { find: '@', replacement: path.resolve('./src') }
    ],
    extensions: ['.ts', '.js', '.svelte', '.json'],
    mainFields: ['svelte', 'browser', 'module', 'main'],
    dedupe: ['svelte', 'chart.js', 'howler']
  },
  build: {
    target: 'esnext',
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['gsap', 'chart.js', 'howler'],
          svelte: ['svelte']
        }
      }
    }
  },
  optimizeDeps: {
    include: ['gsap', 'howler', 'chart.js'],
    exclude: []
  }
})
