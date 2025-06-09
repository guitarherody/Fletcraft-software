<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  const particleCount = 25; // Reduced for subtlety

  function createParticle() {
    const particle = document.createElement('div');
    particle.className = 'particle subtle-particle';
    
    // Random position
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    
    // Random animation duration and delay
    particle.style.animationDuration = (Math.random() * 20 + 30) + 's'; // Much slower
    particle.style.animationDelay = Math.random() * 30 + 's';
    
    // Subtle size
    const size = Math.random() * 2 + 1;
    particle.style.width = size + 'px';
    particle.style.height = size + 'px';
    
    // Subtle color variations (cooler tones)
    const hue = Math.random() * 40 + 220; // Blue range only
    particle.style.setProperty('--particle-hue', hue.toString());
    
    return particle;
  }

  onMount(() => {
    // Create subtle particles
    for (let i = 0; i < particleCount; i++) {
      const particle = createParticle();
      container.appendChild(particle);
      particles.push(particle);
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
    border-radius: 50%;
    animation: subtle-float linear infinite;
    pointer-events: none;
  }

  :global(.subtle-particle) {
    background: radial-gradient(circle, 
      hsl(var(--particle-hue, 240), 60%, 70%) 0%, 
      hsl(var(--particle-hue, 240), 40%, 60%) 40%, 
      transparent 70%);
    box-shadow: 0 0 4px hsl(var(--particle-hue, 240), 60%, 70%);
    opacity: 0.3;
  }

  @keyframes subtle-float {
    0% {
      transform: translateY(100vh) scale(0.8);
      opacity: 0;
    }
    10% {
      opacity: 0.3;
    }
    90% {
      opacity: 0.3;
    }
    100% {
      transform: translateY(-10vh) scale(1.1);
      opacity: 0;
    }
  }
</style> 