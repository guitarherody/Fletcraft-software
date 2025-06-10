<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let heroSection: HTMLElement;
  let fireflyContainer: HTMLElement;
  let liquidGlassContainer: HTMLElement;

  onMount(() => {
    // Subtle entrance animations
    if (heroSection) {
      gsap.timeline()
        .from('.hero-badge', {
          duration: 1.2,
          y: -30,
          opacity: 0,
          ease: 'power2.out'
        })
        .from('.hero-title', {
          duration: 1.5,
          y: 50,
          opacity: 0,
          ease: 'power3.out'
        }, '-=0.8')
        .from('.hero-subtitle', {
          duration: 1.2,
          y: 30,
          opacity: 0,
          ease: 'power2.out'
        }, '-=1')
        .from('.hero-buttons', {
          duration: 1,
          y: 20,
          opacity: 0,
          ease: 'power2.out'
        }, '-=0.8')
        .from('.liquid-glass-orb', {
          duration: 2,
          scale: 0,
          opacity: 0,
          ease: 'back.out(1.7)',
          stagger: 0.2
        }, '-=1.5');

      // Sparkle animation
      gsap.to('.sparkle', {
        scale: 1.2,
        opacity: 0.8,
        duration: 1.5,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        stagger: 0.3
      });
    }

    // Create firefly particles
    createFireflies();
    // Create liquid glass elements
    createLiquidGlass();
  });

  function createLiquidGlass() {
    if (!liquidGlassContainer) return;
    
    // Create floating glass orbs
    for (let i = 0; i < 6; i++) {
      const orb = document.createElement('div');
      orb.className = 'liquid-glass-orb';
      
      // Random positioning
      const x = 10 + Math.random() * 80;
      const y = 10 + Math.random() * 80;
      orb.style.left = x + '%';
      orb.style.top = y + '%';
      
      // Random size
      const size = 80 + Math.random() * 120;
      orb.style.width = size + 'px';
      orb.style.height = size + 'px';
      
      liquidGlassContainer.appendChild(orb);

      // Floating animation
      gsap.to(orb, {
        x: `+=${(Math.random() - 0.5) * 200}`,
        y: `+=${(Math.random() - 0.5) * 100}`,
        duration: 8 + Math.random() * 12,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 3
      });

      // Morphing animation
      gsap.to(orb, {
        scale: 0.8 + Math.random() * 0.4,
        duration: 6 + Math.random() * 6,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: Math.random() * 2
      });
    }

    // Create morphing blobs
    for (let i = 0; i < 3; i++) {
      const blob = document.createElement('div');
      blob.className = 'liquid-glass-blob';
      
      const x = 20 + Math.random() * 60;
      const y = 20 + Math.random() * 60;
      blob.style.left = x + '%';
      blob.style.top = y + '%';
      
      liquidGlassContainer.appendChild(blob);

      // Blob morphing
      gsap.to(blob, {
        borderRadius: '50% 30% 70% 40%',
        duration: 4,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut'
      });

      gsap.to(blob, {
        borderRadius: '30% 60% 40% 70%',
        duration: 6,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: 2
      });
    }
  }

  function createFireflies() {
    if (!fireflyContainer) return;
    
    const numFireflies = 15;
    // Theme-consistent colors - purple/violet palette
    const colors = [
      '#8B5CF6', // primary violet
      '#A855F7', // purple
      '#C084FC', // lighter purple  
      '#DDD6FE', // very light purple
      '#F3E8FF', // lavender
      '#E879F9', // fuchsia
      '#F0ABFC'  // light fuchsia
    ];

    for (let i = 0; i < numFireflies; i++) {
      const firefly = document.createElement('div');
      firefly.className = 'firefly';
      
      // Random starting position
      const startX = Math.random() * 100;
      const startY = Math.random() * 100;
      firefly.style.left = startX + '%';
      firefly.style.top = startY + '%';
      
      // Random theme color
      const color = colors[Math.floor(Math.random() * colors.length)];
      firefly.style.setProperty('--firefly-color', color);
      
      // Faster animation timing
      firefly.style.animationDelay = Math.random() * 5 + 's';
      firefly.style.animationDuration = (8 + Math.random() * 8) + 's';
      
      // Create multiple trail elements for better effect
      for (let j = 0; j < 3; j++) {
        const trail = document.createElement('div');
        trail.className = `firefly-trail trail-${j + 1}`;
        trail.style.animationDelay = (j * 0.1) + 's';
        firefly.appendChild(trail);
      }
      
      fireflyContainer.appendChild(firefly);

      // Faster GSAP animation for organic movement
      gsap.to(firefly, {
        x: `+=${(Math.random() - 0.5) * 300}`,
        y: `+=${(Math.random() - 0.5) * 200}`,
        duration: 4 + Math.random() * 6,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: Math.random() * 2
      });

      // Additional faster floating motion
      gsap.to(firefly, {
        x: `+=${(Math.random() - 0.5) * 80}`,
        y: `+=${(Math.random() - 0.5) * 60}`,
        duration: 1.5 + Math.random() * 2,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 1.5
      });

      // Quick micro movements for liveliness
      gsap.to(firefly, {
        x: `+=${(Math.random() - 0.5) * 20}`,
        y: `+=${(Math.random() - 0.5) * 20}`,
        duration: 0.8 + Math.random() * 0.7,
        repeat: -1,
        yoyo: true,
        ease: 'power2.inOut',
        delay: Math.random() * 1
      });
    }
  }
