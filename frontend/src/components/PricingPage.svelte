<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly, scale } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { fetchServices, type Service } from '../lib/api';
  import LiquidGlass from './LiquidGlass.svelte';

  gsap.registerPlugin(ScrollTrigger);

  let services: Service[] = [];
  let loading = true;
  let error = '';
  let selectedService: Service | null = null;
  let showCheckout = false;

  // Checkout form data
  let customerName = '';
  let customerEmail = '';
  let customerPhone = '';
  let isProcessing = false;
  let errorMessage = '';

  const API_BASE = import.meta.env.VITE_API_URL 
    ? `${import.meta.env.VITE_API_URL}/api`
    : 'https://fletcraft-software.onrender.com/api';

  onMount(async () => {
    try {
      services = await fetchServices();
      loading = false;
      
      // Enhanced animations after services load
      setTimeout(() => {
        const serviceCards = document.querySelectorAll('.pricing-card');
        const hero = document.querySelector('.pricing-hero');
        
        if (hero) {
          gsap.fromTo(hero.children,
            { y: 50, opacity: 0 },
            { 
              y: 0, 
              opacity: 1, 
              duration: 1,
              stagger: 0.2,
              ease: 'back.out(1.7)'
            }
          );
        }
        
        if (serviceCards.length > 0) {
          gsap.fromTo(serviceCards,
            {
              y: 80,
              opacity: 0,
              scale: 0.8,
              rotationY: 25
            },
            {
              scrollTrigger: {
                trigger: '.pricing-grid',
                start: 'top center+=100',
                toggleActions: 'play none none reverse'
              },
              y: 0,
              opacity: 1,
              scale: 1,
              rotationY: 0,
              duration: 0.8,
              stagger: 0.15,
              ease: 'back.out(1.7)'
            }
          );

          // Continuous floating animation
          gsap.to(serviceCards, {
            y: '+=8',
            duration: 4,
            ease: 'sine.inOut',
            yoyo: true,
            repeat: -1,
            stagger: 0.3
          });
        }
      }, 100);
      
    } catch (err) {
      console.error('Failed to load services:', err);
      error = 'Failed to load services. Please try again later.';
      loading = false;
    }
  });

  function getServiceIcon(iconClass: string): string {
    const iconMap: { [key: string]: string } = {
      'fas fa-code': '💻',
      'fas fa-globe': '🌐',
      'fas fa-mobile-alt': '📱',
      'fas fa-robot': '🤖',
      'fas fa-cloud': '☁️',
      'fas fa-shield-alt': '🔒',
      'fas fa-palette': '🎨'
    };
    return iconMap[iconClass] || '⚡';
  }

  function openCheckout(service: Service) {
    selectedService = service;
    showCheckout = true;
    document.body.style.overflow = 'hidden';
  }

  function closeCheckout() {
    showCheckout = false;
    selectedService = null;
    customerName = '';
    customerEmail = '';
    customerPhone = '';
    errorMessage = '';
    document.body.style.overflow = 'auto';
  }

  async function handlePurchase() {
    if (!selectedService || !customerName || !customerEmail) return;

    try {
      isProcessing = true;
      errorMessage = '';

      // Create order
      const orderResponse = await fetch(`${API_BASE}/orders/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          service: selectedService.id,
          customer_name: customerName,
          customer_email: customerEmail,
          customer_phone: customerPhone,
          amount: selectedService.price,
          currency: 'ZAR'
        })
      });

      if (!orderResponse.ok) {
        throw new Error('Failed to create order');
      }

      const order = await orderResponse.json();

      // Create PayFast payment
      const paymentResponse = await fetch(`${API_BASE}/orders/create_payfast_payment/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          order_id: order.order_id
        })
      });

      if (!paymentResponse.ok) {
        throw new Error('Failed to create payment');
      }

      const paymentData = await paymentResponse.json();

      // Create and submit PayFast form
      const form = document.createElement('form');
      form.method = 'POST';
      form.action = paymentData.payment_url;
      form.style.display = 'none';

      Object.entries(paymentData.payment_data).forEach(([key, value]) => {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = String(value);
        form.appendChild(input);
      });

      document.body.appendChild(form);
      form.submit();

    } catch (error) {
      console.error('Payment error:', error);
      errorMessage = error.message || 'An error occurred while processing payment';
    } finally {
      isProcessing = false;
    }
  }
