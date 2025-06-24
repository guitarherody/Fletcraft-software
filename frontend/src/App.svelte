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
    // Enhanced routing with multiple fallback methods
    function updateRoute() {
      const path = window.location.pathname;
      const hash = window.location.hash;
      const searchParams = new URLSearchParams(window.location.search);
      
      console.log('=== ROUTING DEBUG ===');
      console.log('Full URL:', window.location.href);
      console.log('Path:', path);
      console.log('Hash:', hash);
      console.log('Search params:', searchParams.toString());
      console.log('Has PayFast params:', searchParams.has('pf_payment_id') || searchParams.has('m_payment_id'));
      
      // Multiple ways to detect success page
      const isSuccessPage = 
        path === '/payment/success' ||
        path.includes('/payment/success') ||
        hash === '#success' ||
        hash === '#payment/success' ||
        searchParams.has('pf_payment_id') ||
        searchParams.has('m_payment_id') ||
        path.includes('success');
      
      const isPricingPage = 
        path === '/pricing' || 
        path.includes('/pricing') || 
        hash === '#pricing';
      
      if (isSuccessPage) {
        currentPage = 'success';
        console.log('✅ SUCCESS PAGE DETECTED!');
        // Also update URL to clean version
        if (path !== '/payment/success') {
          window.history.replaceState({}, '', '/payment/success' + window.location.search);
        }
      } else if (isPricingPage) {
        currentPage = 'pricing';
        console.log('📄 Pricing page detected');
      } else {
        currentPage = 'home';
        console.log('🏠 Home page (default)');
      }
      
      console.log('Current page set to:', currentPage);
      console.log('==================');
    }
    
    // Initial route detection
    updateRoute();
    
    // Listen for all navigation events
    window.addEventListener('popstate', updateRoute);
    window.addEventListener('hashchange', updateRoute);
    
    // Also check every second for the first 10 seconds (in case of async redirects)
    let checkCount = 0;
    const intervalId = setInterval(() => {
      checkCount++;
      if (checkCount >= 10) {
        clearInterval(intervalId);
        return;
      }
      
      const searchParams = new URLSearchParams(window.location.search);
      if ((searchParams.has('pf_payment_id') || searchParams.has('m_payment_id')) && currentPage !== 'success') {
        console.log('🔄 Delayed PayFast parameter detection');
        updateRoute();
      }
    }, 1000);
    
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
      window.removeEventListener('popstate', updateRoute);
      window.removeEventListener('hashchange', updateRoute);
      clearInterval(intervalId);
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
