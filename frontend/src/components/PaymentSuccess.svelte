<script lang="ts">
  import { onMount } from 'svelte';
  import ParticleSystem from './ParticleSystem.svelte';

  let paymentId = '';
  let merchantPaymentId = '';

  onMount(() => {
    // Get payment details from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    paymentId = urlParams.get('pf_payment_id') || '';
    merchantPaymentId = urlParams.get('m_payment_id') || '';
  });
</script>

<svelte:head>
  <title>Payment Successful - Fletcraft Software</title>
  <meta name="description" content="Your payment has been successfully processed. Thank you for choosing Fletcraft Software!" />
</svelte:head>

<!-- Background Particles -->
<ParticleSystem />

<!-- Fast Swirling Particles -->
<div class="swirling-particles">
  <div class="swirl-particle swirl-1"></div>
  <div class="swirl-particle swirl-2"></div>
  <div class="swirl-particle swirl-3"></div>
  <div class="swirl-particle swirl-4"></div>
  <div class="swirl-particle swirl-5"></div>
  <div class="swirl-particle swirl-6"></div>
  <div class="swirl-particle swirl-7"></div>
  <div class="swirl-particle swirl-8"></div>
  <div class="swirl-particle swirl-9"></div>
  <div class="swirl-particle swirl-10"></div>
  <div class="swirl-particle swirl-11"></div>
  <div class="swirl-particle swirl-12"></div>
</div>

<!-- Enhanced Particle-like Fireworks -->
<div class="fireworks-container">
  <div class="firework firework-1"></div>
  <div class="firework firework-2"></div>
  <div class="firework firework-3"></div>
  <div class="firework firework-4"></div>
  <div class="firework firework-5"></div>
  <div class="firework firework-6"></div>
</div>

<!-- Enhanced Particle Explosions -->
<div class="particle-explosions">
  <div class="explosion explosion-1"></div>
  <div class="explosion explosion-2"></div>
  <div class="explosion explosion-3"></div>
  <div class="explosion explosion-4"></div>
</div>

<!-- Floating Magic Particles -->
<div class="magic-particles">
  <div class="magic-particle magic-1"></div>
  <div class="magic-particle magic-2"></div>
  <div class="magic-particle magic-3"></div>
  <div class="magic-particle magic-4"></div>
  <div class="magic-particle magic-5"></div>
  <div class="magic-particle magic-6"></div>
  <div class="magic-particle magic-7"></div>
  <div class="magic-particle magic-8"></div>
  <div class="magic-particle magic-9"></div>
  <div class="magic-particle magic-10"></div>
</div>

