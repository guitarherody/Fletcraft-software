<script lang="ts">
  import { onMount } from 'svelte';
  import { isLoading, scrollProgress, currentSection, soundEnabled } from './lib/stores';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  
  // Core Components
  import Navbar from './components/Navbar.svelte';
  import Hero from './components/Hero.svelte';
  import Services from './components/Services.svelte';
  import Team from './components/Team.svelte';
  import Contact from './components/Contact.svelte';
  
  // Advanced Components
  import ParticleSystem from './components/ParticleSystem.svelte';
  import AIChat from './components/AIChat.svelte';
  import Portfolio from './components/Portfolio.svelte';
  import Analytics from './components/Analytics.svelte';

  gsap.registerPlugin(ScrollTrigger);

  onMount(() => {
    // Remove artificial loading delay for better performance
    isLoading.set(false);

    // Track scroll progress
    const updateScrollProgress = () => {
      const scrollTop = window.pageYOffset;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      scrollProgress.set(Math.min(Math.max(progress, 0), 100));
    };

    window.addEventListener('scroll', updateScrollProgress);

    return () => {
      window.removeEventListener('scroll', updateScrollProgress);
    };
  });
</script>

<!-- Simple loading indicator (removed artificial delay) -->

<!-- Scroll Progress Indicator -->
<div class="fixed top-0 left-0 w-full h-1 bg-primary/20 z-40">
  <div 
    class="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-75"
    style="width: {$scrollProgress}%"
  ></div>
</div>

<main class="relative">
  <!-- Background Particle System -->
  <ParticleSystem />
  
  <!-- Navigation -->
  <Navbar />
  
  <!-- Main Sections -->
  <Hero />
  <Services />
  <Team />
  <Portfolio />
  <Analytics />
  <Contact />
  
  <!-- AI Chat Assistant -->
  <AIChat />
</main>

<style>
  :global(html) {
    scroll-behavior: smooth;
  }

  :global(body) {
    overflow-x: hidden;
  }
  
  :global(::-webkit-scrollbar) {
    width: 8px;
  }
  
  :global(::-webkit-scrollbar-track) {
    background: rgba(10, 10, 10, 0.5);
  }
  
  :global(::-webkit-scrollbar-thumb) {
    background: linear-gradient(to bottom, #6366f1, #8b5cf6);
    border-radius: 4px;
  }
</style>
