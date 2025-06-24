<script lang="ts">
  import { onMount } from 'svelte';
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
  
  // Simple Components
  import ParticleSystem from './components/ParticleSystem.svelte';

  // Local state for routing
  let currentPage = 'home';
  let scrollProgress = 0;

  gsap.registerPlugin(ScrollTrigger);

  onMount(() => {
    // Simple routing based on URL
    const path = window.location.pathname;
    if (path === '/pricing') {
      currentPage = 'pricing';
    } else if (path === '/payment/success') {
      currentPage = 'success';
    } else {
      currentPage = 'home';
    }
    
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

  // Simple navigation function
  function navigateTo(path: string) {
    window.history.pushState({}, '', path);
    if (path === '/pricing') {
      currentPage = 'pricing';
    } else if (path === '/payment/success') {
      currentPage = 'success';
    } else {
      currentPage = 'home';
    }
  }

  // Expose navigation function globally for components
  globalThis.navigateTo = navigateTo;
</script>

<!-- Enhanced Scroll Progress Indicator -->
{#if currentPage === 'home'}
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
  {#if currentPage === 'home'}
    <!-- Main Home Sections -->
    <Hero />
    <Services />
    <Team />
    <Contact />
  {:else if currentPage === 'pricing'}
    <PricingPage />
  {:else if currentPage === 'success'}
    <PaymentSuccess />
  {:else}
    <!-- Default to home -->
    <Hero />
    <Services />
    <Team />
    <Contact />
  {/if}
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
