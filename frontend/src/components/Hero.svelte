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
    
    // Completely clean - no floating cards for ultra-cinematic look
  }

  function createLiquidGlass() {
    if (!liquidGlassContainer) return;
    
    // Remove all morphing blobs for cleaner look
    // Focus only on warp speed particles
  }

  function createFireflies() {
    if (!fireflyContainer) return;
    
    // Create BLAZING WARP SPEED particle system - cinematic effect
    const numParticles = 40;
    const colors = ['#FFFFFF', '#C084FC', '#8B5CF6', '#A855F7'];

    for (let i = 0; i < numParticles; i++) {
      const particle = document.createElement('div');
      particle.className = 'warp-particle';
      
      // Start from left edge with varied vertical positions
      const startX = -5;
      const startY = 10 + Math.random() * 80;
      particle.style.left = startX + '%';
      particle.style.top = startY + '%';
      
      // Enhanced warp speed trail effect
      const color = colors[Math.floor(Math.random() * colors.length)];
      const brightness = Math.random() * 0.5 + 0.5; // 0.5 to 1.0
      
      // Core particle - more intense
      particle.style.width = '4px';
      particle.style.height = '1px';
      particle.style.background = color;
      particle.style.position = 'absolute';
      particle.style.filter = 'blur(0.3px)';
      particle.style.boxShadow = `0 0 12px ${color}, 0 0 24px ${color}80`;
             particle.style.opacity = brightness.toString();
      
      // Create longer trailing streaks for intense warp effect
      for (let j = 0; j < 5; j++) {
        const trail = document.createElement('div');
        trail.className = `warp-trail trail-${j + 1}`;
        trail.style.position = 'absolute';
        trail.style.width = `${20 + j * 12}px`;
        trail.style.height = '1px';
        trail.style.background = `linear-gradient(90deg, ${color}${90 - j * 15}, transparent)`;
        trail.style.left = `-${20 + j * 12}px`;
        trail.style.top = '0';
        trail.style.transformOrigin = 'left center';
        trail.style.opacity = `${0.9 - j * 0.15}`;
        trail.style.filter = 'blur(0.2px)';
        particle.appendChild(trail);
      }
      
      fireflyContainer.appendChild(particle);

      // ULTRA WARP SPEED animation - blazing fast
      gsap.fromTo(particle, 
        {
          x: '0vw',
          opacity: 0,
          scale: 0.3
        },
        {
          x: '150vw',
          opacity: brightness,
          scale: 1,
          duration: 0.4 + Math.random() * 0.8, // Much faster
          repeat: -1,
          ease: 'power4.out',
          delay: Math.random() * 3
        }
      );

      // Minimal vertical drift to maintain speed feeling
      gsap.to(particle, {
        y: `+=${(Math.random() - 0.5) * 15}`,
        duration: 0.8 + Math.random() * 0.5,
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: Math.random() * 0.5
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

    <!-- Clean Cinematic Title -->
    <div class="hero-title mb-8 relative">
      <h1 class="text-6xl md:text-8xl lg:text-9xl font-bold leading-tight tracking-tight">
        <span class="block bg-gradient-to-r from-white via-gray-200 to-white bg-clip-text text-transparent">
          Fletcraft
        </span>
        <span class="block text-2xl md:text-4xl lg:text-5xl bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent font-light tracking-wide mt-2">
          Software Excellence
        </span>
      </h1>
    </div>

    <!-- Clean Subtitle -->
    <div class="hero-subtitle mb-16">
      <p class="text-lg md:text-xl text-gray-400 leading-relaxed max-w-2xl mx-auto font-light">
        We transform ideas into stunning digital experiences using cutting-edge technology and innovative design.
      </p>
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


  </div>


</section>

<style>
  /* Cinematic Warp Speed Particle Effects */
  :global(.warp-particle) {
    position: absolute;
    pointer-events: none;
    will-change: transform;
    backface-visibility: hidden;
  }

  :global(.warp-trail) {
    position: absolute;
    pointer-events: none;
    will-change: transform;
  }

  /* Enhanced sparkle animation */
  :global(.sparkle) {
    box-shadow: 0 0 6px currentColor;
    animation: sparkle-glow 3s ease-in-out infinite;
  }

  @keyframes sparkle-glow {
    0%, 100% { 
      box-shadow: 0 0 6px currentColor;
      transform: scale(1);
    }
    50% { 
      box-shadow: 0 0 15px currentColor, 0 0 25px currentColor;
      transform: scale(1.1);
    }
  }

  /* Cinematic background */
  section {
    background: 
      radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.05) 0%, transparent 50%),
      radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.03) 0%, transparent 50%),
      linear-gradient(135deg, rgba(0, 0, 0, 0.98) 0%, rgba(10, 10, 10, 1) 100%);
  }

  /* Performance optimizations */
  section {
    transform: translateZ(0);
    will-change: transform;
  }

  /* Typography enhancements */
  h1 {
    text-shadow: 0 0 40px rgba(139, 92, 246, 0.3);
  }

  /* Clean animations */
  .hero-badge,
  .hero-title,
  .hero-subtitle,
  .hero-buttons {
    animation: fadeInUp 1s ease-out;
  }

  .hero-title {
    animation-delay: 0.2s;
  }

  .hero-subtitle {
    animation-delay: 0.4s;
  }

  .hero-buttons {
    animation-delay: 0.6s;
  }

  @keyframes fadeInUp {
    0% {
      opacity: 0;
      transform: translateY(30px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
     }
 </style> 