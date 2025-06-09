<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let heroSection: HTMLElement;

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
        .from('.dodecahedron', {
          duration: 2,
          scale: 0.7,
          opacity: 0,
          rotationY: 45,
          ease: 'power2.out'
        }, '-=1.5');

      // Continuous dodecahedron rotation
      gsap.to('.dodecahedron', {
        rotationY: 360,
        duration: 40,
        ease: 'none',
        repeat: -1
      });

      // Subtle floating animation for dodecahedron
      gsap.to('.dodecahedron', {
        y: '+=15',
        duration: 4,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1
      });

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
  });
</script>

<section bind:this={heroSection} class="relative min-h-screen flex items-center justify-center overflow-hidden bg-background text-text-primary">
  <!-- Subtle cinematic background -->
  <div class="absolute inset-0 bg-gradient-to-b from-background via-background/95 to-background"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(99,102,241,0.03)_0%,transparent_70%)]"></div>
  
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
  
  <!-- Dodecahedron (D12 Style) - Centered Behind Hero Text -->
  <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 pointer-events-none z-0">
    <div class="dodecahedron relative w-48 h-48 md:w-64 md:h-64">
      <!-- 12 pentagonal faces positioned like a real D12 -->
      <div class="d12-face face-1"></div>
      <div class="d12-face face-2"></div>
      <div class="d12-face face-3"></div>
      <div class="d12-face face-4"></div>
      <div class="d12-face face-5"></div>
      <div class="d12-face face-6"></div>
      <div class="d12-face face-7"></div>
      <div class="d12-face face-8"></div>
      <div class="d12-face face-9"></div>
      <div class="d12-face face-10"></div>
      <div class="d12-face face-11"></div>
      <div class="d12-face face-12"></div>
    </div>
  </div>
  
  <!-- Content -->
  <div class="container relative px-6 md:px-8 z-10">
    <div class="max-w-4xl mx-auto text-center">
      <div class="mb-8 inline-block hero-badge">
        <span class="inline-block px-4 py-2 rounded-full text-sm font-medium bg-primary/5 text-primary border border-primary/10 backdrop-blur-sm">
          Welcome to Fletcraft Software
        </span>
      </div>
      
      <h1 class="hero-title text-5xl md:text-7xl font-display font-bold mb-8 leading-tight">
        <span class="bg-gradient-to-r from-text-primary via-primary to-text-primary bg-clip-text text-transparent">
          Crafting Digital
        </span>
        <br>
        <span class="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
          Excellence
        </span>
      </h1>
      
      <p class="hero-subtitle text-lg md:text-xl text-text-secondary mb-12 max-w-2xl mx-auto leading-relaxed opacity-90">
        We transform visionary ideas into powerful software solutions that drive business growth and innovation in the digital age.
      </p>
      
      <div class="hero-buttons flex flex-wrap gap-6 justify-center">
        <a href="#contact" 
          class="group relative px-8 py-4 bg-primary overflow-hidden rounded-lg transition-all duration-500 hover:scale-105 hover:shadow-xl hover:shadow-primary/25">
          <div class="absolute inset-0 bg-gradient-to-r from-primary to-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <span class="relative text-white font-medium flex items-center gap-2">
            Get Started
            <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </span>
        </a>
        
        <a href="#services" 
          class="group px-8 py-4 border border-primary/20 rounded-lg transition-all duration-500 hover:border-primary/40 hover:scale-105 backdrop-blur-sm bg-background/30">
          <span class="text-text-primary group-hover:text-primary font-medium flex items-center gap-2 transition-colors duration-300">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
            </svg>
            Our Services
          </span>
        </a>
      </div>
    </div>
  </div>
  
  <!-- Scroll Indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 opacity-60">
    <div class="flex flex-col items-center gap-2 text-text-secondary animate-bounce-slow">
      <span class="text-sm font-medium">Scroll to explore</span>
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </div>
</section>

