<script lang="ts">
  import { onMount } from 'svelte';

  // Declare global navigation function
  declare global {
    var navigateTo: ((path: string) => void) | undefined;
  }

  let nav: HTMLElement;
  let isScrolled = false;

  onMount(() => {
    // Simple scroll effect
    const handleScroll = () => {
      const scrolled = window.scrollY > 80;
      if (scrolled !== isScrolled) {
        isScrolled = scrolled;
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  });

  function handleNavigation(path: string) {
    if (globalThis.navigateTo) {
      globalThis.navigateTo(path);
    } else {
      window.location.href = path;
    }
  }

  function scrollToSection(sectionId: string) {
    const currentPath = window.location.pathname;
    if (currentPath !== '/') {
      handleNavigation('/');
      setTimeout(() => {
        const element = document.getElementById(sectionId);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } else {
      const element = document.getElementById(sectionId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
</script>

<nav bind:this={nav} class="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 w-11/12 max-w-4xl transition-all duration-300">
  <div class="nav-container px-6 py-4 rounded-2xl {isScrolled ? 'scrolled' : ''}">
    <div class="flex items-center justify-between">
      
      <!-- Logo -->
      <div class="flex items-center space-x-2">
        <div class="logo-icon w-10 h-10 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-purple-400" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2L2 7L12 12L22 7L12 2Z"/>
            <path d="M2 17L12 22L22 17"/>
            <path d="M2 12L12 17L22 12"/>
          </svg>
        </div>
        <span class="font-bold text-lg text-white">Fletcher</span>
      </div>

      <!-- Navigation Links -->
      <div class="hidden md:flex items-center space-x-1">
        <button on:click={() => scrollToSection('home')} class="nav-link px-4 py-2 rounded-xl text-sm font-medium text-gray-300 hover:text-white transition-colors duration-200">
          Home
        </button>
        <button on:click={() => scrollToSection('services')} class="nav-link px-4 py-2 rounded-xl text-sm font-medium text-gray-300 hover:text-white transition-colors duration-200">
          Services
        </button>
        <button on:click={() => scrollToSection('team')} class="nav-link px-4 py-2 rounded-xl text-sm font-medium text-gray-300 hover:text-white transition-colors duration-200">
          Team
        </button>
        <button on:click={() => scrollToSection('contact')} class="nav-link px-4 py-2 rounded-xl text-sm font-medium text-gray-300 hover:text-white transition-colors duration-200">
          Contact
        </button>
      </div>

      <!-- CTA Button -->
      <div class="flex items-center space-x-4">
        <button on:click={() => handleNavigation('/pricing')} class="cta-button px-6 py-2.5 rounded-xl text-sm font-semibold bg-gradient-to-r from-purple-600 to-pink-600 text-white hover:from-purple-700 hover:to-pink-700 transition-all duration-200">
          Get Started
        </button>
        
        <!-- Mobile Menu Button -->
        <button class="md:hidden menu-button p-2 rounded-xl bg-white/10 text-white hover:bg-white/20 transition-colors duration-200">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>

<style>
  .nav-container {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
  }

  .nav-container.scrolled {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  }

  .logo-icon {
    background: rgba(139, 92, 246, 0.2);
    border: 1px solid rgba(139, 92, 246, 0.3);
  }

  .nav-link:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .cta-button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
  }
</style> 