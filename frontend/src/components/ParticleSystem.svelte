<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 25; // More particles for space tunnel effect

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 15 : 25;
    
    createParticles();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 15 : 25;
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

  function createSpaceParticle() {
    const particle = document.createElement('div');
    particle.className = 'space-particle';
    
    // Create glowing core
    const core = document.createElement('div');
    core.className = 'particle-core';
    
    // Create trailing streaks
    const trail = document.createElement('div');
    trail.className = 'particle-trail';
    
    particle.appendChild(core);
    particle.appendChild(trail);
    
    return particle;
  }

  function createParticles() {
    if (!container) return;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = createSpaceParticle();
      
      // Start particles at random positions around the screen edges (simulating distance)
      const centerX = window.innerWidth / 2;
      const centerY = window.innerHeight / 2;
      
      // Create a circular starting area around the center (simulating far distance)
      const angle = Math.random() * Math.PI * 2;
      const radius = Math.random() * 100 + 50; // Small radius for "far away" effect
      const startX = centerX + Math.cos(angle) * radius;
      const startY = centerY + Math.sin(angle) * radius;
      
      // Calculate end position (much further out, past screen edges)
      const endRadius = Math.max(window.innerWidth, window.innerHeight) * 1.5;
      const endX = centerX + Math.cos(angle) * endRadius;
      const endY = centerY + Math.sin(angle) * endRadius;
      
      gsap.set(particle, {
        x: startX,
        y: startY,
        scale: 0.1, // Start very small (far away)
        opacity: 0.3,
      });
      
      container.appendChild(particle);
      particles.push(particle);
      
      // Create the space movement animation
      const createSpaceMovement = (element: HTMLElement, delay: number = 0) => {
        const duration = isMobile() ? 2.5 + Math.random() * 1.5 : 1.5 + Math.random() * 1; // Fast movement
        
        // Reset to starting position
        gsap.set(element, {
          x: startX,
          y: startY,
          scale: 0.1,
          opacity: 0.3,
        });
        
        // Animate toward viewer and through screen
        gsap.to(element, {
          x: endX,
          y: endY,
          scale: 3 + Math.random() * 2, // Get much larger as it approaches
          opacity: 1,
          duration: duration,
          ease: 'power2.in', // Accelerate as it approaches
          delay: delay,
          onUpdate: function() {
            // Add classes based on scale for trail effects
            const currentScale = gsap.getProperty(element, 'scale') as number;
            element.classList.remove('medium', 'large');
            if (currentScale > 2.5) {
              element.classList.add('large');
            } else if (currentScale > 1.5) {
              element.classList.add('medium');
            }
          },
          onComplete: () => {
            // Loop the animation with random delay
            const newDelay = Math.random() * 3;
            createSpaceMovement(element, newDelay);
          }
        });
        
        // Fade out near the end (as it passes through viewer)
        gsap.to(element, {
          opacity: 0,
          duration: duration * 0.3,
          delay: delay + duration * 0.7,
          ease: 'power2.out'
        });
      };
      
      // Start each particle with a random delay for staggered effect
      const initialDelay = Math.random() * 4;
      createSpaceMovement(particle, initialDelay);
      
      // Add subtle rotation for more dynamic effect
      gsap.to(particle, {
        rotation: 360,
        duration: 8 + Math.random() * 4,
        ease: 'none',
        repeat: -1
      });
    }
  }
</script>

<div bind:this={container} class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
  <!-- Particles will be added here dynamically -->
</div>

<style>
  :global(.space-particle) {
    position: absolute;
    pointer-events: none;
    filter: blur(0px);
    transition: filter 0.3s ease;
  }

  :global(.particle-core) {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      #E879F9 0%,
      #C084FC 30%,
      #A855F7 60%,
      #8B5CF6 100%
    );
    box-shadow: 
      0 0 6px #E879F9,
      0 0 12px #C084FC,
      0 0 18px #A855F7,
      0 0 24px rgba(139, 92, 246, 0.3);
    position: relative;
    z-index: 2;
  }

  :global(.particle-trail) {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 2px;
    height: 20px;
    background: linear-gradient(to bottom,
      transparent 0%,
      rgba(232, 121, 249, 0.8) 20%,
      rgba(192, 132, 252, 0.6) 50%,
      rgba(168, 85, 247, 0.4) 80%,
      transparent 100%
    );
    border-radius: 1px;
    z-index: 1;
    opacity: 0.7;
  }

  /* Enhanced glow effect that increases with scale */
  :global(.space-particle:hover) {
    filter: blur(1px);
  }

  :global(.space-particle.large) {
    filter: blur(1px);
  }

  /* Create streak effect as particles move fast */
  :global(.space-particle.medium .particle-trail) {
    height: 40px;
    opacity: 0.9;
  }

  :global(.space-particle.large .particle-trail) {
    height: 60px;
    opacity: 1;
    box-shadow: 0 0 8px rgba(232, 121, 249, 0.5);
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    :global(.particle-core) {
      width: 3px;
      height: 3px;
      box-shadow: 
        0 0 4px #E879F9,
        0 0 8px #C084FC,
        0 0 12px #A855F7;
    }
    
    :global(.particle-trail) {
      height: 15px;
    }
  }
</style>