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

<section bind:this={heroSection} class="relative min-h-screen flex items-center justify-center overflow-hidden bg-background text-text-primary px-4 sm:px-6">
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
  
  <!-- 3D Crystal with Light Source - Centered Behind Hero Text -->
  <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 pointer-events-none z-0">
    
    <!-- Light Source -->
    <div class="light-source">
      <div class="light-beam"></div>
      <div class="light-glow"></div>
    </div>
    
    <!-- Connected Crystal Container -->
    <div class="crystal-container">
      <div class="crystal-3d">
        
        <!-- Inner Core Light -->
        <div class="crystal-core-light"></div>
        
        <!-- Crystal SVG with Connected Faces -->
        <svg class="crystal-svg" width="120" height="160" viewBox="0 0 120 160">
          <defs>
            <!-- Crystal Gradients -->
            <linearGradient id="crystal-face-bright" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:0.9"/>
              <stop offset="30%" style="stop-color:#F0E6FF;stop-opacity:0.8"/>
              <stop offset="70%" style="stop-color:#E8D5FF;stop-opacity:0.6"/>
              <stop offset="100%" style="stop-color:#D4BDFF;stop-opacity:0.4"/>
            </linearGradient>
            
            <linearGradient id="crystal-face-lit" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#E8D5FF;stop-opacity:0.8"/>
              <stop offset="50%" style="stop-color:#D4BDFF;stop-opacity:0.7"/>
              <stop offset="100%" style="stop-color:#C4A5FF;stop-opacity:0.5"/>
            </linearGradient>
            
            <linearGradient id="crystal-face-medium" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#C4A5FF;stop-opacity:0.7"/>
              <stop offset="50%" style="stop-color:#A88BFA;stop-opacity:0.6"/>
              <stop offset="100%" style="stop-color:#9B7DF7;stop-opacity:0.5"/>
            </linearGradient>
            
            <linearGradient id="crystal-face-shadow" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#9B7DF7;stop-opacity:0.6"/>
              <stop offset="50%" style="stop-color:#8B6CF4;stop-opacity:0.5"/>
              <stop offset="100%" style="stop-color:#7C5CE3;stop-opacity:0.4"/>
            </linearGradient>
            
            <linearGradient id="crystal-face-dark" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#7C5CE3;stop-opacity:0.5"/>
              <stop offset="50%" style="stop-color:#6B5B95;stop-opacity:0.4"/>
              <stop offset="100%" style="stop-color:#4A4566;stop-opacity:0.3"/>
            </linearGradient>
            
            <!-- Light reflection filters -->
            <filter id="crystal-glow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
              <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
              </feMerge>
            </filter>
          </defs>
          
          <!-- Crystal Geometry - Properly Connected Crystal -->
          
          <!-- Top Point -->
          <polygon points="60,10 45,35 75,35" 
                   fill="url(#crystal-face-bright)" 
                   stroke="#FFFFFF" 
                   stroke-width="0.5" 
                   filter="url(#crystal-glow)"/>
          
          <!-- Upper Left Face -->
          <polygon points="45,35 20,60 50,85 60,60" 
                   fill="url(#crystal-face-lit)" 
                   stroke="#E8D5FF" 
                   stroke-width="0.3"/>
          
          <!-- Upper Right Face -->
          <polygon points="75,35 100,60 70,85 60,60" 
                   fill="url(#crystal-face-medium)" 
                   stroke="#D4BDFF" 
                   stroke-width="0.3"/>
          
          <!-- Center Front Face -->
          <polygon points="45,35 75,35 70,85 50,85" 
                   fill="url(#crystal-face-bright)" 
                   stroke="#F0E6FF" 
                   stroke-width="0.2" 
                   filter="url(#crystal-glow)"/>
          
          <!-- Middle Left Face -->
          <polygon points="20,60 10,95 40,125 50,85" 
                   fill="url(#crystal-face-shadow)" 
                   stroke="#C4A5FF" 
                   stroke-width="0.3"/>
          
          <!-- Middle Right Face -->
          <polygon points="100,60 110,95 80,125 70,85" 
                   fill="url(#crystal-face-shadow)" 
                   stroke="#A88BFA" 
                   stroke-width="0.3"/>
          
          <!-- Lower Left Face -->
          <polygon points="40,125 10,95 35,140 60,150" 
                   fill="url(#crystal-face-dark)" 
                   stroke="#9B7DF7" 
                   stroke-width="0.3"/>
          
          <!-- Lower Right Face -->
          <polygon points="80,125 110,95 85,140 60,150" 
                   fill="url(#crystal-face-dark)" 
                   stroke="#8B6CF4" 
                   stroke-width="0.3"/>
          
          <!-- Bottom Face -->
          <polygon points="50,85 70,85 80,125 40,125" 
                   fill="url(#crystal-face-medium)" 
                   stroke="#C4A5FF" 
                   stroke-width="0.2"/>
          
          <!-- Main Central Diamond -->
          <polygon points="60,60 50,85 60,110 70,85" 
                   fill="url(#crystal-face-bright)" 
                   stroke="#FFFFFF" 
                   stroke-width="0.4" 
                   filter="url(#crystal-glow)"/>
          
          <!-- Inner Highlights -->
          <line x1="45" y1="35" x2="75" y2="35" 
                stroke="#FFFFFF" 
                stroke-width="1.5" 
                opacity="0.8"/>
          <line x1="50" y1="85" x2="70" y2="85" 
                stroke="#FFFFFF" 
                stroke-width="1.2" 
                opacity="0.6"/>
          <line x1="60" y1="10" x2="60" y2="150" 
                stroke="#F0E6FF" 
                stroke-width="0.8" 
                opacity="0.4"/>
          
        </svg>
        
        <!-- Light Reflections -->
        <div class="light-reflections">
          <div class="reflection reflection-1"></div>
          <div class="reflection reflection-2"></div>
          <div class="reflection reflection-3"></div>
        </div>
        
      </div>
    </div>
  </div>
  
  <!-- Content -->
  <div class="container relative px-4 sm:px-6 md:px-8 z-10">
    <div class="max-w-4xl mx-auto text-center">
      <div class="mb-6 sm:mb-8 inline-block hero-badge">
        <span class="inline-block px-3 py-2 sm:px-4 rounded-full text-xs sm:text-sm font-medium bg-primary/5 text-primary border border-primary/10 backdrop-blur-sm">
          Welcome to Fletcraft Software
        </span>
      </div>
      
      <h1 class="hero-title text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-display font-bold mb-6 sm:mb-8 leading-tight">
        <span class="bg-gradient-to-r from-text-primary via-primary to-text-primary bg-clip-text text-transparent">
          Crafting Digital
        </span>
        <br>
        <span class="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
          Excellence
        </span>
      </h1>
      
      <p class="hero-subtitle text-base sm:text-lg md:text-xl text-text-secondary mb-8 sm:mb-12 max-w-2xl mx-auto leading-relaxed opacity-90">
        We transform visionary ideas into powerful software solutions that drive business growth and innovation in the digital age.
      </p>
      
      <div class="hero-buttons flex flex-col sm:flex-row flex-wrap gap-4 sm:gap-6 justify-center">
        <a href="#contact" 
          class="group relative px-6 sm:px-8 py-3 sm:py-4 bg-primary overflow-hidden rounded-lg transition-all duration-500 hover:scale-105 hover:shadow-xl hover:shadow-primary/25">
          <div class="absolute inset-0 bg-gradient-to-r from-primary to-secondary opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <span class="relative text-white font-medium flex items-center justify-center gap-2">
            Get Started
            <svg class="w-4 h-4 sm:w-5 sm:h-5 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </span>
        </a>
        
        <a href="#services" 
          class="group px-6 sm:px-8 py-3 sm:py-4 border border-primary/20 rounded-lg transition-all duration-500 hover:border-primary/40 hover:scale-105 backdrop-blur-sm bg-background/30">
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
  
  <!-- Scroll Indicator -->
  <div class="absolute bottom-6 sm:bottom-8 left-1/2 transform -translate-x-1/2 opacity-60">
    <div class="flex flex-col items-center gap-2 text-text-secondary animate-bounce-slow">
      <span class="text-xs sm:text-sm font-medium">Scroll to explore</span>
      <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
      </svg>
    </div>
  </div>
