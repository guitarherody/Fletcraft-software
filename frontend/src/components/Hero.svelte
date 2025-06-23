<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import LiquidGlass from './LiquidGlass.svelte';

  let heroSection: HTMLElement;
  let fireflyContainer: HTMLElement;
  let liquidGlassContainer: HTMLElement;
  let glassCardContainer: HTMLElement;

  onMount(() => {
    // Enhanced entrance animations with Apple-style easing
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
        }, '-=1.5')
        .from('.glass-feature-card', {
          duration: 1.5,
          y: 40,
          opacity: 0,
          ease: 'power2.out',
          stagger: 0.1
        }, '-=1.2');

      // Enhanced sparkle animation with liquid glass effect
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

    // Create enhanced firefly system
    createFireflies();
    // Create liquid glass background elements
    createLiquidGlass();
    // Create floating glass cards
    createFloatingGlassCards();
  });

  function createFloatingGlassCards() {
    if (!glassCardContainer) return;
    
    const cards = [
      { icon: '⚡', text: 'Lightning Fast', x: 15, y: 20 },
      { icon: '🎨', text: 'Beautiful Design', x: 75, y: 15 },
      { icon: '🚀', text: 'Modern Tech', x: 20, y: 70 },
      { icon: '💎', text: 'Premium Quality', x: 80, y: 75 }
    ];

    cards.forEach((card, i) => {
      const cardEl = document.createElement('div');
      cardEl.className = 'glass-feature-card absolute pointer-events-none';
      cardEl.style.left = card.x + '%';
      cardEl.style.top = card.y + '%';
      
      cardEl.innerHTML = `
        <div class="liquid-glass-enhanced flex items-center space-x-3 px-4 py-3 rounded-2xl">
          <span class="text-2xl">${card.icon}</span>
          <span class="text-sm font-medium text-white/80">${card.text}</span>
        </div>
      `;
      
      glassCardContainer.appendChild(cardEl);

      // Floating animation with Apple-style easing
      gsap.to(cardEl, {
        y: `+=${(Math.random() - 0.5) * 40}`,
        x: `+=${(Math.random() - 0.5) * 30}`,
        duration: 8 + Math.random() * 4,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: i * 0.5
      });

      // Subtle rotation
      gsap.to(cardEl, {
        rotation: `+=${(Math.random() - 0.5) * 10}`,
        duration: 12 + Math.random() * 6,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: i * 0.3
      });
    });
  }

  function createLiquidGlass() {
    if (!liquidGlassContainer) return;
    
    // Create morphing glass blobs with Apple-inspired shapes
    for (let i = 0; i < 4; i++) {
      const blob = document.createElement('div');
      blob.className = `liquid-glass-blob morph-${(i % 3) + 1}`;
      
      // Positioning with better distribution
      const x = 10 + (i * 20) + Math.random() * 15;
      const y = 15 + Math.random() * 70;
      blob.style.left = x + '%';
      blob.style.top = y + '%';
      
      // Size variation
      const size = 120 + Math.random() * 100;
      blob.style.width = size + 'px';
      blob.style.height = size + 'px';
      
      // Apple Liquid Glass styling
      blob.style.background = `
        linear-gradient(135deg, 
          rgba(99, 102, 241, 0.1) 0%,
          rgba(139, 92, 246, 0.08) 50%,
          rgba(168, 85, 247, 0.06) 100%
        )
      `;
      blob.style.backdropFilter = 'blur(30px) saturate(150%)';
      blob.style.border = '1px solid rgba(255, 255, 255, 0.1)';
      blob.style.boxShadow = `
        0 8px 32px rgba(139, 92, 246, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.1)
      `;
      blob.style.position = 'absolute';
      blob.style.filter = 'blur(0.5px)';
      
      liquidGlassContainer.appendChild(blob);

      // Floating animation with Apple-style physics
      gsap.to(blob, {
        x: `+=${(Math.random() - 0.5) * 150}`,
        y: `+=${(Math.random() - 0.5) * 80}`,
        duration: 15 + Math.random() * 10,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 5
      });

      // Scale pulsing
      gsap.to(blob, {
        scale: 0.8 + Math.random() * 0.4,
        duration: 8 + Math.random() * 4,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: Math.random() * 3
      });
    }

    // Create floating glass orbs
    for (let i = 0; i < 8; i++) {
      const orb = document.createElement('div');
      orb.className = 'liquid-glass-orb';
      
      // Better distribution across the hero area
      const x = 5 + Math.random() * 90;
      const y = 10 + Math.random() * 80;
      orb.style.left = x + '%';
      orb.style.top = y + '%';
      
      // Size variation
      const size = 60 + Math.random() * 80;
      orb.style.width = size + 'px';
      orb.style.height = size + 'px';
      orb.style.borderRadius = '50%';
      orb.style.position = 'absolute';
      
      // Apple glass styling with enhanced effects
      orb.style.background = `
        radial-gradient(circle at 30% 30%, 
          rgba(255, 255, 255, 0.15) 0%,
          rgba(99, 102, 241, 0.1) 40%,
          rgba(139, 92, 246, 0.05) 100%
        )
      `;
      orb.style.backdropFilter = 'blur(25px) saturate(180%)';
      orb.style.border = '1px solid rgba(255, 255, 255, 0.15)';
      orb.style.boxShadow = `
        0 8px 32px rgba(139, 92, 246, 0.12),
        inset 0 1px 0 rgba(255, 255, 255, 0.2),
        inset 0 -1px 0 rgba(99, 102, 241, 0.1)
      `;
      
      liquidGlassContainer.appendChild(orb);

      // Complex floating motion
      gsap.to(orb, {
        x: `+=${(Math.random() - 0.5) * 200}`,
        y: `+=${(Math.random() - 0.5) * 100}`,
        duration: 12 + Math.random() * 8,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 4
      });

      // Rotation animation
      gsap.to(orb, {
        rotation: 360,
        duration: 20 + Math.random() * 15,
        repeat: -1,
        ease: 'none'
      });

      // Scale animation
      gsap.to(orb, {
        scale: 0.7 + Math.random() * 0.6,
        duration: 6 + Math.random() * 4,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: Math.random() * 2
      });
    }
  }

  function createFireflies() {
    if (!fireflyContainer) return;
    
    const numFireflies = 20;
    // Enhanced color palette with Apple-inspired gradients
    const colors = [
      '#8B5CF6', '#A855F7', '#C084FC', '#DDD6FE', 
      '#F3E8FF', '#E879F9', '#F0ABFC', '#FBBF24'
    ];

    for (let i = 0; i < numFireflies; i++) {
      const firefly = document.createElement('div');
      firefly.className = 'firefly';
      
      // Random starting position
      const startX = Math.random() * 100;
      const startY = Math.random() * 100;
      firefly.style.left = startX + '%';
      firefly.style.top = startY + '%';
      
      // Enhanced styling with glass effect
      const color = colors[Math.floor(Math.random() * colors.length)];
      firefly.style.setProperty('--firefly-color', color);
      firefly.style.backdropFilter = 'blur(2px)';
      firefly.style.borderRadius = '50%';
      firefly.style.boxShadow = `0 0 10px ${color}, 0 0 20px ${color}40`;
      
      // Timing variations
      firefly.style.animationDelay = Math.random() * 5 + 's';
      firefly.style.animationDuration = (6 + Math.random() * 6) + 's';
      
      // Enhanced trail effect
      for (let j = 0; j < 4; j++) {
        const trail = document.createElement('div');
        trail.className = `firefly-trail trail-${j + 1}`;
        trail.style.animationDelay = (j * 0.08) + 's';
        firefly.appendChild(trail);
      }
      
      fireflyContainer.appendChild(firefly);

      // Enhanced organic movement with Apple-style easing
      gsap.to(firefly, {
        x: `+=${(Math.random() - 0.5) * 400}`,
        y: `+=${(Math.random() - 0.5) * 200}`,
        duration: 8 + Math.random() * 8,
        repeat: -1,
        yoyo: true,
        ease: 'power1.inOut',
        delay: Math.random() * 3
      });

      // Micro-movements for realism
      gsap.to(firefly, {
        x: `+=${(Math.random() - 0.5) * 60}`,
        y: `+=${(Math.random() - 0.5) * 40}`,
        duration: 2 + Math.random() * 2,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 1
      });
    }
  }