</script>

<div class="min-h-screen bg-background">
  <!-- Hero Section -->
  <section class="pricing-hero relative overflow-hidden bg-gradient-to-br from-primary/5 via-secondary/5 to-accent/5 py-20 lg:py-32">
    <!-- Background Effects -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_30%,rgba(99,102,241,0.1)_0%,transparent_70%)]"></div>
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_70%,rgba(139,92,246,0.1)_0%,transparent_70%)]"></div>
    
    <div class="container relative px-4 sm:px-6 lg:px-8 text-center">
      <h1 class="text-4xl sm:text-5xl md:text-7xl font-display font-bold mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Our Services & Pricing
      </h1>
      <p class="text-lg sm:text-xl text-text-secondary max-w-3xl mx-auto mb-8">
        Transparent pricing for world-class software development services. Choose the service that fits your needs and get started instantly.
      </p>
      
      <LiquidGlass variant="button" intensity="medium" shimmer={true} className="inline-block">
        <div class="px-8 py-4 text-center">
          <div class="text-sm text-text-secondary mb-1">Secure payments powered by</div>
          <div class="flex items-center justify-center space-x-2">
            <span class="text-lg font-bold text-primary">PayFast</span>
            <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
          </div>
        </div>
      </LiquidGlass>
    </div>
  </section>

  <!-- Services Grid -->
  <section class="py-16 lg:py-24">
    <div class="container px-4 sm:px-6 lg:px-8">
      {#if loading}
        <div class="flex justify-center items-center py-20">
          <LiquidGlass variant="orb" size="lg" intensity="medium" animated={true}>
            <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-primary"></div>
          </LiquidGlass>
        </div>
      {:else if error}
        <div class="flex justify-center items-center py-20">
          <LiquidGlass variant="card" intensity="light" className="max-w-md text-center">
            <div class="p-8">
              <div class="text-red-500 text-6xl mb-4">⚠️</div>
              <h3 class="text-lg font-semibold mb-2 text-text-primary">Error Loading Services</h3>
              <p class="text-text-secondary">{error}</p>
            </div>
          </LiquidGlass>
        </div>
      {:else}
        <div class="pricing-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {#each services as service (service.id)}
            <div class="pricing-card group">
              <LiquidGlass variant="card" intensity="medium" animated={true} shimmer={true} className="h-full group-hover:scale-105 transition-transform duration-500">
                <div class="relative p-8 h-full flex flex-col">
                  <!-- Service Icon -->
                  <div class="text-center mb-6">
                    <LiquidGlass variant="orb" size="md" intensity="light" animated={true} className="w-20 h-20 mx-auto">
                      <div class="text-4xl transform transition-transform duration-300 group-hover:scale-110 group-hover:rotate-12">
                        {getServiceIcon(service.icon)}
                      </div>
                    </LiquidGlass>
                  </div>

                  <!-- Service Info -->
                  <div class="text-center mb-6">
                    <h3 class="text-2xl font-bold text-text-primary mb-3 group-hover:text-primary transition-colors duration-300">
                      {service.title}
                    </h3>
                    <p class="text-text-secondary leading-relaxed">
                      {service.description}
                    </p>
                  </div>

                  <!-- Price -->
                  <div class="text-center mb-8 mt-auto">
                    <LiquidGlass variant="button" intensity="light" className="inline-block">
                      <div class="px-6 py-4 text-center">
                        <div class="text-4xl font-bold text-green-400 mb-1">
                          R {service.price}
                        </div>
                        <div class="text-sm text-text-secondary">One-time payment</div>
                      </div>
                    </LiquidGlass>
                  </div>

                  <!-- Purchase Button -->
                  <LiquidGlass variant="button" intensity="strong" shimmer={true} className="w-full">
                    <button
                      on:click={() => openCheckout(service)}
                      class="w-full px-6 py-4 text-white font-bold text-lg transition-all duration-300 flex items-center justify-center space-x-3">
                      <span>Purchase Now</span>
                      <svg class="w-5 h-5 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                      </svg>
                    </button>
                  </LiquidGlass>

                  <!-- Floating accent -->
                  <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-60 transition-opacity duration-300">
                    <LiquidGlass variant="orb" size="sm" intensity="light" className="w-3 h-3">
                    </LiquidGlass>
                  </div>
                </div>
              </LiquidGlass>
            </div>
          {/each}
        </div>
      {/if}
    </div>
  </section>
</div>

<!-- Checkout Modal -->
{#if showCheckout && selectedService}
  <div 
    class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50"
    transition:fade={{ duration: 200 }}
    on:click={closeCheckout}
  >
    <div 
      class="w-full max-w-md"
      transition:scale={{ duration: 300, easing: quintOut }}
      on:click|stopPropagation
    >
      <LiquidGlass variant="card" intensity="strong" className="w-full">
        <div class="p-8">
          <!-- Header -->
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-2xl font-bold text-text-primary">Complete Purchase</h2>
            <button 
              on:click={closeCheckout}
              class="text-text-secondary hover:text-text-primary transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>

          <!-- Service Summary -->
          <LiquidGlass variant="card" intensity="light" className="mb-6">
            <div class="p-4">
              <h3 class="font-semibold text-lg text-text-primary mb-2">{selectedService.title}</h3>
              <p class="text-text-secondary text-sm mb-3">{selectedService.description}</p>
              <div class="text-2xl font-bold text-green-400">R {selectedService.price}</div>
            </div>
          </LiquidGlass>

          <!-- Form -->
          <form on:submit|preventDefault={handlePurchase} class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-text-primary mb-2">
                Full Name *
              </label>
              <input
                type="text"
                bind:value={customerName}
                required
                class="w-full px-4 py-3 rounded-lg bg-background/50 border border-primary/20 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 text-text-primary"
                placeholder="Enter your full name"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-text-primary mb-2">
                Email Address *
              </label>
              <input
                type="email"
                bind:value={customerEmail}
                required
                class="w-full px-4 py-3 rounded-lg bg-background/50 border border-primary/20 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 text-text-primary"
                placeholder="Enter your email address"
              />
              <p class="text-xs text-text-secondary mt-1">
                💡 For testing: Don't use dylan@fletcraft.co.za or guitarherody@gmail.com (merchant accounts)
              </p>
            </div>

            <div>
              <label class="block text-sm font-medium text-text-primary mb-2">
                Phone Number (Optional)
              </label>
              <input
                type="tel"
                bind:value={customerPhone}
                class="w-full px-4 py-3 rounded-lg bg-background/50 border border-primary/20 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/20 text-text-primary"
                placeholder="Enter your phone number"
              />
            </div>

            {#if errorMessage}
              <LiquidGlass variant="card" intensity="light" className="border-red-500/30">
                <div class="p-4 text-red-400 text-sm">
                  {errorMessage}
                </div>
              </LiquidGlass>
            {/if}

            <!-- Submit Button -->
            <LiquidGlass variant="button" intensity="strong" shimmer={true} className="w-full">
              <button
                type="submit"
                disabled={isProcessing || !customerName || !customerEmail}
                class="w-full px-6 py-4 text-white font-bold text-lg transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center space-x-3">
                {#if isProcessing}
                  <div class="animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-white"></div>
                  <span>Processing...</span>
                {:else}
                  <span>Pay with PayFast</span>
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                  </svg>
                {/if}
              </button>
            </LiquidGlass>
          </form>
        </div>
      </LiquidGlass>
    </div>
  </div>
{/if}

<style>
  .pricing-card {
    perspective: 1000px;
    transform-style: preserve-3d;
  }

  .pricing-card:hover {
    transform: translateY(-4px) rotateX(2deg);
  }

  /* Input styling */
  input:focus {
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
  }

  /* Performance optimizations */
  .pricing-card {
    will-change: transform;
    backface-visibility: hidden;
  }
</style> 