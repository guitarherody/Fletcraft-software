<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let heroSection: HTMLElement;
  let enable3D = false; // Disable heavy 3D by default for better performance

  onMount(() => {
    // Simple, fast animations
    if (heroSection) {
      gsap.from('.hero-text', {
        duration: 0.8,
        y: 30,
        opacity: 0,
        stagger: 0.1,
        ease: 'power2.out'
      });
    }
  });
</script>

<section bind:this={heroSection} class="relative min-h-screen flex items-center justify-center overflow-hidden bg-background text-text-primary">
  <!-- Lightweight background effects (no heavy 3D) -->
  <div class="absolute inset-0 bg-gradient-to-b from-background via-transparent to-background opacity-90"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(99,102,241,0.1)_0%,transparent_100%)]"></div>
  
  <!-- Animated geometric shapes for visual interest -->
  <div class="absolute inset-0 overflow-hidden pointer-events-none">
    <div class="absolute top-1/4 left-1/4 w-32 h-32 border border-primary/20 rounded-full animate-pulse"></div>
    <div class="absolute bottom-1/4 right-1/4 w-24 h-24 border border-secondary/20 rounded-full animate-pulse" style="animation-delay: 1s;"></div>
    <div class="absolute top-1/2 right-1/3 w-16 h-16 border border-accent/20 rounded-full animate-pulse" style="animation-delay: 2s;"></div>
  </div>
  
  <!-- Content -->
  <div class="container relative px-6 md:px-8 z-10">
    <div class="max-w-4xl mx-auto text-center">
      <div class="mb-6 inline-block">
        <span class="hero-text inline-block px-4 py-1 rounded-full text-sm font-medium bg-primary/10 text-primary mb-4">
          Welcome to Fletcraft Software
        </span>
      </div>
      
      <h1 class="hero-text text-5xl md:text-7xl font-display font-bold mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent animate-gradient-x leading-tight">
        Crafting Digital Excellence
      </h1>
      
      <p class="hero-text text-lg md:text-xl text-text-secondary mb-10 max-w-2xl mx-auto leading-relaxed">
        We transform visionary ideas into powerful software solutions that drive business growth and innovation in the digital age.
      </p>
      
      <div class="hero-text flex flex-wrap gap-4 justify-center">
        <a href="#contact" 
          class="group relative px-8 py-3 bg-primary overflow-hidden rounded-lg transition-all duration-300 hover:scale-105">
          <div class="absolute inset-0 bg-gradient-to-r from-primary via-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
          <span class="relative text-white font-medium">Get Started</span>
        </a>
        
        <a href="#services" 
          class="group px-8 py-3 border-2 border-primary/20 rounded-lg transition-all duration-300 hover:border-primary/40 hover:scale-105">
          <span class="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent font-medium">
            Our Services
          </span>
        </a>
      </div>
    </div>
  </div>
  
  <!-- Scroll Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
    <svg class="w-6 h-6 text-text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
    </svg>
  </div>
</section> 