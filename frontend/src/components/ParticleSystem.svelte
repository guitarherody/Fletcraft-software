<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 150; // Even more particles for firefly effect

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 100 : 150;
    
    createParticles();
    createLightRefractions();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 100 : 150;
      if (newParticleCount !== particleCount) {
        particleCount = newParticleCount;
        clearParticles();
        createParticles();
        createLightRefractions();
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

  function createLightRefractions() {
    if (!container) return;
    
    // Create 8 prismatic light beams
    for (let i = 0; i < 8; i++) {
      const lightBeam = document.createElement('div');
      lightBeam.className = `light-refraction refraction-${i + 1}`;
      
      // Random positioning
      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight;
      
      lightBeam.style.left = x + 'px';
      lightBeam.style.top = y + 'px';
      lightBeam.style.animationDelay = Math.random() * 10 + 's';
      
      container.appendChild(lightBeam);
      particles.push(lightBeam);
    }
    
    // Create 5 diamond sparkle points
    for (let i = 0; i < 5; i++) {
      const sparkle = document.createElement('div');
      sparkle.className = `diamond-sparkle sparkle-${i + 1}`;
      
      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight;
      
      sparkle.style.left = x + 'px';
      sparkle.style.top = y + 'px';
      sparkle.style.animationDelay = Math.random() * 8 + 's';
      
      container.appendChild(sparkle);
      particles.push(sparkle);
    }
  }

  function createFloatingParticle() {
    const particle = document.createElement('div');
    particle.className = 'floating-particle firefly';
    
    // Random firefly type
    const type = Math.random();
    if (type < 0.3) {
      particle.classList.add('firefly-warm');
    } else if (type < 0.6) {
      particle.classList.add('firefly-cool');
    } else {
      particle.classList.add('firefly-magic');
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
      
      // Firefly size range
      const size = Math.random() * 4 + 2; // 2-6px for more realistic firefly size
      
      // Set initial position and properties
      particle.style.left = x + 'px';
      particle.style.top = y + 'px';
      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.animationDelay = Math.random() * 15 + 's';
      particle.style.animationDuration = (20 + Math.random() * 25) + 's'; // Slower, more firefly-like
      
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
    animation: fireflyFloat linear infinite;
  }

  :global(.floating-particle.firefly) {
    border-radius: 50%;
  }

  /* Firefly Trail Effect */
  :global(.floating-particle.firefly::before) {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.3;
    z-index: -1;
    filter: blur(3px);
  }

  :global(.floating-particle.firefly::after) {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 600%;
    height: 600%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.1;
    z-index: -2;
    filter: blur(8px);
  }

  :global(.floating-particle.firefly-warm) {
    background: radial-gradient(circle, 
      rgba(255, 220, 120, 1) 0%,
      rgba(255, 180, 60, 0.9) 30%,
      rgba(255, 140, 40, 0.7) 60%,
      transparent 100%
    );
    box-shadow: 
      0 0 15px rgba(255, 200, 80, 1),
      0 0 30px rgba(255, 160, 50, 0.8),
      0 0 45px rgba(255, 140, 40, 0.6),
      0 0 60px rgba(255, 120, 30, 0.4);
    animation: fireflyFloat linear infinite, fireflyGlow 3s ease-in-out infinite;
  }

  :global(.floating-particle.firefly-warm::before) {
    background: radial-gradient(circle, 
      rgba(255, 200, 80, 0.4) 0%,
      rgba(255, 160, 50, 0.2) 50%,
      transparent 100%
    );
  }

  :global(.floating-particle.firefly-warm::after) {
    background: radial-gradient(circle, 
      rgba(255, 180, 60, 0.2) 0%,
      rgba(255, 140, 40, 0.1) 50%,
      transparent 100%
    );
  }

  :global(.floating-particle.firefly-cool) {
    background: radial-gradient(circle, 
      rgba(120, 220, 255, 1) 0%,
      rgba(80, 180, 255, 0.9) 30%,
      rgba(60, 140, 255, 0.7) 60%,
      transparent 100%
    );
    box-shadow: 
      0 0 15px rgba(100, 200, 255, 1),
      0 0 30px rgba(80, 180, 255, 0.8),
      0 0 45px rgba(60, 160, 255, 0.6),
      0 0 60px rgba(40, 140, 255, 0.4);
    animation: fireflyFloat linear infinite, fireflyPulse 4s ease-in-out infinite;
  }

  :global(.floating-particle.firefly-cool::before) {
    background: radial-gradient(circle, 
      rgba(100, 200, 255, 0.4) 0%,
      rgba(80, 180, 255, 0.2) 50%,
      transparent 100%
    );
  }

  :global(.floating-particle.firefly-cool::after) {
    background: radial-gradient(circle, 
      rgba(120, 220, 255, 0.2) 0%,
      rgba(100, 200, 255, 0.1) 50%,
      transparent 100%
    );
  }

  :global(.floating-particle.firefly-magic) {
    background: radial-gradient(circle, 
      rgba(220, 120, 255, 1) 0%,
      rgba(180, 80, 255, 0.9) 30%,
      rgba(140, 60, 255, 0.7) 60%,
      transparent 100%
    );
    box-shadow: 
      0 0 15px rgba(200, 100, 255, 1),
      0 0 30px rgba(180, 80, 255, 0.8),
      0 0 45px rgba(160, 60, 255, 0.6),
      0 0 60px rgba(140, 40, 255, 0.4);
    animation: fireflyFloat linear infinite, fireflySparkle 2.5s ease-in-out infinite;
  }

  :global(.floating-particle.firefly-magic::before) {
    background: radial-gradient(circle, 
      rgba(200, 100, 255, 0.4) 0%,
      rgba(180, 80, 255, 0.2) 50%,
      transparent 100%
    );
  }

  :global(.floating-particle.firefly-magic::after) {
    background: radial-gradient(circle, 
      rgba(220, 120, 255, 0.2) 0%,
      rgba(200, 100, 255, 0.1) 50%,
      transparent 100%
    );
  }

  @keyframes fireflyFloat {
    0% {
      transform: translateY(100vh) translateX(0px) rotate(0deg);
      opacity: 0;
    }
    5% {
      opacity: 0.4;
    }
    15% {
      opacity: 1;
    }
    85% {
      opacity: 1;
    }
    95% {
      opacity: 0.4;
    }
    100% {
      transform: translateY(-10vh) translateX(80px) rotate(180deg);
      opacity: 0;
    }
  }

  @keyframes fireflyGlow {
    0%, 100% {
      transform: scale(1);
      filter: brightness(1) blur(0px);
      box-shadow: 
        0 0 15px rgba(255, 200, 80, 1),
        0 0 30px rgba(255, 160, 50, 0.8),
        0 0 45px rgba(255, 140, 40, 0.6);
    }
    33% {
      transform: scale(1.3);
      filter: brightness(1.5) blur(0.5px);
      box-shadow: 
        0 0 25px rgba(255, 200, 80, 1),
        0 0 50px rgba(255, 160, 50, 1),
        0 0 75px rgba(255, 140, 40, 0.8),
        0 0 100px rgba(255, 120, 30, 0.6);
    }
    66% {
      transform: scale(0.8);
      filter: brightness(0.7) blur(0px);
      box-shadow: 
        0 0 10px rgba(255, 200, 80, 0.8),
        0 0 20px rgba(255, 160, 50, 0.6),
        0 0 30px rgba(255, 140, 40, 0.4);
    }
  }

  @keyframes fireflyPulse {
    0%, 100% {
      transform: scale(1);
      filter: brightness(1);
      box-shadow: 
        0 0 15px rgba(100, 200, 255, 1),
        0 0 30px rgba(80, 180, 255, 0.8),
        0 0 45px rgba(60, 160, 255, 0.6);
    }
    50% {
      transform: scale(1.2);
      filter: brightness(1.8);
      box-shadow: 
        0 0 30px rgba(100, 200, 255, 1),
        0 0 60px rgba(80, 180, 255, 1),
        0 0 90px rgba(60, 160, 255, 0.8),
        0 0 120px rgba(40, 140, 255, 0.6);
    }
  }

  @keyframes fireflySparkle {
    0%, 100% {
      transform: scale(1) rotate(0deg);
      filter: brightness(1) hue-rotate(0deg);
      box-shadow: 
        0 0 15px rgba(200, 100, 255, 1),
        0 0 30px rgba(180, 80, 255, 0.8),
        0 0 45px rgba(160, 60, 255, 0.6);
    }
    25% {
      transform: scale(1.4) rotate(90deg);
      filter: brightness(2) hue-rotate(30deg);
      box-shadow: 
        0 0 35px rgba(200, 100, 255, 1),
        0 0 70px rgba(180, 80, 255, 1),
        0 0 105px rgba(160, 60, 255, 0.8),
        0 0 140px rgba(140, 40, 255, 0.6);
    }
    50% {
      transform: scale(0.6) rotate(180deg);
      filter: brightness(0.5) hue-rotate(60deg);
      box-shadow: 
        0 0 8px rgba(200, 100, 255, 0.8),
        0 0 16px rgba(180, 80, 255, 0.6),
        0 0 24px rgba(160, 60, 255, 0.4);
    }
    75% {
      transform: scale(1.2) rotate(270deg);
      filter: brightness(1.7) hue-rotate(90deg);
      box-shadow: 
        0 0 28px rgba(200, 100, 255, 1),
        0 0 56px rgba(180, 80, 255, 0.9),
        0 0 84px rgba(160, 60, 255, 0.7);
    }
  }

  /* Enhanced responsiveness */
  @media (max-width: 768px) {
    :global(.floating-particle) {
      animation-duration: 25s, 4s;
    }
    
    :global(.floating-particle.firefly::before) {
      width: 250%;
      height: 250%;
      filter: blur(2px);
    }
    
    :global(.floating-particle.firefly::after) {
      width: 400%;
      height: 400%;
      filter: blur(5px);
    }
  }

  /* Performance optimizations */
  @media (prefers-reduced-motion: reduce) {
    :global(.floating-particle) {
      animation-duration: 50s;
      animation-timing-function: linear;
    }
    
    :global(.floating-particle.firefly-warm),
    :global(.floating-particle.firefly-cool),
    :global(.floating-particle.firefly-magic) {
      animation: fireflyFloat 50s linear infinite;
    }
    
    :global(.floating-particle.firefly::before),
    :global(.floating-particle.firefly::after) {
      display: none;
    }

    :global(.light-refraction),
    :global(.diamond-sparkle) {
      display: none;
    }
  }

  /* Diamond Light Refraction Effects */
  :global(.light-refraction) {
    position: absolute;
    width: 200px;
    height: 4px;
    pointer-events: none;
    transform-origin: left center;
    animation: refractionBeam 12s linear infinite;
    opacity: 0.7;
  }

  :global(.light-refraction::before) {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 0, 150, 0.8) 10%,
      rgba(255, 50, 0, 0.8) 20%,
      rgba(255, 200, 0, 0.8) 30%,
      rgba(150, 255, 0, 0.8) 40%,
      rgba(0, 255, 100, 0.8) 50%,
      rgba(0, 200, 255, 0.8) 60%,
      rgba(100, 0, 255, 0.8) 70%,
      rgba(255, 0, 200, 0.8) 80%,
      transparent 100%
    );
    filter: blur(1px);
    opacity: 0.6;
  }

  :global(.light-refraction::after) {
    content: '';
    position: absolute;
    top: -2px;
    left: 0;
    width: 100%;
    height: 8px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 255, 255, 0.4) 30%,
      rgba(255, 255, 255, 0.8) 50%,
      rgba(255, 255, 255, 0.4) 70%,
      transparent 100%
    );
    filter: blur(3px);
    opacity: 0.3;
  }

  :global(.refraction-1) {
    transform: rotate(15deg);
    animation-delay: 0s;
  }
  
  :global(.refraction-2) {
    transform: rotate(-25deg);
    animation-delay: 1.5s;
  }
  
  :global(.refraction-3) {
    transform: rotate(45deg);
    animation-delay: 3s;
  }
  
  :global(.refraction-4) {
    transform: rotate(-10deg);
    animation-delay: 4.5s;
  }
  
  :global(.refraction-5) {
    transform: rotate(35deg);
    animation-delay: 6s;
  }
  
  :global(.refraction-6) {
    transform: rotate(-45deg);
    animation-delay: 7.5s;
  }
  
  :global(.refraction-7) {
    transform: rotate(60deg);
    animation-delay: 9s;
  }
  
  :global(.refraction-8) {
    transform: rotate(-30deg);
    animation-delay: 10.5s;
  }

  /* Diamond Sparkle Points */
  :global(.diamond-sparkle) {
    position: absolute;
    width: 12px;
    height: 12px;
    pointer-events: none;
    animation: diamondSparkle 6s ease-in-out infinite;
  }

  :global(.diamond-sparkle::before) {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2px;
    height: 20px;
    background: linear-gradient(to bottom,
      transparent 0%,
      rgba(255, 255, 255, 1) 30%,
      rgba(255, 255, 255, 1) 70%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.5px);
    box-shadow: 
      0 0 10px rgba(255, 255, 255, 0.8),
      0 0 20px rgba(255, 255, 255, 0.6),
      0 0 30px rgba(255, 255, 255, 0.4);
  }

  :global(.diamond-sparkle::after) {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 2px;
    background: linear-gradient(to right,
      transparent 0%,
      rgba(255, 255, 255, 1) 30%,
      rgba(255, 255, 255, 1) 70%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.5px);
    box-shadow: 
      0 0 10px rgba(255, 255, 255, 0.8),
      0 0 20px rgba(255, 255, 255, 0.6),
      0 0 30px rgba(255, 255, 255, 0.4);
  }

  :global(.sparkle-1) {
    animation-delay: 0s;
  }
  
  :global(.sparkle-2) {
    animation-delay: 1.2s;
  }
  
  :global(.sparkle-3) {
    animation-delay: 2.4s;
  }
  
  :global(.sparkle-4) {
    animation-delay: 3.6s;
  }
  
  :global(.sparkle-5) {
    animation-delay: 4.8s;
  }

  @keyframes refractionBeam {
    0% {
      opacity: 0;
      transform: scale(0) translateX(-100px);
      filter: hue-rotate(0deg) brightness(0.5);
    }
    10% {
      opacity: 0.7;
      transform: scale(1) translateX(0px);
      filter: hue-rotate(30deg) brightness(1.5);
    }
    25% {
      opacity: 1;
      transform: scale(1.2) translateX(50px);
      filter: hue-rotate(90deg) brightness(2);
    }
    50% {
      opacity: 0.9;
      transform: scale(1) translateX(100px);
      filter: hue-rotate(180deg) brightness(1.8);
    }
    75% {
      opacity: 0.6;
      transform: scale(0.8) translateX(150px);
      filter: hue-rotate(270deg) brightness(1.2);
    }
    90% {
      opacity: 0.3;
      transform: scale(0.5) translateX(200px);
      filter: hue-rotate(330deg) brightness(0.8);
    }
    100% {
      opacity: 0;
      transform: scale(0) translateX(250px);
      filter: hue-rotate(360deg) brightness(0.5);
    }
  }

  @keyframes diamondSparkle {
    0% {
      transform: scale(0) rotate(0deg);
      opacity: 0;
      filter: brightness(1) blur(0px);
    }
    15% {
      transform: scale(1.5) rotate(45deg);
      opacity: 1;
      filter: brightness(2) blur(0.5px);
    }
    30% {
      transform: scale(1) rotate(90deg);
      opacity: 0.8;
      filter: brightness(1.5) blur(0px);
    }
    50% {
      transform: scale(1.8) rotate(180deg);
      opacity: 1;
      filter: brightness(2.5) blur(1px);
    }
    70% {
      transform: scale(1.2) rotate(270deg);
      opacity: 0.6;
      filter: brightness(1.8) blur(0.5px);
    }
    85% {
      transform: scale(0.8) rotate(315deg);
      opacity: 0.3;
      filter: brightness(1.2) blur(0px);
    }
    100% {
      transform: scale(0) rotate(360deg);
      opacity: 0;
      filter: brightness(1) blur(0px);
    }
  }
</style>