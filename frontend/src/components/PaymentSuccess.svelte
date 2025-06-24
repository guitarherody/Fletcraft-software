<script lang="ts">
  import { onMount } from 'svelte';
  import ParticleSystem from '../../../components/ParticleSystem.svelte';

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

<div class="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900/20 to-blue-900/20 flex items-center justify-center p-4">
  <div class="relative z-10 w-full max-w-2xl">
    <div class="glass text-center p-8 lg:p-12 rounded-2xl">
      
      <!-- Success Icon -->
      <div class="mb-8">
        <div class="w-24 h-24 mx-auto bg-green-500/20 rounded-full flex items-center justify-center border-4 border-green-400/30 animate-pulse">
          <div class="text-6xl text-green-400">✅</div>
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
        <div class="glass mb-8 p-6 text-left rounded-xl animate-fadeInUp" style="animation-delay: 400ms;">
          <h3 class="text-lg font-semibold text-white mb-4">Payment Details</h3>
          {#if paymentId}
            <div class="mb-2">
              <span class="text-sm text-gray-400">PayFast Payment ID:</span>
              <div class="font-mono text-purple-400">{paymentId}</div>
            </div>
          {/if}
          {#if merchantPaymentId}
            <div class="mb-2">
              <span class="text-sm text-gray-400">Order Reference:</span>
              <div class="font-mono text-purple-400">{merchantPaymentId}</div>
            </div>
          {/if}
        </div>
      {/if}

      <!-- Next Steps -->
      <div class="glass mb-8 p-6 text-left rounded-xl animate-fadeInUp" style="animation-delay: 600ms;">
        <h3 class="text-lg font-semibold text-white mb-4">What Happens Next?</h3>
        <div class="space-y-3 text-gray-300">
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-green-400/20 flex items-center justify-center mt-0.5">
              <span class="text-green-400 text-sm">1</span>
            </div>
            <div>
              <div class="font-medium text-white">Confirmation Email</div>
              <div class="text-sm">You'll receive a confirmation email with your order details</div>
            </div>
          </div>
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-purple-400/20 flex items-center justify-center mt-0.5">
              <span class="text-purple-400 text-sm">2</span>
            </div>
            <div>
              <div class="font-medium text-white">Project Kickoff</div>
              <div class="text-sm">Our team will contact you within 24 hours to discuss your project</div>
            </div>
          </div>
          <div class="flex items-start space-x-3">
            <div class="w-6 h-6 rounded-full bg-pink-400/20 flex items-center justify-center mt-0.5">
              <span class="text-pink-400 text-sm">3</span>
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
        <a href="/" class="inline-flex items-center space-x-2 px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-semibold rounded-lg transition-all duration-200 hover:scale-105">
          <span>Return Home</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
          </svg>
        </a>

        <a href="/#contact" class="inline-flex items-center space-x-2 px-8 py-4 bg-white/10 text-white font-semibold rounded-lg backdrop-blur-sm border border-white/20 hover:bg-white/20 transition-all duration-200">
          <span>Contact Support</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
          </svg>
        </a>
      </div>

      <!-- Trust Badge -->
      <div class="mt-8 pt-6 border-t border-white/10 animate-fadeInUp" style="animation-delay: 1000ms;">
        <div class="flex items-center justify-center space-x-2 text-gray-400">
          <svg class="w-5 h-5 text-green-400" fill="currentColor" viewBox="0 0 20 20">
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
</style> 