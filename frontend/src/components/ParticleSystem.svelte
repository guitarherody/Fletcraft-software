<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 8; // Reduced for mobile performance

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 6 : 12;
    
    createParticles();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 6 : 12;
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

  function createDodecahedronParticle() {
    // Create main container
    const particle = document.createElement('div');
    particle.className = 'particle dodecahedron-particle';
    
    // Create dodecahedron structure
    const dodecahedron = document.createElement('div');
    dodecahedron.className = 'mini-dodecahedron';
    
    // Create 12 faces - simplified for mobile performance
    const faceCount = isMobile() ? 6 : 12; // Reduce faces on mobile
    for (let i = 1; i <= faceCount; i++) {
      const face = document.createElement('div');
      face.className = `mini-face mini-face-${i}`;
      dodecahedron.appendChild(face);
    }
    
    particle.appendChild(dodecahedron);
    return particle;
  }

  function createParticles() {
    if (!container) return;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = createDodecahedronParticle();
      
      // Random starting position
      const x = Math.random() * window.innerWidth;
      const y = Math.random() * window.innerHeight;
      
      gsap.set(particle, {
        x: x,
        y: y,
        scale: Math.random() * 0.3 + 0.2, // Smaller on mobile
        opacity: Math.random() * 0.4 + 0.1,
      });
      
      container.appendChild(particle);
      particles.push(particle);
      
      // Floating animation with reduced intensity for mobile
      const duration = isMobile() ? 60 + Math.random() * 40 : 40 + Math.random() * 30;
      const distance = isMobile() ? 15 : 25;
      
      gsap.to(particle, {
        x: `+=${Math.random() * distance * 2 - distance}`,
        y: `+=${Math.random() * distance * 2 - distance}`,
        rotation: 360,
        duration: duration,
        ease: 'none',
        repeat: -1,
        yoyo: true
      });
      
      // Individual dodecahedron rotation
      const dodecahedron = particle.querySelector('.mini-dodecahedron');
      if (dodecahedron) {
        gsap.to(dodecahedron, {
          rotationX: 360,
          rotationY: 360,
          duration: 30 + Math.random() * 20,
          ease: 'none',
          repeat: -1
        });
      }
    }
  }
</script>

<div bind:this={container} class="fixed inset-0 pointer-events-none z-0" style="perspective: 1000px;">
  <!-- Particles will be added here dynamically -->
</div>

<style>
  :global(.particle) {
    position: absolute;
    animation: subtle-float linear infinite;
    pointer-events: none;
    transform: scale(var(--particle-scale, 0.5));
  }

  :global(.dodecahedron-particle) {
    width: 16px;
    height: 16px;
    opacity: 0.4;
  }

  :global(.mini-dodecahedron) {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    perspective: 200px;
    position: relative;
  }

  :global(.mini-face) {
    position: absolute;
    width: 8px;
    height: 8px;
    background: linear-gradient(135deg, 
      hsla(var(--particle-hue, 240), 60%, 70%, 0.1) 0%, 
      hsla(var(--particle-hue, 240), 40%, 60%, 0.15) 50%, 
      hsla(var(--particle-hue, 240), 60%, 70%, 0.08) 100%);
    border: 0.5px solid hsla(var(--particle-hue, 240), 60%, 70%, 0.2);
    border-radius: 2px;
    transform-origin: center;
    clip-path: polygon(30% 0%, 70% 0%, 100% 35%, 82% 100%, 18% 100%, 0% 35%);
  }

  /* Mini dodecahedron face positioning */
  :global(.mini-face-1) { transform: translateZ(6px) rotateY(0deg); }
  :global(.mini-face-2) { transform: translateZ(6px) rotateY(72deg); }
  :global(.mini-face-3) { transform: translateZ(6px) rotateY(144deg); }
  :global(.mini-face-4) { transform: translateZ(6px) rotateY(216deg); }
  :global(.mini-face-5) { transform: translateZ(6px) rotateY(288deg); }
  :global(.mini-face-6) { transform: translateZ(-6px) rotateY(36deg); }
  :global(.mini-face-7) { transform: translateZ(-6px) rotateY(108deg); }
  :global(.mini-face-8) { transform: translateZ(-6px) rotateY(180deg); }
  :global(.mini-face-9) { transform: translateZ(-6px) rotateY(252deg); }
  :global(.mini-face-10) { transform: translateZ(-6px) rotateY(324deg); }
  :global(.mini-face-11) { transform: rotateX(90deg) translateZ(6px); }
  :global(.mini-face-12) { transform: rotateX(-90deg) translateZ(6px); }

  @keyframes subtle-float {
    0% {
      transform: translateY(100vh) scale(var(--particle-scale, 0.5)) rotate(0deg);
      opacity: 0;
    }
    10% {
      opacity: 0.4;
    }
    90% {
      opacity: 0.4;
    }
    100% {
      transform: translateY(-10vh) scale(calc(var(--particle-scale, 0.5) * 1.2)) rotate(180deg);
      opacity: 0;
    }
  }
</style>