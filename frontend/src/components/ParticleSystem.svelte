<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 80; // Much more particles for better ambiance

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 50 : 80;
    
    createParticles();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 50 : 80;
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
    
    // Random particle type
    const type = Math.random();
    if (type < 0.3) {
      particle.classList.add('sparkle');
    } else if (type < 0.6) {
      particle.classList.add('dot');
    } else {
      particle.classList.add('orb');
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
      
      // Random size
      const size = Math.random() * 4 + 2; // 2-6px
      
      // Set initial position and properties
      particle.style.left = x + 'px';
      particle.style.top = y + 'px';
      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.animationDelay = Math.random() * 10 + 's';
      particle.style.animationDuration = (15 + Math.random() * 25) + 's'; // 15-40s float time
      
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

  :global(.floating-particle.sparkle) {
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.8) 0%,
      rgba(232, 121, 249, 0.6) 50%,
      transparent 100%
    );
    border-radius: 50%;
    box-shadow: 
      0 0 6px rgba(255, 255, 255, 0.5),
      0 0 12px rgba(232, 121, 249, 0.3);
    animation: gentleFloat linear infinite, sparkle 3s ease-in-out infinite;
  }

  :global(.floating-particle.dot) {
    background: radial-gradient(circle, 
      rgba(192, 132, 252, 0.7) 0%,
      rgba(168, 85, 247, 0.4) 70%,
      transparent 100%
    );
    border-radius: 50%;
    box-shadow: 0 0 4px rgba(192, 132, 252, 0.4);
    animation: gentleFloat linear infinite, pulse 4s ease-in-out infinite;
  }

  :global(.floating-particle.orb) {
    background: radial-gradient(circle at 30% 30%, 
      rgba(139, 92, 246, 0.5) 0%,
      rgba(99, 102, 241, 0.3) 60%,
      transparent 100%
    );
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(2px);
    box-shadow: 
      0 0 8px rgba(139, 92, 246, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.2);
    animation: gentleFloat linear infinite, drift 6s ease-in-out infinite;
  }

  @keyframes gentleFloat {
    0% {
      transform: translateY(100vh) translateX(0px) rotate(0deg);
      opacity: 0;
    }
    10% {
      opacity: 1;
    }
    90% {
      opacity: 1;
    }
    100% {
      transform: translateY(-10vh) translateX(50px) rotate(180deg);
      opacity: 0;
    }
  }

  @keyframes sparkle {
    0%, 100% {
      transform: scale(1);
      filter: brightness(1);
    }
    50% {
      transform: scale(1.5);
      filter: brightness(1.5);
    }
  }

  @keyframes pulse {
    0%, 100% {
      transform: scale(1);
      opacity: 0.7;
    }
    50% {
      transform: scale(1.2);
      opacity: 1;
    }
  }

  @keyframes drift {
    0%, 100% {
      transform: translateX(0px);
    }
    25% {
      transform: translateX(-20px);
    }
    75% {
      transform: translateX(20px);
    }
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    :global(.floating-particle) {
      animation-duration: 20s, 4s;
    }
  }

  /* Performance optimizations */
  @media (prefers-reduced-motion: reduce) {
    :global(.floating-particle) {
      animation-duration: 30s;
      animation-timing-function: linear;
    }
    
    :global(.floating-particle.sparkle),
    :global(.floating-particle.dot),
    :global(.floating-particle.orb) {
      animation: gentleFloat 30s linear infinite;
    }
  }
</style>