<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';

  let nav: HTMLElement;
  let isScrolled = false;

  onMount(() => {
    gsap.registerPlugin(ScrollTrigger);

    // Navbar scroll effect
    ScrollTrigger.create({
      start: "top -80",
      end: "max",
      onUpdate: (self) => {
        if (self.progress > 0 && !isScrolled) {
          isScrolled = true;
          gsap.to(nav, {
            background: 'rgba(255, 255, 255, 0.08)',
            backdropFilter: 'blur(30px)',
            borderBottom: '1px solid rgba(139, 92, 246, 0.2)',
            duration: 0.3,
            ease: 'power2.out'
          });
        } else if (self.progress === 0 && isScrolled) {
          isScrolled = false;
          gsap.to(nav, {
            background: 'rgba(255, 255, 255, 0.03)',
            backdropFilter: 'blur(20px)',
            borderBottom: '1px solid rgba(139, 92, 246, 0.1)',
            duration: 0.3,
            ease: 'power2.out'
          });
        }
      }
    });

    // Floating navigation animation
    gsap.to(nav, {
      y: -2,
      duration: 3,
      ease: 'sine.inOut',
      yoyo: true,
      repeat: -1
    });
  });
</script>

<nav bind:this={nav} class="liquid-glass-nav fixed top-4 left-1/2 transform -translate-x-1/2 z-50 w-11/12 max-w-4xl">
  <div class="liquid-glass-nav-container px-6 py-4 rounded-2xl">
    <div class="flex items-center justify-between">
      <!-- Logo with liquid glass effect -->
      <div class="liquid-glass-logo flex items-center space-x-2">
        <div class="liquid-glass-logo-icon w-10 h-10 rounded-xl flex items-center justify-center">
          <svg class="w-6 h-6 text-primary" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2L2 7L12 12L22 7L12 2Z"/>
            <path d="M2 17L12 22L22 17"/>
            <path d="M2 12L12 17L22 12"/>
          </svg>
        </div>
        <span class="font-bold text-lg text-text-primary">Fletcraft</span>
      </div>

      <!-- Navigation Links -->
      <div class="hidden md:flex items-center space-x-1">
        <a href="#home" class="liquid-glass-nav-link px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300">
          Home
        </a>
        <a href="#services" class="liquid-glass-nav-link px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300">
          Services
        </a>
        <a href="#portfolio" class="liquid-glass-nav-link px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300">
          Portfolio
        </a>
        <a href="#team" class="liquid-glass-nav-link px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300">
          Team
        </a>
        <a href="#contact" class="liquid-glass-nav-link px-4 py-2 rounded-xl text-sm font-medium transition-all duration-300">
          Contact
        </a>
      </div>

      <!-- CTA Button -->
      <div class="flex items-center space-x-4">
        <a href="#contact" class="liquid-glass-cta-button px-6 py-2.5 rounded-xl text-sm font-semibold transition-all duration-300">
          Get Started
        </a>
        
        <!-- Mobile Menu Button -->
        <button class="md:hidden liquid-glass-menu-button p-2 rounded-xl">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>

<style>
  .liquid-glass-nav {
    will-change: transform;
  }

  .liquid-glass-nav-container {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.1);
    box-shadow: 
      0 8px 32px rgba(139, 92, 246, 0.08),
      inset 0 1px 0 rgba(255, 255, 255, 0.08);
    transition: all 0.3s ease;
  }

  .liquid-glass-logo-icon {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(168, 85, 247, 0.2));
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(139, 92, 246, 0.25);
    box-shadow: 
      0 4px 16px rgba(139, 92, 246, 0.12),
      inset 0 1px 0 rgba(255, 255, 255, 0.15);
  }

  .liquid-glass-nav-link {
    color: rgba(255, 255, 255, 0.8);
    position: relative;
    overflow: hidden;
  }

  .liquid-glass-nav-link::before {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(139, 92, 246, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: inherit;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .liquid-glass-nav-link:hover::before {
    opacity: 1;
  }

  .liquid-glass-nav-link:hover {
    color: rgba(255, 255, 255, 1);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.15);
  }

  .liquid-glass-cta-button {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.8), rgba(168, 85, 247, 0.8));
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(139, 92, 246, 0.3);
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 
      0 6px 20px rgba(139, 92, 246, 0.2),
      inset 0 1px 0 rgba(255, 255, 255, 0.2);
  }

  .liquid-glass-cta-button::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .liquid-glass-cta-button:hover::before {
    opacity: 1;
  }

  .liquid-glass-cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 
      0 8px 25px rgba(139, 92, 246, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.3);
  }

  .liquid-glass-menu-button {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(139, 92, 246, 0.15);
    color: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
  }

  .liquid-glass-menu-button:hover {
    background: rgba(139, 92, 246, 0.1);
    color: rgba(255, 255, 255, 1);
    transform: translateY(-1px);
  }
</style> 