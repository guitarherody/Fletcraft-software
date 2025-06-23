<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  
  let isScrolled = false;
  let isMenuOpen = false;
  
  function handleScroll() {
    isScrolled = window.scrollY > 20;
  }
  
  onMount(() => {
    window.addEventListener('scroll', handleScroll);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  });
  
  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
    
    if (isMenuOpen) {
      gsap.from('.mobile-menu-item', {
        y: 20,
        opacity: 0,
        stagger: 0.1,
        duration: 0.3,
        ease: 'power2.out'
      });
    }
  }
</script>

<nav class:scrolled={isScrolled}
     class="fixed top-0 left-0 right-0 z-50 transition-all duration-300">
  <div class="container mx-auto px-6 md:px-8">
    <div class="flex items-center justify-between h-20">
      <!-- Logo -->
      <a href="/" class="flex items-center space-x-2">
        <span class="text-2xl font-display font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
          Fletcraft
        </span>
      </a>
      
      <!-- Desktop Menu -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="#services" class="nav-link">Services</a>
        <a href="/pricing" class="nav-link">Pricing</a>
        <a href="#about" class="nav-link">About</a>
        <a href="#work" class="nav-link">Work</a>
        <a href="#contact" 
           class="px-6 py-2 rounded-lg bg-primary/10 text-primary hover:bg-primary/20 transition-colors">
          Contact Us
        </a>
      </div>
      
      <!-- Mobile Menu Button -->
      <button class="md:hidden" on:click={toggleMenu}>
        <svg class="w-6 h-6 text-text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          {#if !isMenuOpen}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          {:else}
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          {/if}
        </svg>
      </button>
    </div>
    
    <!-- Mobile Menu -->
    {#if isMenuOpen}
      <div class="md:hidden">
        <div class="py-4 space-y-4">
          <a href="#services" class="mobile-menu-item block px-4 py-2 hover:bg-primary/5 rounded-lg">Services</a>
          <a href="/pricing" class="mobile-menu-item block px-4 py-2 hover:bg-primary/5 rounded-lg">Pricing</a>
          <a href="#about" class="mobile-menu-item block px-4 py-2 hover:bg-primary/5 rounded-lg">About</a>
          <a href="#work" class="mobile-menu-item block px-4 py-2 hover:bg-primary/5 rounded-lg">Work</a>
          <a href="#contact" class="mobile-menu-item block px-4 py-2 bg-primary/10 text-primary hover:bg-primary/20 rounded-lg">
            Contact Us
          </a>
        </div>
      </div>
    {/if}
  </div>
</nav>

<style lang="postcss">
  nav {
    @apply bg-transparent;
    backdrop-filter: blur(0px);
  }
  
  nav.scrolled {
    @apply bg-background/80;
    backdrop-filter: blur(12px);
    border-bottom: 1px solid theme('colors.primary.DEFAULT/0.1');
  }
  
  .nav-link {
    @apply text-text-secondary hover:text-text-primary transition-colors relative;
  }
  
  .nav-link::after {
    content: '';
    @apply absolute bottom-0 left-0 w-0 h-0.5 bg-primary transition-all duration-300;
  }
  
  .nav-link:hover::after {
    @apply w-full;
  }
</style> 