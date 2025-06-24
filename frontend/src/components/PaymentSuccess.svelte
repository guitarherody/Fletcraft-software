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

<!-- Clean Success Celebration -->
<div class="success-celebration">
  <div class="celebration-particle cel-1"></div>
  <div class="celebration-particle cel-2"></div>
  <div class="celebration-particle cel-3"></div>
  <div class="celebration-particle cel-4"></div>
  <div class="celebration-particle cel-5"></div>
  <div class="celebration-particle cel-6"></div>
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
  }

  /* Clean Success Celebration */
  .success-celebration {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }

  .celebration-particle {
    position: absolute;
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 1) 0%,
      rgba(255, 255, 255, 0.6) 40%,
      transparent 100%
    );
    filter: blur(0.3px);
    box-shadow: 
      0 0 8px rgba(255, 255, 255, 0.8),
      0 0 16px rgba(255, 255, 255, 0.4);
    animation: celebrationFloat 6s ease-in-out infinite;
  }

  .cel-1 {
    top: 20%;
    left: 25%;
    animation-delay: 0s;
  }

  .cel-2 {
    top: 15%;
    right: 30%;
    animation-delay: 1s;
  }

  .cel-3 {
    top: 35%;
    left: 70%;
    animation-delay: 2s;
  }

  .cel-4 {
    top: 60%;
    left: 15%;
    animation-delay: 3s;
  }

  .cel-5 {
    top: 75%;
    right: 25%;
    animation-delay: 4s;
  }

  .cel-6 {
    top: 45%;
    right: 15%;
    animation-delay: 5s;
  }

  @keyframes celebrationFloat {
    0% {
      transform: translateY(0) scale(0.8);
      opacity: 0.6;
    }
    25% {
      transform: translateY(-20px) scale(1.2);
      opacity: 1;
    }
    50% {
      transform: translateY(-10px) scale(1);
      opacity: 0.8;
    }
    75% {
      transform: translateY(-25px) scale(1.1);
      opacity: 0.9;
    }
         100% {
       transform: translateY(0) scale(0.8);
       opacity: 0.6;
     }
   }

   .glass-dark {
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

  /* Enhanced firefly-like fireworks */
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
    width: 8px;
    height: 8px;
    border-radius: 50%;
    animation: fireworkExplode 4s ease-out infinite;
  }

  /* Firefly trail effects for fireworks */
  .firework::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 500%;
    height: 500%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.4;
    z-index: -1;
    filter: blur(8px);
    background: inherit;
  }

  .firework::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 1000%;
    height: 1000%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.15;
    z-index: -2;
    filter: blur(20px);
    background: inherit;
  }

  .firework-1 {
    top: 15%;
    left: 20%;
    background: radial-gradient(circle, rgba(255, 220, 120, 1), rgba(255, 180, 60, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(255, 200, 80, 1),
      0 0 60px rgba(255, 160, 50, 0.8),
      0 0 90px rgba(255, 140, 40, 0.6),
      0 0 120px rgba(255, 120, 30, 0.4);
    animation-delay: 0s;
  }

  .firework-2 {
    top: 25%;
    right: 15%;
    background: radial-gradient(circle, rgba(200, 120, 255, 1), rgba(180, 80, 255, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(200, 100, 255, 1),
      0 0 60px rgba(180, 80, 255, 0.8),
      0 0 90px rgba(160, 60, 255, 0.6),
      0 0 120px rgba(140, 40, 255, 0.4);
    animation-delay: 1s;
  }

  .firework-3 {
    top: 10%;
    left: 50%;
    background: radial-gradient(circle, rgba(120, 255, 180, 1), rgba(80, 255, 140, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(100, 255, 160, 1),
      0 0 60px rgba(80, 255, 140, 0.8),
      0 0 90px rgba(60, 255, 120, 0.6),
      0 0 120px rgba(40, 255, 100, 0.4);
    animation-delay: 2s;
  }

  .firework-4 {
    top: 30%;
    left: 80%;
    background: radial-gradient(circle, rgba(255, 120, 180, 1), rgba(255, 80, 140, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(255, 100, 160, 1),
      0 0 60px rgba(255, 80, 140, 0.8),
      0 0 90px rgba(255, 60, 120, 0.6),
      0 0 120px rgba(255, 40, 100, 0.4);
    animation-delay: 0.5s;
  }

  .firework-5 {
    top: 35%;
    left: 10%;
    background: radial-gradient(circle, rgba(120, 220, 255, 1), rgba(80, 180, 255, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(100, 200, 255, 1),
      0 0 60px rgba(80, 180, 255, 0.8),
      0 0 90px rgba(60, 160, 255, 0.6),
      0 0 120px rgba(40, 140, 255, 0.4);
    animation-delay: 1.5s;
  }

  .firework-6 {
    top: 20%;
    right: 30%;
    background: radial-gradient(circle, rgba(255, 200, 120, 1), rgba(255, 180, 80, 0.8), transparent);
    box-shadow: 
      0 0 30px rgba(255, 180, 100, 1),
      0 0 60px rgba(255, 160, 80, 0.8),
      0 0 90px rgba(255, 140, 60, 0.6),
      0 0 120px rgba(255, 120, 40, 0.4);
    animation-delay: 2.5s;
  }

  /* Particle explosion effects with firefly trails */
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
    width: 6px;
    height: 6px;
    border-radius: 50%;
    animation: particleExplode 3s ease-out infinite;
  }

  .particle-explosion::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.4;
    z-index: -1;
    filter: blur(4px);
    background: inherit;
  }

  .particle-explosion::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 600%;
    height: 600%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.2;
    z-index: -2;
    filter: blur(10px);
    background: inherit;
  }

  .explosion-1 {
    top: 40%;
    left: 25%;
    background: radial-gradient(circle, rgba(255, 160, 120, 1), rgba(255, 140, 80, 0.8), transparent);
    box-shadow: 
      0 0 25px rgba(255, 140, 100, 1),
      0 0 50px rgba(255, 120, 80, 0.8),
      0 0 75px rgba(255, 100, 60, 0.6);
    animation-delay: 3s;
  }

  .explosion-2 {
    top: 60%;
    right: 20%;
    background: radial-gradient(circle, rgba(180, 120, 255, 1), rgba(160, 80, 255, 0.8), transparent);
    box-shadow: 
      0 0 25px rgba(160, 100, 255, 1),
      0 0 50px rgba(140, 80, 255, 0.8),
      0 0 75px rgba(120, 60, 255, 0.6);
    animation-delay: 3.5s;
  }

  .explosion-3 {
    top: 45%;
    left: 70%;
    background: radial-gradient(circle, rgba(120, 255, 160, 1), rgba(80, 255, 120, 0.8), transparent);
    box-shadow: 
      0 0 25px rgba(100, 255, 140, 1),
      0 0 50px rgba(80, 255, 120, 0.8),
      0 0 75px rgba(60, 255, 100, 0.6);
    animation-delay: 4s;
  }

  .explosion-4 {
    top: 50%;
    left: 45%;
    background: radial-gradient(circle, rgba(255, 180, 140, 1), rgba(255, 160, 100, 0.8), transparent);
    box-shadow: 
      0 0 25px rgba(255, 160, 120, 1),
      0 0 50px rgba(255, 140, 100, 0.8),
      0 0 75px rgba(255, 120, 80, 0.6);
    animation-delay: 4.5s;
  }

  /* Floating magic particles with enhanced firefly effect */
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
    width: 4px;
    height: 4px;
    border-radius: 50%;
    animation: magicFloat 12s linear infinite;
  }

  .magic-particle::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 400%;
    height: 400%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.3;
    z-index: -1;
    filter: blur(3px);
    background: inherit;
  }

  .magic-particle::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 800%;
    height: 800%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.15;
    z-index: -2;
    filter: blur(8px);
    background: inherit;
  }

  .magic-1 {
    top: 80%;
    left: 15%;
    background: radial-gradient(circle, rgba(255, 200, 140, 1), rgba(255, 180, 100, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 180, 120, 1),
      0 0 40px rgba(255, 160, 100, 0.8),
      0 0 60px rgba(255, 140, 80, 0.6);
    animation-delay: 5s;
  }

  .magic-2 {
    top: 90%;
    right: 10%;
    background: radial-gradient(circle, rgba(160, 140, 255, 1), rgba(140, 120, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(140, 120, 255, 1),
      0 0 40px rgba(120, 100, 255, 0.8),
      0 0 60px rgba(100, 80, 255, 0.6);
    animation-delay: 5.5s;
  }

  .magic-3 {
    top: 85%;
    left: 50%;
    background: radial-gradient(circle, rgba(140, 255, 180, 1), rgba(120, 255, 160, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(120, 255, 160, 1),
      0 0 40px rgba(100, 255, 140, 0.8),
      0 0 60px rgba(80, 255, 120, 0.6);
    animation-delay: 6s;
  }

  .magic-4 {
    top: 75%;
    left: 30%;
    background: radial-gradient(circle, rgba(255, 160, 180, 1), rgba(255, 140, 160, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 140, 160, 1),
      0 0 40px rgba(255, 120, 140, 0.8),
      0 0 60px rgba(255, 100, 120, 0.6);
    animation-delay: 6.5s;
  }

  .magic-5 {
    top: 95%;
    right: 40%;
    background: radial-gradient(circle, rgba(180, 255, 200, 1), rgba(160, 255, 180, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(160, 255, 180, 1),
      0 0 40px rgba(140, 255, 160, 0.8),
      0 0 60px rgba(120, 255, 140, 0.6);
    animation-delay: 7s;
  }

  .magic-6 {
    top: 70%;
    right: 15%;
    background: radial-gradient(circle, rgba(255, 180, 160, 1), rgba(255, 160, 140, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 160, 140, 1),
      0 0 40px rgba(255, 140, 120, 0.8),
      0 0 60px rgba(255, 120, 100, 0.6);
    animation-delay: 7.5s;
  }

  .magic-7 {
    top: 88%;
    left: 70%;
    background: radial-gradient(circle, rgba(200, 160, 255, 1), rgba(180, 140, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(180, 140, 255, 1),
      0 0 40px rgba(160, 120, 255, 0.8),
      0 0 60px rgba(140, 100, 255, 0.6);
    animation-delay: 8s;
  }

  .magic-8 {
    top: 92%;
    left: 25%;
    background: radial-gradient(circle, rgba(255, 200, 180, 1), rgba(255, 180, 160, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 180, 160, 1),
      0 0 40px rgba(255, 160, 140, 0.8),
      0 0 60px rgba(255, 140, 120, 0.6);
    animation-delay: 8.5s;
  }

  .magic-9 {
    top: 78%;
    right: 60%;
    background: radial-gradient(circle, rgba(160, 200, 255, 1), rgba(140, 180, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(140, 180, 255, 1),
      0 0 40px rgba(120, 160, 255, 0.8),
      0 0 60px rgba(100, 140, 255, 0.6);
    animation-delay: 9s;
  }

  .magic-10 {
    top: 83%;
    left: 55%;
    background: radial-gradient(circle, rgba(200, 255, 160, 1), rgba(180, 255, 140, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(180, 255, 140, 1),
      0 0 40px rgba(160, 255, 120, 0.8),
      0 0 60px rgba(140, 255, 100, 0.6);
    animation-delay: 9.5s;
  }

  /* Enhanced swirling particles with firefly trails */
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
    width: 3px;
    height: 3px;
    border-radius: 50%;
    animation: swirlMotion 18s linear infinite;
  }

  .swirl-particle::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 350%;
    height: 350%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.25;
    z-index: -1;
    filter: blur(2px);
    background: inherit;
  }

  .swirl-particle::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 700%;
    height: 700%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.1;
    z-index: -2;
    filter: blur(6px);
    background: inherit;
  }

  .swirl-1 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(255, 220, 180, 1), rgba(255, 200, 160, 0.8), transparent);
    box-shadow: 0 0 15px rgba(255, 200, 160, 1), 0 0 30px rgba(255, 180, 140, 0.8);
    animation-delay: 0s; 
  }
  .swirl-2 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(200, 180, 255, 1), rgba(180, 160, 255, 0.8), transparent);
    box-shadow: 0 0 15px rgba(180, 160, 255, 1), 0 0 30px rgba(160, 140, 255, 0.8);
    animation-delay: 1.5s; 
  }
  .swirl-3 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(180, 255, 200, 1), rgba(160, 255, 180, 0.8), transparent);
    box-shadow: 0 0 15px rgba(160, 255, 180, 1), 0 0 30px rgba(140, 255, 160, 0.8);
    animation-delay: 3s; 
  }
  .swirl-4 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(255, 180, 200, 1), rgba(255, 160, 180, 0.8), transparent);
    box-shadow: 0 0 15px rgba(255, 160, 180, 1), 0 0 30px rgba(255, 140, 160, 0.8);
    animation-delay: 4.5s; 
  }
  .swirl-5 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(180, 220, 255, 1), rgba(160, 200, 255, 0.8), transparent);
    box-shadow: 0 0 15px rgba(160, 200, 255, 1), 0 0 30px rgba(140, 180, 255, 0.8);
    animation-delay: 6s; 
  }
  .swirl-6 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(220, 255, 180, 1), rgba(200, 255, 160, 0.8), transparent);
    box-shadow: 0 0 15px rgba(200, 255, 160, 1), 0 0 30px rgba(180, 255, 140, 0.8);
    animation-delay: 7.5s; 
  }
  .swirl-7 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(255, 200, 220, 1), rgba(255, 180, 200, 0.8), transparent);
    box-shadow: 0 0 15px rgba(255, 180, 200, 1), 0 0 30px rgba(255, 160, 180, 0.8);
    animation-delay: 9s; 
  }
  .swirl-8 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(200, 220, 255, 1), rgba(180, 200, 255, 0.8), transparent);
    box-shadow: 0 0 15px rgba(180, 200, 255, 1), 0 0 30px rgba(160, 180, 255, 0.8);
    animation-delay: 10.5s; 
  }
  .swirl-9 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(220, 200, 255, 1), rgba(200, 180, 255, 0.8), transparent);
    box-shadow: 0 0 15px rgba(200, 180, 255, 1), 0 0 30px rgba(180, 160, 255, 0.8);
    animation-delay: 12s; 
  }
  .swirl-10 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(255, 220, 200, 1), rgba(255, 200, 180, 0.8), transparent);
    box-shadow: 0 0 15px rgba(255, 200, 180, 1), 0 0 30px rgba(255, 180, 160, 0.8);
    animation-delay: 13.5s; 
  }
  .swirl-11 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(200, 255, 220, 1), rgba(180, 255, 200, 0.8), transparent);
    box-shadow: 0 0 15px rgba(180, 255, 200, 1), 0 0 30px rgba(160, 255, 180, 0.8);
    animation-delay: 15s; 
  }
  .swirl-12 { 
    top: 50%; 
    left: 50%; 
    background: radial-gradient(circle, rgba(220, 255, 200, 1), rgba(200, 255, 180, 0.8), transparent);
    box-shadow: 0 0 15px rgba(200, 255, 180, 1), 0 0 30px rgba(180, 255, 160, 0.8);
    animation-delay: 16.5s; 
  }

  @keyframes fireworkExplode {
    0% {
      transform: scale(0) rotate(0deg);
      opacity: 0;
      filter: brightness(0.5) blur(0px);
    }
    10% {
      transform: scale(0.3) rotate(36deg);
      opacity: 0.6;
      filter: brightness(1.2) blur(0.5px);
    }
    20% {
      transform: scale(1.5) rotate(72deg);
      opacity: 1;
      filter: brightness(2) blur(1px);
      box-shadow: 
        0 0 40px currentColor,
        0 0 80px currentColor,
        0 0 120px currentColor;
    }
    40% {
      transform: scale(2.5) rotate(144deg);
      opacity: 0.9;
      filter: brightness(1.8) blur(0.8px);
    }
    60% {
      transform: scale(1.8) rotate(216deg);
      opacity: 0.7;
      filter: brightness(1.4) blur(0.6px);
    }
    80% {
      transform: scale(1.2) rotate(288deg);
      opacity: 0.4;
      filter: brightness(1) blur(0.3px);
    }
    100% {
      transform: scale(0.5) rotate(360deg);
      opacity: 0;
      filter: brightness(0.5) blur(0px);
    }
  }

  @keyframes particleExplode {
    0% {
      transform: scale(0) translateX(0) translateY(0) rotate(0deg);
      opacity: 0;
      filter: brightness(0.8);
    }
    15% {
      transform: scale(1.2) translateX(30px) translateY(-25px) rotate(45deg);
      opacity: 1;
      filter: brightness(1.8) blur(0.5px);
    }
    35% {
      transform: scale(2) translateX(80px) translateY(-60px) rotate(135deg);
      opacity: 0.9;
      filter: brightness(2.2) blur(1px);
    }
    55% {
      transform: scale(1.5) translateX(120px) translateY(-40px) rotate(225deg);
      opacity: 0.6;
      filter: brightness(1.5) blur(0.8px);
    }
    75% {
      transform: scale(1) translateX(150px) translateY(-20px) rotate(315deg);
      opacity: 0.3;
      filter: brightness(1) blur(0.5px);
    }
    100% {
      transform: scale(0.3) translateX(180px) translateY(0px) rotate(405deg);
      opacity: 0;
      filter: brightness(0.5) blur(0px);
    }
  }

  @keyframes magicFloat {
    0% {
      transform: translateY(100vh) translateX(0) rotate(0deg) scale(0.8);
      opacity: 0;
      filter: brightness(0.8) blur(0px);
    }
    5% {
      opacity: 0.6;
      filter: brightness(1.2) blur(0.2px);
    }
    15% {
      opacity: 1;
      filter: brightness(1.8) blur(0.5px);
    }
    25% {
      transform: translateY(75vh) translateX(20px) rotate(90deg) scale(1.4);
      filter: brightness(2.2) blur(0.8px);
    }
    50% {
      transform: translateY(40vh) translateX(-15px) rotate(180deg) scale(0.6);
      filter: brightness(1) blur(0.3px);
    }
    75% {
      transform: translateY(20vh) translateX(35px) rotate(270deg) scale(1.2);
      filter: brightness(1.6) blur(0.6px);
    }
    95% {
      opacity: 0.4;
      filter: brightness(0.8) blur(0.2px);
    }
    100% {
      transform: translateY(-10vh) translateX(50px) rotate(360deg) scale(0.8);
      opacity: 0;
      filter: brightness(0.5) blur(0px);
    }
  }

  @keyframes swirlMotion {
    0% {
      transform: rotate(0deg) translateX(150px) translateY(0) scale(0.8);
      opacity: 0.6;
      filter: brightness(1) blur(0px);
    }
    25% {
      transform: rotate(90deg) translateX(150px) translateY(0) scale(1.3);
      opacity: 1;
      filter: brightness(1.8) blur(0.5px);
    }
    50% {
      transform: rotate(180deg) translateX(150px) translateY(0) scale(0.7);
      opacity: 0.8;
      filter: brightness(1.2) blur(0.3px);
    }
    75% {
      transform: rotate(270deg) translateX(150px) translateY(0) scale(1.1);
      opacity: 1;
      filter: brightness(1.6) blur(0.4px);
    }
    100% {
      transform: rotate(360deg) translateX(150px) translateY(0) scale(0.8);
      opacity: 0.6;
      filter: brightness(1) blur(0px);
    }
  }
</style> 