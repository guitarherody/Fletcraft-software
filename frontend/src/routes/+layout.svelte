<script lang="ts">
  import '../app.css';
  import { onMount } from 'svelte';

  let prismaticContainer: HTMLDivElement;

  onMount(() => {
    // Create global prismatic light effects
    createPrismaticLights();
    
    return () => {
      // Cleanup if needed
    };
  });

  function createPrismaticLights() {
    if (!prismaticContainer) return;

    // Create 4 prismatic light beams that drift across the screen
    for (let i = 0; i < 4; i++) {
      const light = document.createElement('div');
      light.className = 'prismatic-light';
      light.style.top = Math.random() * 100 + 'vh';
      light.style.left = '-400px';
      light.style.transform = `rotate(${Math.random() * 30 - 15}deg)`;
      light.style.animationDelay = Math.random() * 20 + 's';
      
      prismaticContainer.appendChild(light);
    }

    // Create 3 rainbow beams with different trajectories
    for (let i = 0; i < 3; i++) {
      const beam = document.createElement('div');
      beam.className = 'rainbow-beam';
      beam.style.top = Math.random() * 80 + 10 + 'vh';
      beam.style.left = '-500px';
      beam.style.transform = `rotate(${Math.random() * 40 - 20}deg)`;
      beam.style.animationDelay = Math.random() * 25 + 's';
      
      prismaticContainer.appendChild(beam);
    }
  }
</script>

<!-- Global Prismatic Light Container -->
<div bind:this={prismaticContainer} class="fixed inset-0 pointer-events-none z-0 overflow-hidden"></div>

<!-- Ominous Dynamic Lighting -->
<div class="global-lighting">
  <div class="dynamic-light" style="top: 25vh; left: -220px; animation-delay: 3s;"></div>
  <div class="dynamic-light" style="top: 65vh; left: -220px; animation-delay: 12s;"></div>
  <div class="dynamic-light" style="top: 85vh; left: -220px; animation-delay: 18s;"></div>
</div>

<!-- Page content --> 