<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 120; // Increased particle count for more visibility

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 80 : 120;
    
    createParticles();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 80 : 120;
      if (newParticleCount !== particleCount) {
        particleCount = newParticleCount;
        clearParticles();
        createParticles();
      }
    };
    
    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
      clearParticles();
    };
  });

  function clearParticles() {
    particles.forEach(particle => {
      if (particle.parentNode) {
        particle.parentNode.removeChild(particle);
      }
    });
    particles = [];
  }

  function createFloatingParticle() {
    const particle = document.createElement('div');
    particle.className = 'floating-particle';
    
    // Random particle type with higher chance for visible types
    const type = Math.random();
    if (type < 0.4) {
      particle.classList.add('sparkle-bright');
    } else if (type < 0.7) {
      particle.classList.add('orb-bright');
    } else {
      particle.classList.add('glow-dot');
    }
    
    return particle;
  }

  function createParticles() {
    if (!container) return;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = createFloatingParticle();
      
      // Random starting position
      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight;
      
      // Larger, more visible size range
      const size = Math.random() * 6 + 3; // 3-9px instead of 2-6px
      
      // Set initial position and properties
      particle.style.left = x + 'px';
      particle.style.top = y + 'px';
      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.animationDelay = Math.random() * 10 + 's';
      particle.style.animationDuration = (12 + Math.random() * 20) + 's'; // 12-32s float time
      
      container.appendChild(particle);
      particles.push(particle);
    }
  }
</script>

<div bind:this={container} class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
  <!-- Particles will be added here dynamically -->
</div>

<style>
  :global(.floating-particle) {
    position: absolute;
    pointer-events: none;
    will-change: transform;
    animation: gentleFloat linear infinite;
  }

  :global(.floating-particle.sparkle-bright) {
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 1) 0%,
      rgba(249, 115, 22, 0.8) 30%,
      rgba(234, 88, 12, 0.6) 60%,
      transparent 100%
    );
    border-radius: 50%;
    box-shadow: 
      0 0 8px rgba(249, 115, 22, 0.8),
      0 0 16px rgba(234, 88, 12, 0.6),
      0 0 24px rgba(249, 115, 22, 0.4);
    animation: gentleFloat linear infinite, brightSparkle 2s ease-in-out infinite;
  }

  :global(.floating-particle.orb-bright) {
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.9) 0%,
      rgba(168, 85, 247, 0.8) 40%,
      rgba(147, 51, 234, 0.6) 70%,
      transparent 100%
    );
    border-radius: 50%;
    box-shadow: 
      0 0 10px rgba(168, 85, 247, 0.7),
      0 0 20px rgba(147, 51, 234, 0.5),
      0 0 30px rgba(168, 85, 247, 0.3);
    animation: gentleFloat linear infinite, orbPulse 3s ease-in-out infinite;
  }

  :global(.floating-particle.glow-dot) {
    background: radial-gradient(circle at 30% 30%, 
      rgba(255, 255, 255, 0.9) 0%,
      rgba(16, 185, 129, 0.8) 50%,
      rgba(5, 150, 105, 0.6) 80%,
      transparent 100%
    );
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(1px);
    box-shadow: 
      0 0 12px rgba(16, 185, 129, 0.6),
      0 0 24px rgba(5, 150, 105, 0.4),
      inset 0 1px 0 rgba(255, 255, 255, 0.4);
    animation: gentleFloat linear infinite, glowDrift 4s ease-in-out infinite;
  }

  @keyframes gentleFloat {
    0% {
      transform: translateY(100vh) translateX(0px) rotate(0deg);
      opacity: 0;
    }
    5% {
      opacity: 0.8;
    }
    10% {
      opacity: 1;
    }
    90% {
      opacity: 0.8;
    }
    100% {
      transform: translateY(-10vh) translateX(60px) rotate(180deg);
      opacity: 0;
    }
  }

  @keyframes brightSparkle {
    0%, 100% {
      transform: scale(1) rotate(0deg);
      filter: brightness(1);
      box-shadow: 
        0 0 8px rgba(249, 115, 22, 0.8),
        0 0 16px rgba(234, 88, 12, 0.6);
    }
    50% {
      transform: scale(1.5) rotate(180deg);
      filter: brightness(1.8);
      box-shadow: 
        0 0 16px rgba(249, 115, 22, 1),
        0 0 32px rgba(234, 88, 12, 0.8),
        0 0 48px rgba(249, 115, 22, 0.6);
    }
  }

  @keyframes orbPulse {
    0%, 100% {
      transform: scale(1);
      opacity: 0.8;
      box-shadow: 
        0 0 10px rgba(168, 85, 247, 0.7),
        0 0 20px rgba(147, 51, 234, 0.5);
    }
    50% {
      transform: scale(1.3);
      opacity: 1;
      box-shadow: 
        0 0 20px rgba(168, 85, 247, 1),
        0 0 40px rgba(147, 51, 234, 0.8),
        0 0 60px rgba(168, 85, 247, 0.6);
    }
  }

  @keyframes glowDrift {
    0%, 100% {
      transform: translateX(0px) scale(1);
      box-shadow: 
        0 0 12px rgba(16, 185, 129, 0.6),
        0 0 24px rgba(5, 150, 105, 0.4);
    }
    25% {
      transform: translateX(-30px) scale(1.1);
      box-shadow: 
        0 0 18px rgba(16, 185, 129, 0.8),
        0 0 36px rgba(5, 150, 105, 0.6);
    }
    75% {
      transform: translateX(30px) scale(0.9);
      box-shadow: 
        0 0 15px rgba(16, 185, 129, 0.7),
        0 0 30px rgba(5, 150, 105, 0.5);
    }
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    :global(.floating-particle) {
      animation-duration: 18s, 3s;
    }
  }

  /* Performance optimizations */
  @media (prefers-reduced-motion: reduce) {
    :global(.floating-particle) {
      animation-duration: 40s;
      animation-timing-function: linear;
    }
    
    :global(.floating-particle.sparkle-bright),
    :global(.floating-particle.orb-bright),
    :global(.floating-particle.glow-dot) {
      animation: gentleFloat 40s linear infinite;
    }
  }
</style>