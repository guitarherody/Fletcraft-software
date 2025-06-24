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

  /* Mysterious Glowing Particles */
  .cinematic-particle {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 120, 60, 1) 0%,
      rgba(255, 80, 40, 0.8) 20%,
      rgba(200, 60, 30, 0.4) 60%,
      transparent 100%
    );
    filter: blur(0.5px);
    box-shadow: 
      0 0 12px rgba(255, 100, 50, 0.9),
      0 0 24px rgba(255, 80, 40, 0.5),
      0 0 36px rgba(200, 60, 30, 0.3);
    animation: mysteriousFloat 12s ease-in-out infinite;
  }

  /* Dynamic Light Rays */
  .light-ray {
    position: absolute;
    width: 250px;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 100, 50, 0.1) 25%,
      rgba(255, 120, 60, 0.4) 50%,
      rgba(255, 100, 50, 0.1) 75%,
      transparent 100%
    );
    filter: blur(0.8px);
    animation: ominousLightSweep 18s ease-in-out infinite;
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

  @keyframes mysteriousFloat {
    0% {
      transform: translateY(0) translateX(0) scale(0.8) rotate(0deg);
      opacity: 0.6;
      filter: blur(0.5px) brightness(1) hue-rotate(0deg);
    }
    20% {
      transform: translateY(-20px) translateX(15px) scale(1.2) rotate(45deg);
      opacity: 1;
      filter: blur(0.3px) brightness(1.4) hue-rotate(15deg);
    }
    40% {
      transform: translateY(-35px) translateX(-8px) scale(0.9) rotate(90deg);
      opacity: 0.8;
      filter: blur(0.6px) brightness(1.1) hue-rotate(30deg);
    }
    60% {
      transform: translateY(-25px) translateX(25px) scale(1.3) rotate(135deg);
      opacity: 1.2;
      filter: blur(0.4px) brightness(1.6) hue-rotate(45deg);
    }
    80% {
      transform: translateY(-45px) translateX(-12px) scale(0.7) rotate(180deg);
      opacity: 0.7;
      filter: blur(0.7px) brightness(0.9) hue-rotate(60deg);
    }
    100% {
      transform: translateY(0) translateX(0) scale(0.8) rotate(225deg);
      opacity: 0.6;
      filter: blur(0.5px) brightness(1) hue-rotate(75deg);
    }
  }

  @keyframes ominousLightSweep {
    0% {
      transform: translateX(-250px) scale(0.8) rotate(0deg);
      opacity: 0;
      filter: hue-rotate(0deg) brightness(0.8);
    }
    15% {
      opacity: 0.4;
      transform: translateX(-50px) scale(1.1) rotate(3deg);
      filter: hue-rotate(20deg) brightness(1.2);
    }
    35% {
      opacity: 0.6;
      transform: translateX(30vw) scale(1.3) rotate(-2deg);
      filter: hue-rotate(40deg) brightness(1.5);
    }
    55% {
      opacity: 0.5;
      transform: translateX(60vw) scale(1.1) rotate(4deg);
      filter: hue-rotate(60deg) brightness(1.3);
    }
    75% {
      opacity: 0.3;
      transform: translateX(90vw) scale(0.9) rotate(-3deg);
      filter: hue-rotate(80deg) brightness(1.1);
    }
    85% {
      opacity: 0.1;
      transform: translateX(100vw) scale(0.8) rotate(2deg);
      filter: hue-rotate(90deg) brightness(0.9);
    }
    100% {
      transform: translateX(calc(100vw + 250px)) scale(0.6) rotate(5deg);
      opacity: 0;
      filter: hue-rotate(100deg) brightness(0.8);
    }
  }
</style>