</section>

<style>
  /* D12 Dodecahedron styles - Enhanced realistic appearance */
  .dodecahedron-container {
    filter: drop-shadow(0 6px 20px rgba(180, 165, 119, 0.3));
    opacity: 0.7; /* More visible but still subtle */
  }

  .dodecahedron-svg {
    width: 120px;
    height: 120px;
    animation: dodecahedron-float 50s linear infinite, dodecahedron-bob 8s ease-in-out infinite;
  }

  @media (min-width: 640px) {
    .dodecahedron-container {
      filter: drop-shadow(0 8px 25px rgba(180, 165, 119, 0.35));
      opacity: 0.75;
    }
    
    .dodecahedron-svg {
      width: 160px;
      height: 160px;
    }
  }

  @media (min-width: 768px) {
    .dodecahedron-container {
      filter: drop-shadow(0 10px 30px rgba(180, 165, 119, 0.4));
      opacity: 0.8;
    }
    
    .dodecahedron-svg {
      width: 200px;
      height: 200px;
    }
  }

  @media (min-width: 1024px) {
    .dodecahedron-svg {
      width: 240px;
      height: 240px;
    }
  }

  .dodecahedron-3d {
    transform-origin: center;
    transform-style: preserve-3d;
  }

  /* Enhanced face styling for realistic 3D appearance */
  .d12-face {
    transition: all 0.3s ease;
  }

  .face-top {
    filter: brightness(1.2);
  }

  .face-middle {
    filter: brightness(1.0);
  }

  .face-shadow {
    filter: brightness(0.8);
  }

  .face-side {
    filter: brightness(0.9);
  }

  .face-center {
    filter: brightness(1.1);
  }

  /* Subtle glow effect around the entire dodecahedron */
  .dodecahedron-svg:hover {
    filter: drop-shadow(0 0 15px rgba(244, 228, 188, 0.4));
  }

  /* Animation keyframes for floating and bobbing */
  @keyframes dodecahedron-float {
    from { transform: rotateY(0deg) rotateX(5deg); }
    to { transform: rotateY(360deg) rotateX(5deg); }
  }

  @keyframes dodecahedron-bob {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
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