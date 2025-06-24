<script lang="ts">
  import { onMount } from 'svelte';

  onMount(() => {
    // Clean cinematic particle system
  });
</script>

<div class="particle-container">
  <!-- Cinematic Glowing Particles -->
  {#each Array(12) as _, i}
    <div class="cinematic-particle particle-{i + 1}"></div>
  {/each}
  
  <!-- Dynamic Light Rays -->
  {#each Array(3) as _, i}
    <div class="light-ray ray-{i + 1}"></div>
  {/each}
</div>

<style>
  .particle-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 1;
    overflow: hidden;
  }

  /* Cinematic Glowing Particles */
  .cinematic-particle {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 1) 0%,
      rgba(255, 255, 255, 0.8) 20%,
      rgba(255, 255, 255, 0.3) 60%,
      transparent 100%
    );
    filter: blur(0.5px);
    box-shadow: 
      0 0 8px rgba(255, 255, 255, 0.8),
      0 0 16px rgba(255, 255, 255, 0.4),
      0 0 24px rgba(255, 255, 255, 0.2);
    animation: cinematicFloat 15s ease-in-out infinite;
  }

  /* Dynamic Light Rays */
  .light-ray {
    position: absolute;
    width: 200px;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 255, 255, 0.1) 30%,
      rgba(255, 255, 255, 0.3) 50%,
      rgba(255, 255, 255, 0.1) 70%,
      transparent 100%
    );
    filter: blur(0.8px);
    animation: lightSweep 20s ease-in-out infinite;
    transform-origin: left center;
  }

  /* Particle Positions */
  .particle-1 {
    top: 20%;
    left: 15%;
    animation-delay: 0s;
  }
  
  .particle-2 {
    top: 60%;
    right: 25%;
    animation-delay: 2s;
  }
  
  .particle-3 {
    top: 35%;
    left: 70%;
    animation-delay: 4s;
  }
  
  .particle-4 {
    top: 80%;
    left: 40%;
    animation-delay: 6s;
  }
  
  .particle-5 {
    top: 15%;
    right: 15%;
    animation-delay: 8s;
  }
  
  .particle-6 {
    top: 75%;
    right: 8%;
    animation-delay: 10s;
  }
  
  .particle-7 {
    top: 45%;
    left: 8%;
    animation-delay: 12s;
  }
  
  .particle-8 {
    top: 25%;
    left: 45%;
    animation-delay: 1s;
  }
  
  .particle-9 {
    top: 85%;
    left: 75%;
    animation-delay: 3s;
  }
  
  .particle-10 {
    top: 55%;
    right: 45%;
    animation-delay: 5s;
  }
  
  .particle-11 {
    top: 10%;
    left: 85%;
    animation-delay: 7s;
  }
  
  .particle-12 {
    top: 90%;
    left: 25%;
    animation-delay: 9s;
  }

  /* Light Ray Positions */
  .ray-1 {
    top: 30%;
    left: -200px;
    transform: rotate(8deg);
    animation-delay: 0s;
  }
  
  .ray-2 {
    top: 65%;
    left: -200px;
    transform: rotate(-5deg);
    animation-delay: 7s;
  }
  
  .ray-3 {
    top: 85%;
    left: -200px;
    transform: rotate(12deg);
    animation-delay: 14s;
  }

  @keyframes cinematicFloat {
    0% {
      transform: translateY(0) scale(0.8);
      opacity: 0.6;
      filter: blur(0.5px) brightness(1);
    }
    25% {
      transform: translateY(-12px) scale(1);
      opacity: 1;
      filter: blur(0.3px) brightness(1.2);
    }
    50% {
      transform: translateY(-8px) scale(1.1);
      opacity: 0.9;
      filter: blur(0.4px) brightness(1.4);
    }
    75% {
      transform: translateY(-15px) scale(0.9);
      opacity: 0.7;
      filter: blur(0.6px) brightness(1.1);
    }
    100% {
      transform: translateY(0) scale(0.8);
      opacity: 0.6;
      filter: blur(0.5px) brightness(1);
    }
  }

  @keyframes lightSweep {
    0% {
      transform: translateX(-200px) scale(0.8);
      opacity: 0;
    }
    15% {
      opacity: 0.3;
      transform: translateX(0px) scale(1);
    }
    50% {
      opacity: 0.5;
      transform: translateX(50vw) scale(1.2);
    }
    85% {
      opacity: 0.2;
      transform: translateX(100vw) scale(0.9);
    }
    100% {
      transform: translateX(calc(100vw + 200px)) scale(0.8);
      opacity: 0;
    }
  }
</style>