</script>

<section bind:this={heroSection} class="relative min-h-screen flex items-center justify-center overflow-hidden bg-background text-text-primary px-4 sm:px-6">
  <!-- Subtle cinematic background -->
  <div class="absolute inset-0 bg-gradient-to-b from-background via-background/95 to-background"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(99,102,241,0.03)_0%,transparent_70%)]"></div>
  
  <!-- Liquid Glass Background Elements -->
  <div bind:this={liquidGlassContainer} class="liquid-glass-container absolute inset-0 pointer-events-none z-0">
    <!-- Liquid glass elements will be generated here -->
  </div>
  
  <!-- Subtle grid pattern -->
  <div class="absolute inset-0 opacity-[0.02]" 
       style="background-image: linear-gradient(rgba(99,102,241,0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(99,102,241,0.3) 1px, transparent 1px); background-size: 50px 50px;"></div>
  
  <!-- Sparkle effects -->
  <div class="absolute inset-0 overflow-hidden pointer-events-none">
    <div class="sparkle absolute top-1/4 left-1/4 w-1 h-1 bg-primary rounded-full opacity-60"></div>
    <div class="sparkle absolute top-1/3 right-1/3 w-1 h-1 bg-secondary rounded-full opacity-40"></div>
    <div class="sparkle absolute bottom-1/4 left-1/3 w-1 h-1 bg-accent rounded-full opacity-50"></div>
    <div class="sparkle absolute top-2/3 right-1/4 w-1 h-1 bg-primary rounded-full opacity-30"></div>
    <div class="sparkle absolute bottom-1/3 right-2/3 w-1 h-1 bg-secondary rounded-full opacity-60"></div>
    <div class="sparkle absolute top-1/2 left-1/6 w-1 h-1 bg-accent rounded-full opacity-40"></div>
  </div>
  
  <!-- Firefly Particles -->
  <div bind:this={fireflyContainer} class="firefly-container pointer-events-none z-0">
    <!-- Firefly particles will be generated here -->
  </div>
  
  <!-- Content with enhanced glassmorphism -->
  <div class="container relative px-4 sm:px-6 md:px-8 z-10">
    <div class="max-w-4xl mx-auto text-center">
      <!-- Enhanced glass badge -->
      <div class="mb-6 sm:mb-8 inline-block hero-badge">
        <span class="liquid-glass-badge inline-block px-4 py-3 sm:px-6 sm:py-4 rounded-2xl text-xs sm:text-sm font-medium text-primary border border-primary/20">
          Welcome to Fletcraft Software
        </span>
      </div>
      
      <!-- Glass panel behind title -->
      <div class="liquid-glass-panel relative mb-6 sm:mb-8 p-6 sm:p-8 rounded-3xl">
        <h1 class="hero-title text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-display font-bold leading-tight relative z-10">
          <span class="bg-gradient-to-r from-text-primary via-primary to-text-primary bg-clip-text text-transparent">
            Crafting Digital
          </span>
          <br>
          <span class="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
            Excellence
          </span>
        </h1>
      </div>
      
      <p class="hero-subtitle text-base sm:text-lg md:text-xl text-text-secondary mb-8 sm:mb-12 max-w-2xl mx-auto leading-relaxed opacity-90">
        We transform visionary ideas into powerful software solutions that drive business growth and innovation in the digital age.
      </p>
      
      <div class="hero-buttons flex flex-col sm:flex-row flex-wrap gap-4 sm:gap-6 justify-center">
        <a href="#contact" 
          class="liquid-glass-button group relative px-6 sm:px-8 py-3 sm:py-4 overflow-hidden rounded-2xl transition-all duration-500 hover:scale-105">
          <span class="relative text-white font-medium flex items-center justify-center gap-2 z-10">
            Get Started
            <svg class="w-4 h-4 sm:w-5 sm:h-5 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </span>
        </a>
        
        <a href="#services" 
          class="liquid-glass-button-secondary group px-6 sm:px-8 py-3 sm:py-4 rounded-2xl transition-all duration-500 hover:scale-105">
          <span class="text-text-primary group-hover:text-primary font-medium flex items-center justify-center gap-2 transition-colors duration-300">
            <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
            </svg>
            Our Services
          </span>
        </a>
      </div>
    </div>
  </div>
  
  <!-- Scroll Indicator with glass effect -->
  <div class="absolute bottom-6 sm:bottom-8 left-1/2 transform -translate-x-1/2">
    <div class="liquid-glass-scroll flex flex-col items-center gap-2 text-text-secondary p-4 rounded-2xl">
      <span class="text-xs sm:text-sm font-medium">Scroll to explore</span>
      <svg class="w-4 h-4 sm:w-5 sm:h-5 animate-bounce-slow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </div>