</script>

<section bind:this={heroSection} id="home" class="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-background via-background to-primary/5">
  <!-- Enhanced Background Effects -->
  <div bind:this={liquidGlassContainer} class="absolute inset-0 pointer-events-none overflow-hidden"></div>
  <div bind:this={fireflyContainer} class="absolute inset-0 pointer-events-none overflow-hidden"></div>
  <div bind:this={glassCardContainer} class="absolute inset-0 pointer-events-none overflow-hidden"></div>

  <!-- Main Content with Liquid Glass Container -->
  <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <!-- Hero Badge with Enhanced Glass Effect -->
    <div class="hero-badge mb-8">
      <LiquidGlass variant="button" intensity="medium" shimmer={true} className="inline-block">
        <div class="px-6 py-3 flex items-center space-x-2">
          <div class="sparkle w-2 h-2 bg-primary rounded-full"></div>
          <span class="text-sm font-semibold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
            ✨ Crafting Digital Excellence
          </span>
        </div>
      </LiquidGlass>
    </div>

    <!-- Enhanced Title with Glass Backdrop -->
    <div class="hero-title mb-6 relative">
      <div class="absolute inset-0 bg-glass-white-5 backdrop-blur-lg rounded-3xl opacity-50"></div>
      <h1 class="relative text-5xl md:text-7xl lg:text-8xl font-bold leading-tight">
        <span class="block bg-gradient-to-r from-white via-primary-200 to-white bg-clip-text text-transparent">
          Fletcraft
        </span>
        <span class="block text-3xl md:text-5xl lg:text-6xl bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent font-display">
          Software Excellence
        </span>
      </h1>
    </div>

    <!-- Enhanced Subtitle -->
    <div class="hero-subtitle mb-12">
      <LiquidGlass variant="panel" intensity="light" className="max-w-3xl mx-auto">
        <p class="text-lg md:text-xl text-text-secondary leading-relaxed px-8 py-6">
          We transform ideas into stunning digital experiences using cutting-edge technology and innovative design. 
          Your vision, our expertise, unlimited possibilities.
        </p>
      </LiquidGlass>
    </div>

    <!-- Enhanced CTA Buttons -->
    <div class="hero-buttons flex flex-col sm:flex-row items-center justify-center gap-6">
      <LiquidGlass variant="button" intensity="strong" shimmer={true} animated={true}>
        <a href="#contact" class="px-8 py-4 text-white font-semibold text-lg transition-all duration-300">
          Start Your Project
        </a>
      </LiquidGlass>
      
      <LiquidGlass variant="button" intensity="light" className="group">
        <a href="#portfolio" class="px-8 py-4 text-text-primary font-medium text-lg flex items-center space-x-2 transition-all duration-300">
          <span>View Our Work</span>
          <svg class="w-5 h-5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
          </svg>
        </a>
      </LiquidGlass>
    </div>

    <!-- Floating Statistics with Glass Morphism -->
    <div class="mt-20 grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto">
      {#each [
        { number: '50+', label: 'Projects Delivered' },
        { number: '98%', label: 'Client Satisfaction' },
        { number: '24/7', label: 'Support Available' },
        { number: '5★', label: 'Average Rating' }
      ] as stat, i}
        <LiquidGlass variant="card" intensity="medium" animated={true} className="stat-card">
          <div class="p-6 text-center">
            <div class="text-2xl md:text-3xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent mb-2">
              {stat.number}
            </div>
            <div class="text-sm text-text-secondary font-medium">
              {stat.label}
            </div>
          </div>
        </LiquidGlass>
      {/each}
    </div>
  </div>

  <!-- Enhanced scroll indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 z-10">
    <LiquidGlass variant="orb" size="sm" intensity="light" animated={true}>
      <div class="w-full h-full flex items-center justify-center">
        <svg class="w-6 h-6 text-primary animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
        </svg>
      </div>
    </LiquidGlass>
  </div>
