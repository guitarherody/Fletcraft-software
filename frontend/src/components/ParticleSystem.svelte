<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  let particleCount = 30; // More particles for dense warp effect

  // Detect if user is on mobile
  const isMobile = () => window.innerWidth < 768;
  
  onMount(() => {
    // Adjust particle count based on screen size
    particleCount = isMobile() ? 20 : 30;
    
    createParticles();
    
    // Handle resize
    const handleResize = () => {
      const newParticleCount = isMobile() ? 20 : 30;
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
    
    // Create trailing streak that will point toward center
    const trail = document.createElement('div');
    trail.className = 'particle-trail';
    
    particle.appendChild(core);
    particle.appendChild(trail);
    
    return particle;
  }

  function createParticles() {
    if (!container) return;
    
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;
    
    for (let i = 0; i < particleCount; i++) {
      const particle = createSpaceParticle();
      
      // Random angle for direction from center
      const angle = Math.random() * Math.PI * 2;
      
      // Start at center point (simulating infinite distance)
      const startX = centerX;
      const startY = centerY;
      
      // Calculate end position way past screen edges
      const maxDimension = Math.max(window.innerWidth, window.innerHeight);
      const endRadius = maxDimension * 2; // Go way beyond screen
      const endX = centerX + Math.cos(angle) * endRadius;
      const endY = centerY + Math.sin(angle) * endRadius;
      
      // Set initial position and properties
      gsap.set(particle, {
        x: startX,
        y: startY,
        scale: 0.05, // Start incredibly small
        opacity: 0,
        rotation: (angle * 180 / Math.PI) + 90 // Point trail toward center
      });
      
      container.appendChild(particle);
      particles.push(particle);
      
      // Create the warp-speed movement animation
      const createWarpMovement = (element: HTMLElement, delay: number = 0) => {
        const duration = isMobile() ? 1.8 + Math.random() * 0.8 : 1.2 + Math.random() * 0.6; // Very fast
        
        // Reset to center
        gsap.set(element, {
          x: startX,
          y: startY,
          scale: 0.05,
          opacity: 0,
        });
        
        // Fade in quickly
        gsap.to(element, {
          opacity: 1,
          duration: duration * 0.1,
          delay: delay,
          ease: 'power2.out'
        });
        
        // Main warp movement - exponential acceleration
        gsap.to(element, {
          x: endX,
          y: endY,
          scale: 8 + Math.random() * 4, // Massive scale increase
          duration: duration,
          ease: 'power4.in', // Very aggressive acceleration
          delay: delay,
          onUpdate: function() {
            // Dynamic trail effects based on progress
            const progress = this.progress();
            const currentScale = gsap.getProperty(element, 'scale') as number;
            
            element.classList.remove('small', 'medium', 'large', 'massive');
            
            if (currentScale > 6) {
              element.classList.add('massive');
            } else if (currentScale > 3) {
              element.classList.add('large');
            } else if (currentScale > 1) {
              element.classList.add('medium');
            } else {
              element.classList.add('small');
            }
            
            // Add motion blur effect as speed increases
            if (progress > 0.5) {
              element.style.filter = `blur(${(progress - 0.5) * 4}px)`;
            }
          },
          onComplete: () => {
            // Reset and loop with new random delay and angle
            const newDelay = Math.random() * 2;
            const newAngle = Math.random() * Math.PI * 2;
            const newEndX = centerX + Math.cos(newAngle) * endRadius;
            const newEndY = centerY + Math.sin(newAngle) * endRadius;
            
            // Update rotation for new direction
            gsap.set(element, {
              rotation: (newAngle * 180 / Math.PI) + 90
            });
            
            // Update end position
            gsap.to(element, {
              x: newEndX,
              y: newEndY,
              scale: 8 + Math.random() * 4,
              duration: duration,
              ease: 'power4.in',
              delay: newDelay,
              onUpdate: function() {
                const progress = this.progress();
                const currentScale = gsap.getProperty(element, 'scale') as number;
                
                element.classList.remove('small', 'medium', 'large', 'massive');
                
                if (currentScale > 6) {
                  element.classList.add('massive');
                } else if (currentScale > 3) {
                  element.classList.add('large');
                } else if (currentScale > 1) {
                  element.classList.add('medium');
                } else {
                  element.classList.add('small');
                }
                
                if (progress > 0.5) {
                  element.style.filter = `blur(${(progress - 0.5) * 4}px)`;
                }
              },
              onComplete: () => createWarpMovement(element, newDelay)
            });
          }
        });
        
        // Fade out as it gets very large (passing through viewer)
        gsap.to(element, {
          opacity: 0,
          duration: duration * 0.2,
          delay: delay + duration * 0.8,
          ease: 'power2.in'
        });
      };
      
      // Start each particle with a random delay for continuous effect
      const initialDelay = Math.random() * 3;
      createWarpMovement(particle, initialDelay);
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
    will-change: transform, opacity;
    transform-origin: center;
  }

  :global(.particle-core) {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      #E879F9 0%,
      #C084FC 40%,
      #A855F7 80%,
      transparent 100%
    );
    box-shadow: 
      0 0 4px #E879F9,
      0 0 8px #C084FC,
      0 0 12px rgba(232, 121, 249, 0.6);
    position: relative;
    z-index: 2;
  }

  :global(.particle-trail) {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 1px;
    height: 8px;
    background: linear-gradient(to top,
      transparent 0%,
      rgba(232, 121, 249, 0.9) 30%,
      rgba(192, 132, 252, 0.7) 70%,
      transparent 100%
    );
    border-radius: 0.5px;
    z-index: 1;
    opacity: 0.8;
  }

  /* Dynamic trail effects based on particle scale */
  :global(.space-particle.small .particle-trail) {
    height: 12px;
    width: 1px;
    opacity: 0.6;
  }

  :global(.space-particle.medium .particle-trail) {
    height: 25px;
    width: 2px;
    opacity: 0.8;
    box-shadow: 0 0 3px rgba(232, 121, 249, 0.4);
  }

  :global(.space-particle.large .particle-trail) {
    height: 45px;
    width: 3px;
    opacity: 1;
    box-shadow: 0 0 6px rgba(232, 121, 249, 0.6);
  }

  :global(.space-particle.massive .particle-trail) {
    height: 80px;
    width: 4px;
    opacity: 1;
    box-shadow: 
      0 0 8px rgba(232, 121, 249, 0.8),
      0 0 16px rgba(192, 132, 252, 0.4);
  }

  /* Enhanced core scaling */
  :global(.space-particle.medium .particle-core) {
    width: 4px;
    height: 4px;
    box-shadow: 
      0 0 6px #E879F9,
      0 0 12px #C084FC,
      0 0 18px rgba(232, 121, 249, 0.6);
  }

  :global(.space-particle.large .particle-core) {
    width: 6px;
    height: 6px;
    box-shadow: 
      0 0 8px #E879F9,
      0 0 16px #C084FC,
      0 0 24px rgba(232, 121, 249, 0.7);
  }

  :global(.space-particle.massive .particle-core) {
    width: 8px;
    height: 8px;
    box-shadow: 
      0 0 12px #E879F9,
      0 0 24px #C084FC,
      0 0 36px rgba(232, 121, 249, 0.8);
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    :global(.particle-core) {
      width: 2px;
      height: 2px;
    }
    
    :global(.particle-trail) {
      height: 6px;
    }
    
    :global(.space-particle.massive .particle-trail) {
      height: 60px;
      width: 3px;
    }
  }
</style>