<div class="min-h-screen bg-gradient-to-br from-gray-950 via-slate-900 to-gray-900 flex items-center justify-center p-4">
  <div class="relative z-10 w-full max-w-2xl">
    <div class="glass-dark text-center p-8 lg:p-12 rounded-2xl">
      
      <!-- Success Icon -->
      <div class="mb-8">
        <div class="w-24 h-24 mx-auto bg-gradient-to-br from-emerald-500 to-green-400 rounded-full flex items-center justify-center border-4 border-emerald-400/50 shadow-xl animate-pulse-glow">
          <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
          </svg>
        </div>
      </div>

      <!-- Success Message -->
      <h1 class="text-3xl lg:text-4xl font-bold text-white mb-4 animate-fadeInUp">
        Payment Successful!
      </h1>
      
      <p class="text-lg text-gray-300 mb-8 leading-relaxed animate-fadeInUp" style="animation-delay: 200ms;">
        Thank you for your purchase! Your payment has been successfully processed and we'll begin working on your project immediately.
      </p>

      <!-- Payment Details -->
      {#if paymentId || merchantPaymentId}
        <div class="glass-dark mb-8 p-6 text-left rounded-xl animate-fadeInUp border border-orange-500/20" style="animation-delay: 400ms;">
          <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
            <span class="w-2 h-2 bg-orange-400 rounded-full mr-3"></span>
            Payment Details
          </h3>
          {#if paymentId}
            <div class="mb-2">
              <span class="text-sm text-gray-400">PayFast Payment ID:</span>
              <div class="font-mono text-orange-400">{paymentId}</div>
            </div>
          {/if}
          {#if merchantPaymentId}
            <div class="mb-2">
              <span class="text-sm text-gray-400">Order Reference:</span>
              <div class="font-mono text-orange-400">{merchantPaymentId}</div>
            </div>
          {/if}
        </div>
      {/if}

      <!-- Next Steps -->
      <div class="glass-dark mb-8 p-6 text-left rounded-xl animate-fadeInUp border border-purple-500/20" style="animation-delay: 600ms;">
        <h3 class="text-lg font-semibold text-white mb-4 flex items-center">
          <span class="w-2 h-2 bg-purple-400 rounded-full mr-3"></span>
          What Happens Next?
        </h3>
        <div class="space-y-3 text-gray-300">
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-emerald-500/20 flex items-center justify-center mt-0.5 border border-emerald-400/30">
              <span class="text-emerald-400 text-sm font-bold">1</span>
            </div>
            <div>
              <div class="font-medium text-white">Confirmation Email</div>
              <div class="text-sm">You'll receive a confirmation email with your order details</div>
            </div>
          </div>
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-orange-500/20 flex items-center justify-center mt-0.5 border border-orange-400/30">
              <span class="text-orange-400 text-sm font-bold">2</span>
            </div>
            <div>
              <div class="font-medium text-white">Project Kickoff</div>
              <div class="text-sm">Our team will contact you within 24 hours to discuss your project</div>
            </div>
          </div>
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-purple-500/20 flex items-center justify-center mt-0.5 border border-purple-400/30">
              <span class="text-purple-400 text-sm font-bold">3</span>
            </div>
            <div>
              <div class="font-medium text-white">Development Begins</div>
              <div class="text-sm">We'll start working on your project with regular updates</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center animate-fadeInUp" style="animation-delay: 800ms;">
        <a href="/" class="inline-flex items-center space-x-2 px-8 py-4 bg-gradient-to-r from-orange-600 to-red-600 hover:from-orange-700 hover:to-red-700 text-white font-semibold rounded-lg transition-all duration-200 hover:scale-105 shadow-lg">
          <span>Return Home</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
          </svg>
        </a>

        <a href="/#contact" class="inline-flex items-center space-x-2 px-8 py-4 bg-white/10 text-white font-semibold rounded-lg backdrop-blur-sm border border-orange-400/30 hover:bg-orange-500/20 hover:border-orange-400/50 transition-all duration-200">
          <span>Contact Support</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
          </svg>
        </a>
      </div>

      <!-- Trust Badge -->
      <div class="mt-8 pt-6 border-t border-orange-400/20 animate-fadeInUp" style="animation-delay: 1000ms;">
        <div class="flex items-center justify-center space-x-2 text-gray-400">
          <svg class="w-5 h-5 text-emerald-400" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
          </svg>
          <span class="text-sm">Secured by PayFast - Payment processed successfully</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .animate-fadeInUp {
    animation: fadeInUp 0.8s ease-out both;
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(2rem);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .glass-dark {
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  }

  .animate-pulse-glow {
    animation: pulseGlow 2s ease-in-out infinite;
  }

  @keyframes pulseGlow {
    0%, 100% { 
      transform: scale(1);
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }
    50% { 
      transform: scale(1.05);
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.5);
    }
  }

  /* Enhanced Particle-like Fireworks */
  .fireworks-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .firework {
    position: absolute;
    width: 3px;
    height: 3px;
    border-radius: 50%;
    animation: particleFirework 4s ease-out infinite;
  }

  .firework-1 {
    top: 15%;
    left: 25%;
    background: radial-gradient(circle, #f97316, #ea580c);
    box-shadow: 0 0 6px #f97316, 0 0 12px #f97316;
    animation-delay: 0s;
  }

  .firework-2 {
    top: 25%;
    right: 20%;
    background: radial-gradient(circle, #a855f7, #9333ea);
    box-shadow: 0 0 6px #a855f7, 0 0 12px #a855f7;
    animation-delay: 1.2s;
  }

  .firework-3 {
    top: 65%;
    left: 35%;
    background: radial-gradient(circle, #10b981, #059669);
    box-shadow: 0 0 6px #10b981, 0 0 12px #10b981;
    animation-delay: 2.1s;
  }

  .firework-4 {
    top: 45%;
    right: 15%;
    background: radial-gradient(circle, #f59e0b, #d97706);
    box-shadow: 0 0 6px #f59e0b, 0 0 12px #f59e0b;
    animation-delay: 1.8s;
  }

  .firework-5 {
    top: 35%;
    left: 60%;
    background: radial-gradient(circle, #ec4899, #be185d);
    box-shadow: 0 0 6px #ec4899, 0 0 12px #ec4899;
    animation-delay: 0.7s;
  }

  .firework-6 {
    top: 70%;
    right: 40%;
    background: radial-gradient(circle, #06b6d4, #0891b2);
    box-shadow: 0 0 6px #06b6d4, 0 0 12px #06b6d4;
    animation-delay: 2.5s;
  }

  @keyframes particleFirework {
    0% {
      transform: scale(0) translate(0, 0);
      opacity: 0;
    }
    5% {
      transform: scale(1) translate(0, 0);
      opacity: 1;
    }
    15% {
      transform: scale(1.2) translate(0, 0);
      opacity: 1;
    }
    25% {
      transform: scale(0.8) translate(0, 0);
      opacity: 0.9;
      box-shadow: 
        0 0 0 0 currentColor,
        0 0 0 0 currentColor,
        0 0 0 0 currentColor,
        0 0 0 0 currentColor;
    }
    30% {
      transform: scale(0) translate(0, 0);
      opacity: 0;
    }
    35% {
      transform: scale(2) translate(0, 0);
      opacity: 1;
      box-shadow: 
        25px 0 0 -1px currentColor,
        -25px 0 0 -1px currentColor,
        0 25px 0 -1px currentColor,
        0 -25px 0 -1px currentColor,
        18px 18px 0 -1px currentColor,
        -18px -18px 0 -1px currentColor,
        18px -18px 0 -1px currentColor,
        -18px 18px 0 -1px currentColor,
        35px 10px 0 -1px currentColor,
        -35px -10px 0 -1px currentColor,
        10px 35px 0 -1px currentColor,
        -10px -35px 0 -1px currentColor;
    }
    50% {
      transform: scale(3) translate(0, 0);
      opacity: 0.8;
      box-shadow: 
        45px 0 0 -2px currentColor,
        -45px 0 0 -2px currentColor,
        0 45px 0 -2px currentColor,
        0 -45px 0 -2px currentColor,
        32px 32px 0 -2px currentColor,
        -32px -32px 0 -2px currentColor,
        32px -32px 0 -2px currentColor,
        -32px 32px 0 -2px currentColor,
        50px 15px 0 -2px currentColor,
        -50px -15px 0 -2px currentColor,
        15px 50px 0 -2px currentColor,
        -15px -50px 0 -2px currentColor,
        40px -20px 0 -2px currentColor,
        -40px 20px 0 -2px currentColor,
        20px -40px 0 -2px currentColor,
        -20px 40px 0 -2px currentColor;
    }
    70% {
      transform: scale(4) translate(0, 0);
      opacity: 0.4;
      box-shadow: 
        65px 0 0 -3px transparent,
        -65px 0 0 -3px transparent,
        0 65px 0 -3px transparent,
        0 -65px 0 -3px transparent,
        46px 46px 0 -3px transparent,
        -46px -46px 0 -3px transparent,
        46px -46px 0 -3px transparent,
        -46px 46px 0 -3px transparent,
        70px 20px 0 -3px transparent,
        -70px -20px 0 -3px transparent,
        20px 70px 0 -3px transparent,
        -20px -70px 0 -3px transparent,
        55px -30px 0 -3px transparent,
        -55px 30px 0 -3px transparent,
        30px -55px 0 -3px transparent,
        -30px 55px 0 -3px transparent;
    }
    100% {
      transform: scale(5) translate(0, 0);
      opacity: 0;
    }
  }

  /* Particle Explosions */
  .particle-explosions {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }

  .explosion {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    animation: particleExplosion 3s ease-out infinite;
  }

  .explosion-1 {
    top: 20%;
    left: 30%;
    background: radial-gradient(circle, #ffffff, #f97316);
    animation-delay: 0.5s;
  }

  .explosion-2 {
    top: 60%;
    right: 25%;
    background: radial-gradient(circle, #ffffff, #a855f7);
    animation-delay: 1.5s;
  }

  .explosion-3 {
    top: 40%;
    left: 70%;
    background: radial-gradient(circle, #ffffff, #10b981);
    animation-delay: 2.2s;
  }

  .explosion-4 {
    top: 75%;
    left: 20%;
    background: radial-gradient(circle, #ffffff, #ec4899);
    animation-delay: 0.8s;
  }

  @keyframes particleExplosion {
    0% {
      transform: scale(0);
      opacity: 0;
    }
    10% {
      transform: scale(1);
      opacity: 1;
      box-shadow: 
        0 0 0 0 currentColor,
        0 0 0 0 currentColor,
        0 0 0 0 currentColor,
        0 0 0 0 currentColor;
    }
    20% {
      transform: scale(1.5);
      opacity: 1;
      box-shadow: 
        15px 0 0 -1px currentColor,
        -15px 0 0 -1px currentColor,
        0 15px 0 -1px currentColor,
        0 -15px 0 -1px currentColor,
        11px 11px 0 -1px currentColor,
        -11px -11px 0 -1px currentColor,
        11px -11px 0 -1px currentColor,
        -11px 11px 0 -1px currentColor;
    }
    40% {
      transform: scale(2.5);
      opacity: 0.7;
      box-shadow: 
        30px 0 0 -2px currentColor,
        -30px 0 0 -2px currentColor,
        0 30px 0 -2px currentColor,
        0 -30px 0 -2px currentColor,
        21px 21px 0 -2px currentColor,
        -21px -21px 0 -2px currentColor,
        21px -21px 0 -2px currentColor,
        -21px 21px 0 -2px currentColor,
        35px 12px 0 -2px currentColor,
        -35px -12px 0 -2px currentColor,
        12px 35px 0 -2px currentColor,
        -12px -35px 0 -2px currentColor;
    }
    60% {
      transform: scale(3.5);
      opacity: 0.4;
      box-shadow: 
        45px 0 0 -3px transparent,
        -45px 0 0 -3px transparent,
        0 45px 0 -3px transparent,
        0 -45px 0 -3px transparent,
        32px 32px 0 -3px transparent,
        -32px -32px 0 -3px transparent,
        32px -32px 0 -3px transparent,
        -32px 32px 0 -3px transparent,
        50px 18px 0 -3px transparent,
        -50px -18px 0 -3px transparent,
        18px 50px 0 -3px transparent,
        -18px -50px 0 -3px transparent;
    }
    100% {
      transform: scale(4);
      opacity: 0;
    }
  }

  /* Floating Magic Particles */
  .magic-particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 3;
  }

  .magic-particle {
    position: absolute;
    width: 2px;
    height: 2px;
    border-radius: 50%;
    animation: magicFloat 8s linear infinite;
  }

  .magic-1 {
    top: 10%;
    left: 10%;
    background: radial-gradient(circle, #ffffff, #f97316);
    box-shadow: 0 0 4px #f97316;
    animation-delay: 0s;
  }

  .magic-2 {
    top: 90%;
    left: 80%;
    background: radial-gradient(circle, #ffffff, #a855f7);
    box-shadow: 0 0 4px #a855f7;
    animation-delay: 1s;
  }

  .magic-3 {
    top: 30%;
    right: 5%;
    background: radial-gradient(circle, #ffffff, #10b981);
    box-shadow: 0 0 4px #10b981;
    animation-delay: 2s;
  }

  .magic-4 {
    top: 70%;
    left: 15%;
    background: radial-gradient(circle, #ffffff, #ec4899);
    box-shadow: 0 0 4px #ec4899;
    animation-delay: 3s;
  }

  .magic-5 {
    top: 50%;
    left: 85%;
    background: radial-gradient(circle, #ffffff, #06b6d4);
    box-shadow: 0 0 4px #06b6d4;
    animation-delay: 4s;
  }

  .magic-6 {
    top: 20%;
    left: 50%;
    background: radial-gradient(circle, #ffffff, #f59e0b);
    box-shadow: 0 0 4px #f59e0b;
    animation-delay: 0.5s;
  }

  .magic-7 {
    top: 80%;
    right: 30%;
    background: radial-gradient(circle, #ffffff, #ef4444);
    box-shadow: 0 0 4px #ef4444;
    animation-delay: 1.5s;
  }

  .magic-8 {
    top: 40%;
    left: 25%;
    background: radial-gradient(circle, #ffffff, #8b5cf6);
    box-shadow: 0 0 4px #8b5cf6;
    animation-delay: 2.5s;
  }

  .magic-9 {
    top: 60%;
    right: 60%;
    background: radial-gradient(circle, #ffffff, #14b8a6);
    box-shadow: 0 0 4px #14b8a6;
    animation-delay: 3.5s;
  }

  .magic-10 {
    top: 25%;
    left: 75%;
    background: radial-gradient(circle, #ffffff, #f472b6);
    box-shadow: 0 0 4px #f472b6;
    animation-delay: 4.5s;
  }

  @keyframes magicFloat {
    0% {
      transform: translateY(0) translateX(0) scale(0);
      opacity: 0;
    }
    10% {
      transform: translateY(-20px) translateX(10px) scale(1);
      opacity: 1;
    }
    25% {
      transform: translateY(-60px) translateX(30px) scale(1.2);
      opacity: 1;
    }
    50% {
      transform: translateY(-120px) translateX(-20px) scale(0.8);
      opacity: 0.8;
    }
    75% {
      transform: translateY(-180px) translateX(40px) scale(1.1);
      opacity: 0.6;
    }
    90% {
      transform: translateY(-220px) translateX(0px) scale(0.5);
      opacity: 0.3;
    }
    100% {
      transform: translateY(-250px) translateX(-30px) scale(0);
      opacity: 0;
    }
  }

  /* Fast Swirling Particles */
  .swirling-particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
    overflow: hidden;
  }

  .swirl-particle {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    animation: swirl 4s linear infinite;
  }

  /* Orange Particles */
  .swirl-1 {
    top: 10%;
    left: 20%;
    background: radial-gradient(circle, #f97316, #ea580c);
    box-shadow: 0 0 10px #f97316;
    animation-delay: 0s;
    animation-duration: 3s;
  }

  .swirl-2 {
    top: 80%;
    left: 70%;
    background: radial-gradient(circle, #fb923c, #f97316);
    box-shadow: 0 0 8px #fb923c;
    animation-delay: 0.5s;
    animation-duration: 3.5s;
  }

  .swirl-3 {
    top: 30%;
    right: 15%;
    background: radial-gradient(circle, #fed7aa, #fdba74);
    box-shadow: 0 0 6px #fed7aa;
    animation-delay: 1s;
    animation-duration: 4s;
  }

  .swirl-4 {
    top: 60%;
    left: 10%;
    background: radial-gradient(circle, #ff6b35, #e55527);
    box-shadow: 0 0 12px #ff6b35;
    animation-delay: 1.5s;
    animation-duration: 2.8s;
  }

  /* Purple Particles */
  .swirl-5 {
    top: 25%;
    left: 60%;
    background: radial-gradient(circle, #a855f7, #9333ea);
    box-shadow: 0 0 10px #a855f7;
    animation-delay: 0.3s;
    animation-duration: 3.2s;
  }

  .swirl-6 {
    top: 70%;
    right: 25%;
    background: radial-gradient(circle, #c084fc, #a855f7);
    box-shadow: 0 0 8px #c084fc;
    animation-delay: 0.8s;
    animation-duration: 3.8s;
  }

  .swirl-7 {
    top: 45%;
    left: 80%;
    background: radial-gradient(circle, #e879f9, #d946ef);
    box-shadow: 0 0 9px #e879f9;
    animation-delay: 1.2s;
    animation-duration: 3.3s;
  }

  .swirl-8 {
    top: 15%;
    left: 45%;
    background: radial-gradient(circle, #8b5cf6, #7c3aed);
    box-shadow: 0 0 11px #8b5cf6;
    animation-delay: 1.8s;
    animation-duration: 2.9s;
  }

  /* Emerald Particles */
  .swirl-9 {
    top: 55%;
    left: 30%;
    background: radial-gradient(circle, #10b981, #059669);
    box-shadow: 0 0 10px #10b981;
    animation-delay: 0.2s;
    animation-duration: 3.6s;
  }

  .swirl-10 {
    top: 35%;
    right: 30%;
    background: radial-gradient(circle, #34d399, #10b981);
    box-shadow: 0 0 8px #34d399;
    animation-delay: 0.7s;
    animation-duration: 3.1s;
  }

  .swirl-11 {
    top: 75%;
    left: 50%;
    background: radial-gradient(circle, #6ee7b7, #34d399);
    box-shadow: 0 0 7px #6ee7b7;
    animation-delay: 1.3s;
    animation-duration: 3.7s;
  }

  .swirl-12 {
    top: 20%;
    left: 75%;
    background: radial-gradient(circle, #047857, #065f46);
    box-shadow: 0 0 9px #047857;
    animation-delay: 1.6s;
    animation-duration: 3.4s;
  }

  @keyframes swirl {
    0% {
      transform: translateX(0) translateY(0) rotate(0deg) scale(0);
      opacity: 0;
    }
    10% {
      opacity: 1;
      transform: translateX(10px) translateY(-10px) rotate(36deg) scale(1);
    }
    25% {
      transform: translateX(50px) translateY(-30px) rotate(90deg) scale(1.2);
    }
    50% {
      transform: translateX(100px) translateY(-20px) rotate(180deg) scale(1);
    }
    75% {
      transform: translateX(150px) translateY(-40px) rotate(270deg) scale(1.3);
    }
    90% {
      opacity: 1;
      transform: translateX(200px) translateY(-60px) rotate(324deg) scale(0.8);
    }
    100% {
      opacity: 0;
      transform: translateX(250px) translateY(-80px) rotate(360deg) scale(0);
    }
  }
</style> 