<style>
  /* D12 Dodecahedron styles */
  .dodecahedron {
    transform-style: preserve-3d;
    perspective: 1200px;
    filter: drop-shadow(0 8px 32px rgba(99, 102, 241, 0.2));
    opacity: 0.6; /* Subtle background presence */
  }

  .d12-face {
    position: absolute;
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, 
      rgba(99, 102, 241, 0.08) 0%, 
      rgba(139, 92, 246, 0.12) 30%,
      rgba(59, 130, 246, 0.10) 70%, 
      rgba(99, 102, 241, 0.06) 100%);
    border: 1px solid rgba(99, 102, 241, 0.15);
    border-radius: 6px;
    transform-origin: 32px 32px;
    backface-visibility: hidden;
    /* Perfect pentagon shape for D12 */
    clip-path: polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%);
    
    /* Subtle inner glow like a real dice */
    box-shadow: 
      inset 0 2px 6px rgba(255, 255, 255, 0.08),
      inset 0 -2px 4px rgba(0, 0, 0, 0.03),
      0 4px 16px rgba(99, 102, 241, 0.08);
  }

  /* Responsive face sizing for larger dodecahedron */
  @media (min-width: 768px) {
    .d12-face {
      width: 80px;
      height: 80px;
      transform-origin: 40px 40px;
    }
  }

  /* Geometrically accurate D12 face positioning - scaled up */
  /* Top cap (1 face) */
  .face-1 { transform: rotateX(-26.565deg) translateZ(56px); }
  
  /* Upper ring (5 faces) */
  .face-2 { transform: rotateY(0deg) rotateX(26.565deg) translateZ(56px); }
  .face-3 { transform: rotateY(72deg) rotateX(26.565deg) translateZ(56px); }
  .face-4 { transform: rotateY(144deg) rotateX(26.565deg) translateZ(56px); }
  .face-5 { transform: rotateY(216deg) rotateX(26.565deg) translateZ(56px); }
  .face-6 { transform: rotateY(288deg) rotateX(26.565deg) translateZ(56px); }
  
  /* Lower ring (5 faces) */
  .face-7 { transform: rotateY(36deg) rotateX(153.435deg) translateZ(56px); }
  .face-8 { transform: rotateY(108deg) rotateX(153.435deg) translateZ(56px); }
  .face-9 { transform: rotateY(180deg) rotateX(153.435deg) translateZ(56px); }
  .face-10 { transform: rotateY(252deg) rotateX(153.435deg) translateZ(56px); }
  .face-11 { transform: rotateY(324deg) rotateX(153.435deg) translateZ(56px); }
  
  /* Bottom cap (1 face) */
  .face-12 { transform: rotateX(180deg) rotateY(180deg) translateZ(56px); }

  /* Larger desktop version */
  @media (min-width: 768px) {
    .face-1 { transform: rotateX(-26.565deg) translateZ(70px); }
    .face-2 { transform: rotateY(0deg) rotateX(26.565deg) translateZ(70px); }
    .face-3 { transform: rotateY(72deg) rotateX(26.565deg) translateZ(70px); }
    .face-4 { transform: rotateY(144deg) rotateX(26.565deg) translateZ(70px); }
    .face-5 { transform: rotateY(216deg) rotateX(26.565deg) translateZ(70px); }
    .face-6 { transform: rotateY(288deg) rotateX(26.565deg) translateZ(70px); }
    .face-7 { transform: rotateY(36deg) rotateX(153.435deg) translateZ(70px); }
    .face-8 { transform: rotateY(108deg) rotateX(153.435deg) translateZ(70px); }
    .face-9 { transform: rotateY(180deg) rotateX(153.435deg) translateZ(70px); }
    .face-10 { transform: rotateY(252deg) rotateX(153.435deg) translateZ(70px); }
    .face-11 { transform: rotateY(324deg) rotateX(153.435deg) translateZ(70px); }
    .face-12 { transform: rotateX(180deg) rotateY(180deg) translateZ(70px); }
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