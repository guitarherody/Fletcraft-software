<script lang="ts">
  import { onMount } from 'svelte';

  let container: HTMLDivElement;
  let particles: HTMLElement[] = [];
  const particleCount = 50; // Much smaller count for better performance

  function createParticle() {
    const particle = document.createElement('div');
    particle.className = 'particle';
    
    // Random position
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    
    // Random animation duration
    particle.style.animationDuration = (Math.random() * 20 + 10) + 's';
    particle.style.animationDelay = Math.random() * 20 + 's';
    
    // Random size
    const size = Math.random() * 4 + 2;
    particle.style.width = size + 'px';
    particle.style.height = size + 'px';
    
    return particle;
  }

  onMount(() => {
    // Create lightweight CSS particles
    for (let i = 0; i < particleCount; i++) {
      const particle = createParticle();
      container.appendChild(particle);
      particles.push(particle);
    }

    return () => {
      // Cleanup particles
      particles.forEach(particle => {
        if (particle.parentNode) {
          particle.parentNode.removeChild(particle);
        }
      });
    };
  });
</script>

<div bind:this={container} class="fixed inset-0 pointer-events-none z-0 overflow-hidden"></div>

<style>
  :global(.particle) {
    position: absolute;
    background: radial-gradient(circle, rgba(99,102,241,0.4) 0%, transparent 70%);
    border-radius: 50%;
    animation: float linear infinite;
    pointer-events: none;
  }

  @keyframes float {
    0% {
      transform: translateY(100vh) rotate(0deg);
      opacity: 0;
    }
    10% {
      opacity: 0.6;
    }
    90% {
      opacity: 0.6;
    }
    100% {
      transform: translateY(-100px) rotate(360deg);
      opacity: 0;
    }
  }
</style> 