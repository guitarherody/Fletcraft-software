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

<!-- Global Prismatic Light Effects -->
<div class="global-prismatic-effects">
  <!-- Elegant Prismatic Light Beams -->
  <div class="prismatic-light" style="top: 15vh; left: -250px; transform: rotate(8deg);"></div>
  <div class="prismatic-light" style="top: 45vh; left: -250px; transform: rotate(-12deg); animation-delay: 8s;"></div>
  <div class="prismatic-light" style="top: 75vh; left: -250px; transform: rotate(15deg); animation-delay: 16s;"></div>
  
  <!-- Subtle Rainbow Beams -->
  <div class="rainbow-beam" style="top: 25vh; left: -300px; transform: rotate(-6deg);"></div>
  <div class="rainbow-beam" style="top: 60vh; left: -300px; transform: rotate(10deg); animation-delay: 10s;"></div>
  <div class="rainbow-beam" style="top: 85vh; left: -300px; transform: rotate(-4deg); animation-delay: 20s;"></div>
</div>

<!-- Page content --> 