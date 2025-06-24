<script lang="ts">
  import { onMount } from 'svelte';

  // Declare global navigation function
  declare global {
    var navigateTo: ((path: string) => void) | undefined;
  }

  let nav: HTMLElement;
  let isScrolled = false;
  let isVisible = true;
  let lastScrollY = 0;

  onMount(() => {
    // Enhanced scroll effect with sticky behavior
    const handleScroll = () => {
      const currentScrollY = window.scrollY;
      const scrolled = currentScrollY > 80;
      
      // Determine if navbar should be visible (sticky behavior)
      if (currentScrollY > lastScrollY && currentScrollY > 200) {
        // Scrolling down - hide navbar
        isVisible = false;
      } else {
        // Scrolling up or at top - show navbar
        isVisible = true;
      }
      
      if (scrolled !== isScrolled) {
        isScrolled = scrolled;
      }
      
      lastScrollY = currentScrollY;
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
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
  <!-- Vaporous Effect Layers -->
  <div class="vapor-layer vapor-1"></div>
  <div class="vapor-layer vapor-2"></div>
  <div class="vapor-layer vapor-3"></div>
  
  <!-- Steam Condensation Droplets -->
  <div class="condensation-drops">
    <div class="drop drop-1"></div>
    <div class="drop drop-2"></div>
    <div class="drop drop-3"></div>
    <div class="drop drop-4"></div>
    <div class="drop drop-5"></div>
  </div>
  
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
        <span class="font-bold text-lg text-white">Fletcraft</span>
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
        <button on:click={() => handleNavigation('/pricing')} class="cta-button px-6 py-2.5 rounded-xl text-sm font-semibold bg-gradient-to-r from-orange-600 to-red-600 text-white hover:from-orange-700 hover:to-red-700 transition-all duration-200">
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
  nav {
    position: relative;
  }

  /* Vaporous Glass Effect */
  .nav-container {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(25px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
  }

  .nav-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, 
      rgba(147, 51, 234, 0.08) 0%,
      rgba(16, 185, 129, 0.06) 25%,
      rgba(255, 120, 60, 0.04) 50%,
      rgba(147, 51, 234, 0.06) 75%,
      rgba(16, 185, 129, 0.08) 100%
    );
    border-radius: inherit;
    opacity: 0.6;
    animation: vaporShimmer 8s ease-in-out infinite;
  }

  .nav-container::after {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    background: linear-gradient(45deg, 
      rgba(255, 255, 255, 0.1) 0%,
      transparent 30%,
      rgba(147, 51, 234, 0.05) 50%,
      transparent 70%,
      rgba(16, 185, 129, 0.08) 100%
    );
    border-radius: inherit;
    filter: blur(1px);
    animation: steamFlow 12s linear infinite;
    z-index: -1;
  }

  .nav-container.scrolled {
    background: rgba(255, 255, 255, 0.04);
    border-color: rgba(255, 255, 255, 0.15);
    box-shadow: 
      0 8px 32px rgba(0, 0, 0, 0.4),
      0 0 20px rgba(147, 51, 234, 0.1),
      0 0 40px rgba(16, 185, 129, 0.08),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(30px) saturate(200%);
  }

  /* Vapor Layers */
  .vapor-layer {
    position: absolute;
    border-radius: 1rem;
    pointer-events: none;
    z-index: -1;
  }

  .vapor-1 {
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    background: radial-gradient(ellipse at 30% 20%, 
      rgba(147, 51, 234, 0.1) 0%,
      rgba(16, 185, 129, 0.08) 50%,
      transparent 100%
    );
    filter: blur(8px);
    animation: vaporDrift1 15s ease-in-out infinite;
  }

  .vapor-2 {
    top: -8px;
    left: -8px;
    right: -8px;
    bottom: -8px;
    background: radial-gradient(ellipse at 70% 80%, 
      rgba(16, 185, 129, 0.08) 0%,
      rgba(255, 120, 60, 0.06) 50%,
      transparent 100%
    );
    filter: blur(12px);
    animation: vaporDrift2 18s ease-in-out infinite reverse;
  }

  .vapor-3 {
    top: -10px;
    left: -10px;
    right: -10px;
    bottom: -10px;
    background: radial-gradient(ellipse at 50% 50%, 
      rgba(255, 120, 60, 0.06) 0%,
      rgba(147, 51, 234, 0.04) 50%,
      transparent 100%
    );
    filter: blur(15px);
    animation: vaporDrift3 20s ease-in-out infinite;
  }

  /* Steam Condensation Droplets */
  .condensation-drops {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    border-radius: 1rem;
    overflow: hidden;
  }

  .drop {
    position: absolute;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.3) 0%,
      rgba(255, 255, 255, 0.1) 40%,
      transparent 100%
    );
    border-radius: 50%;
    filter: blur(0.5px);
    animation: dropletForm 6s ease-in-out infinite;
  }

  .drop-1 {
    width: 3px;
    height: 3px;
    top: 20%;
    left: 15%;
    animation-delay: 0s;
  }

  .drop-2 {
    width: 2px;
    height: 2px;
    top: 60%;
    right: 25%;
    animation-delay: 1.5s;
  }

  .drop-3 {
    width: 4px;
    height: 4px;
    top: 40%;
    left: 60%;
    animation-delay: 3s;
  }

  .drop-4 {
    width: 2.5px;
    height: 2.5px;
    top: 75%;
    right: 15%;
    animation-delay: 4.5s;
  }

  .drop-5 {
    width: 3.5px;
    height: 3.5px;
    top: 30%;
    right: 45%;
    animation-delay: 2s;
  }

  .logo-icon {
    background: rgba(147, 51, 234, 0.15);
    border: 1px solid rgba(147, 51, 234, 0.3);
    box-shadow: 
      0 0 10px rgba(147, 51, 234, 0.2),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
  }

  .nav-link:hover {
    background: rgba(255, 255, 255, 0.08);
    box-shadow: 
      0 0 15px rgba(147, 51, 234, 0.15),
      0 0 25px rgba(16, 185, 129, 0.1);
    backdrop-filter: blur(10px);
  }

  .cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 
      0 6px 20px rgba(249, 115, 22, 0.4),
      0 0 30px rgba(147, 51, 234, 0.2);
  }

  /* Animations */
  @keyframes vaporShimmer {
    0%, 100% {
      opacity: 0.6;
      transform: scale(1);
    }
    50% {
      opacity: 0.8;
      transform: scale(1.02);
    }
  }

  @keyframes steamFlow {
    0% {
      transform: translateX(-100%) rotate(0deg);
      opacity: 0.3;
    }
    50% {
      opacity: 0.6;
    }
    100% {
      transform: translateX(100%) rotate(10deg);
      opacity: 0.3;
    }
  }

  @keyframes vaporDrift1 {
    0%, 100% {
      transform: translateX(0) translateY(0) rotate(0deg);
      opacity: 0.8;
    }
    33% {
      transform: translateX(10px) translateY(-5px) rotate(2deg);
      opacity: 0.6;
    }
    66% {
      transform: translateX(-8px) translateY(3px) rotate(-1deg);
      opacity: 0.9;
    }
  }

  @keyframes vaporDrift2 {
    0%, 100% {
      transform: translateX(0) translateY(0) rotate(0deg);
      opacity: 0.6;
    }
    50% {
      transform: translateX(-12px) translateY(-8px) rotate(3deg);
      opacity: 0.8;
    }
  }

  @keyframes vaporDrift3 {
    0%, 100% {
      transform: translateX(0) translateY(0) rotate(0deg);
      opacity: 0.4;
    }
    25% {
      transform: translateX(8px) translateY(4px) rotate(-2deg);
      opacity: 0.7;
    }
    75% {
      transform: translateX(-6px) translateY(-2px) rotate(1deg);
      opacity: 0.5;
    }
  }

  @keyframes dropletForm {
    0% {
      transform: scale(0);
      opacity: 0;
    }
    20% {
      transform: scale(1);
      opacity: 1;
    }
    80% {
      transform: scale(1);
      opacity: 1;
    }
    100% {
      transform: scale(0);
      opacity: 0;
    }
  }
</style> 