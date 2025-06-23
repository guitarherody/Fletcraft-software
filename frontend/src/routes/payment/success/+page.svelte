<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import LiquidGlass from '../../../components/LiquidGlass.svelte';
  import gsap from 'gsap';

  let paymentId = '';
  let merchantPaymentId = '';

  onMount(() => {
    // Get payment details from URL parameters
    paymentId = $page.url.searchParams.get('pf_payment_id') || '';
    merchantPaymentId = $page.url.searchParams.get('m_payment_id') || '';

    // Celebration animation
    const celebration = document.querySelector('.celebration');
    if (celebration) {
      gsap.from('.success-content > *', {
        y: 50,
        opacity: 0,
        duration: 0.8,
        stagger: 0.2,
        ease: 'back.out(1.7)'
      });
    }
  });
</script>

<svelte:head>
  <title>Payment Successful - Fletcraft Software</title>
  <meta name="description" content="Your payment has been successfully processed. Thank you for choosing Fletcraft Software!" />
</svelte:head>

<div class="min-h-screen bg-background flex items-center justify-center p-4">
  <div class="w-full max-w-2xl">
    <LiquidGlass variant="card" intensity="strong" className="text-center">
      <div class="celebration success-content p-8 lg:p-12">
        <!-- Success Icon -->
        <div class="mb-8">
          <LiquidGlass variant="orb" size="lg" intensity="medium" animated={true} className="w-24 h-24 mx-auto">
            <div class="text-6xl text-green-400">✅</div>
          </LiquidGlass>
        </div>

        <!-- Success Message -->
        <h1 class="text-3xl lg:text-4xl font-bold text-text-primary mb-4">
          Payment Successful!
        </h1>
        
        <p class="text-lg text-text-secondary mb-8 leading-relaxed">
          Thank you for your purchase! Your payment has been successfully processed and we'll begin working on your project immediately.
        </p>

        <!-- Payment Details -->
        {#if paymentId || merchantPaymentId}
          <LiquidGlass variant="card" intensity="light" className="mb-8">
            <div class="p-6 text-left">
              <h3 class="text-lg font-semibold text-text-primary mb-4">Payment Details</h3>
              {#if paymentId}
                <div class="mb-2">
                  <span class="text-sm text-text-secondary">PayFast Payment ID:</span>
                  <div class="font-mono text-primary">{paymentId}</div>
                </div>
              {/if}
              {#if merchantPaymentId}
                <div class="mb-2">
                  <span class="text-sm text-text-secondary">Order Reference:</span>
                  <div class="font-mono text-primary">{merchantPaymentId}</div>
                </div>
              {/if}
            </div>
          </LiquidGlass>
        {/if}

        <!-- Next Steps -->
        <LiquidGlass variant="card" intensity="light" className="mb-8">
          <div class="p-6 text-left">
            <h3 class="text-lg font-semibold text-text-primary mb-4">What Happens Next?</h3>
            <div class="space-y-3 text-text-secondary">
              <div class="flex items-start space-x-3">
                <div class="w-6 h-6 rounded-full bg-green-400/20 flex items-center justify-center mt-0.5">
                  <span class="text-green-400 text-sm">1</span>
                </div>
                <div>
                  <div class="font-medium text-text-primary">Confirmation Email</div>
                  <div class="text-sm">You'll receive a confirmation email with your order details</div>
                </div>
              </div>
              <div class="flex items-start space-x-3">
                <div class="w-6 h-6 rounded-full bg-primary/20 flex items-center justify-center mt-0.5">
                  <span class="text-primary text-sm">2</span>
                </div>
                <div>
                  <div class="font-medium text-text-primary">Project Kickoff</div>
                  <div class="text-sm">Our team will contact you within 24 hours to discuss your project</div>
                </div>
              </div>
              <div class="flex items-start space-x-3">
                <div class="w-6 h-6 rounded-full bg-secondary/20 flex items-center justify-center mt-0.5">
                  <span class="text-secondary text-sm">3</span>
                </div>
                <div>
                  <div class="font-medium text-text-primary">Development Begins</div>
                  <div class="text-sm">We'll start working on your project with regular updates</div>
                </div>
              </div>
            </div>
          </div>
        </LiquidGlass>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <LiquidGlass variant="button" intensity="strong" shimmer={true}>
            <a href="/" class="inline-flex items-center space-x-2 px-8 py-4 text-white font-semibold">
              <span>Return Home</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
              </svg>
            </a>
          </LiquidGlass>

          <LiquidGlass variant="button" intensity="medium">
            <a href="#contact" class="inline-flex items-center space-x-2 px-8 py-4 text-primary font-semibold">
              <span>Contact Support</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
              </svg>
            </a>
          </LiquidGlass>
        </div>

        <!-- Trust Badge -->
        <div class="mt-8 pt-6 border-t border-primary/10">
          <div class="flex items-center justify-center space-x-2 text-text-secondary">
            <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            <span class="text-sm">Secured by PayFast - Payment processed successfully</span>
          </div>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<style>
  .celebration {
    position: relative;
  }

  .celebration::before {
    content: '';
    position: absolute;
    top: -20px;
    left: -20px;
    right: -20px;
    bottom: -20px;
    background: radial-gradient(circle at center, rgba(34, 197, 94, 0.1) 0%, transparent 70%);
    border-radius: 20px;
    animation: pulse 3s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 0.5; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
  }
</style> 