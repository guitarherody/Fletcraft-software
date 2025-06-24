<script lang="ts">
  import { onMount } from 'svelte';
  import { currentPage, initRouter } from './lib/router';
  // Temporarily removing stores dependency to fix build issues
  // import { isLoading, scrollProgress, currentSection, soundEnabled } from './lib/stores';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  
  // Core Components - These should work
  import Navigation from './components/Navigation.svelte';
  import Hero from './components/Hero.svelte';
  import Services from './components/Services.svelte';
  import Team from './components/Team.svelte';
  import Contact from './components/Contact.svelte';
  import PricingPage from './components/PricingPage.svelte';
  import PaymentSuccess from './components/PaymentSuccess.svelte';
  
  // Glass Morphism Components
  import LiquidGlass from './components/LiquidGlass.svelte';
  
  // Simple Components
  import ParticleSystem from './components/ParticleSystem.svelte';
  
  // Temporarily disabled - problematic components
  // import AIChat from './components/AIChat.svelte';
  // import Portfolio from './components/Portfolio.svelte';
  // import Analytics from './components/Analytics.svelte';

  // Local state instead of stores
  let isLoading = false;
  let scrollProgress = 0;

  gsap.registerPlugin(ScrollTrigger);

  onMount(() => {
    // Initialize router
    initRouter();
    
    // Remove artificial loading delay for better performance
    isLoading = false;

    // Track scroll progress
    const updateScrollProgress = () => {
      const scrollTop = window.pageYOffset;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;
      scrollProgress = Math.min(Math.max(progress, 0), 100);
    };

    window.addEventListener('scroll', updateScrollProgress);

    return () => {
      window.removeEventListener('scroll', updateScrollProgress);
    };
  });
</script>

<!-- Simple loading indicator (removed artificial delay) -->

<!-- Enhanced Scroll Progress Indicator with Liquid Glass -->
{#if $currentPage === 'home'}
<div class="fixed top-0 left-0 w-full h-1 z-40">
  <div class="relative w-full h-full bg-glass-primary-5 backdrop-blur-lg border-b border-glass-primary-10">
    <div 
      class="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-150 shadow-sm"
      style="width: {scrollProgress}%"
    ></div>
  </div>
</div>
{/if}

<main class="relative">
  <!-- Background Particle System -->
  <ParticleSystem />
  
  <!-- Navigation -->
  <Navigation />
  
  <!-- Route-based content -->
  {#if $currentPage === 'home'}
    <!-- Main Home Sections -->
    <Hero />
    <Services />
    <Team />
    <Contact />
  {:else if $currentPage === 'pricing'}
    <PricingPage />
  {:else if $currentPage === 'success'}
    <PaymentSuccess />
  {:else}
    <!-- Default to home -->
    <Hero />
    <Services />
    <Team />
    <Contact />
  {/if}
  
  <!-- AI Chat Assistant -->
  <!-- <AIChat /> -->
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
