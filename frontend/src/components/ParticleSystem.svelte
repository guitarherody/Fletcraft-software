<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  const particleCount = 15; // Reduced for subtlety and performance

  function createDodecahedronParticle() {
    // Create main container
    const particle = document.createElement('div');
    particle.className = 'particle dodecahedron-particle';
    
    // Create dodecahedron structure
    const dodecahedron = document.createElement('div');
    dodecahedron.className = 'mini-dodecahedron';
    
    // Create 12 faces
    for (let i = 1; i <= 12; i++) {
      const face = document.createElement('div');
      face.className = `mini-face mini-face-${i}`;
      dodecahedron.appendChild(face);
    }
    
    particle.appendChild(dodecahedron);
    
    // Random position
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    
    // Random animation duration and delay
    particle.style.animationDuration = (Math.random() * 25 + 35) + 's'; // Much slower
    particle.style.animationDelay = Math.random() * 30 + 's';
    
    // Subtle size variation
    const scale = Math.random() * 0.3 + 0.4;
    particle.style.setProperty('--particle-scale', scale.toString());
    
    // Subtle color variations (cooler tones)
    const hue = Math.random() * 40 + 220; // Blue range only
    particle.style.setProperty('--particle-hue', hue.toString());
    
    return particle;
  }

  onMount(() => {
    // Create subtle dodecahedron particles
    for (let i = 0; i < particleCount; i++) {
      const particle = createDodecahedronParticle();
      container.appendChild(particle);
      particles.push(particle);
      
      // Add individual rotation and bobbing animation
      const dodecahedron = particle.querySelector('.mini-dodecahedron');
      if (dodecahedron) {
        // Slow rotation
        gsap.to(dodecahedron, {
          rotationY: 360,
          duration: Math.random() * 20 + 40,
          ease: 'none',
          repeat: -1
        });
        
        // Subtle bobbing
        gsap.to(dodecahedron, {
          y: '+=8',
          duration: Math.random() * 2 + 3,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1
        });
      }
    }

    return () => {
      // Cleanup
      particles.forEach(element => {
        if (element.parentNode) {
          element.parentNode.removeChild(element);
        }
      });
    };
  });
</script>

<div bind:this={container} class="fixed inset-0 pointer-events-none z-0 overflow-hidden"></div>

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