</section>

<style>
  /* Enhanced firefly effects */
  :global(.firefly) {
    position: absolute;
    width: 3px;
    height: 3px;
    background: radial-gradient(circle, var(--firefly-color), transparent);
    border-radius: 50%;
    opacity: 0.8;
    pointer-events: none;
    filter: blur(0.5px);
  }

  :global(.firefly-trail) {
    position: absolute;
    width: 2px;
    height: 2px;
    background: var(--firefly-color);
    border-radius: 50%;
    opacity: 0.4;
    animation: firefly-fade 2s ease-in-out infinite;
  }

  :global(.firefly-trail.trail-1) { transform: translate(-4px, 0); }
  :global(.firefly-trail.trail-2) { transform: translate(-8px, 0); opacity: 0.25; }
  :global(.firefly-trail.trail-3) { transform: translate(-12px, 0); opacity: 0.15; }
  :global(.firefly-trail.trail-4) { transform: translate(-16px, 0); opacity: 0.05; }

  @keyframes firefly-fade {
    0%, 100% { opacity: 0; }
    50% { opacity: 0.6; }
  }

  /* Enhanced sparkle animation */
  :global(.sparkle) {
    box-shadow: 0 0 6px currentColor;
    animation: sparkle-glow 2s ease-in-out infinite;
  }

  @keyframes sparkle-glow {
    0%, 100% { 
      box-shadow: 0 0 6px currentColor;
      transform: scale(1);
    }
    50% { 
      box-shadow: 0 0 20px currentColor, 0 0 30px currentColor;
      transform: scale(1.2);
    }
  }

  /* Stat card hover effects */
  :global(.stat-card:hover) {
    transform: translateY(-4px) scale(1.02);
  }

  /* Improved glass morphism blur */
  :global(.liquid-glass-orb),
  :global(.liquid-glass-blob) {
    will-change: transform;
    backface-visibility: hidden;
  }

  /* Performance optimizations */
  section {
    transform: translateZ(0);
    will-change: transform;
  }
</style> 