</section>

<style>
  /* Liquid Glass Elements */
  .liquid-glass-container {
    overflow: hidden;
  }

  .liquid-glass-orb {
    position: absolute;
    background: linear-gradient(45deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.15));
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 50%;
    box-shadow: 
      0 8px 32px rgba(139, 92, 246, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
    will-change: transform;
  }

  .liquid-glass-blob {
    position: absolute;
    width: 150px;
    height: 150px;
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.08), rgba(192, 132, 252, 0.12));
    backdrop-filter: blur(15px);
    border: 1px solid rgba(139, 92, 246, 0.15);
    border-radius: 60% 40% 30% 70%;
    box-shadow: 
      0 10px 40px rgba(139, 92, 246, 0.08),
      inset 0 1px 0 rgba(255, 255, 255, 0.08);
    will-change: transform, border-radius;
  }

  .liquid-glass-badge {
    background: rgba(139, 92, 246, 0.1);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 
      0 8px 32px rgba(139, 92, 246, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
  }

  .liquid-glass-badge:hover {
    background: rgba(139, 92, 246, 0.15);
    transform: translateY(-2px);
    box-shadow: 
      0 12px 40px rgba(139, 92, 246, 0.15),
      inset 0 1px 0 rgba(255, 255, 255, 0.15);
  }

  .liquid-glass-panel {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(139, 92, 246, 0.1);
    box-shadow: 
      0 20px 60px rgba(139, 92, 246, 0.05),
      inset 0 1px 0 rgba(255, 255, 255, 0.05);
  }

  .liquid-glass-button {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.9), rgba(168, 85, 247, 0.9));
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.3);
    box-shadow: 
      0 10px 30px rgba(139, 92, 246, 0.2),
      inset 0 1px 0 rgba(255, 255, 255, 0.2);
    position: relative;
  }

  .liquid-glass-button::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .liquid-glass-button:hover::before {
    opacity: 1;
  }

  .liquid-glass-button:hover {
    box-shadow: 
      0 15px 40px rgba(139, 92, 246, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.3);
  }

  .liquid-glass-button-secondary {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 
      0 10px 30px rgba(139, 92, 246, 0.1),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
  }

  .liquid-glass-button-secondary:hover {
    background: rgba(139, 92, 246, 0.1);
    box-shadow: 
      0 15px 40px rgba(139, 92, 246, 0.15),
      inset 0 1px 0 rgba(255, 255, 255, 0.15);
  }

  .liquid-glass-scroll {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(139, 92, 246, 0.15);
    box-shadow: 
      0 8px 25px rgba(139, 92, 246, 0.08),
      inset 0 1px 0 rgba(255, 255, 255, 0.08);
    transition: all 0.3s ease;
  }

  .liquid-glass-scroll:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.05);
  }

  /* Sparkle animation */
  .sparkle {
    box-shadow: 0 0 6px currentColor;
    animation: sparkle-twinkle 3s ease-in-out infinite;
  }

  @keyframes sparkle-twinkle {
    0%, 100% { 
      opacity: 0.2;
      transform: scale(0.8);
    }
    50% { 
      opacity: 1;
      transform: scale(1.2);
      box-shadow: 0 0 12px currentColor;
    }
  }

  /* Enhanced button effects */
  .hero-buttons a::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.8s ease;
  }

  .hero-buttons a:hover::before {
    left: 100%;
  }
</style> 