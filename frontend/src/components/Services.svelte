<script lang="ts">
  import { onMount } from 'svelte';
  import { fetchServices, type Service } from '../lib/api';
  import Checkout from './Checkout.svelte';

  let services: Service[] = [];
  let loading = true;
  let error = '';
  let showCheckout = false;
  let selectedService: Service | null = null;

  onMount(async () => {
    try {
      services = await fetchServices();
      loading = false;
    } catch (err) {
      console.error('Failed to load services:', err);
      error = 'Failed to load services. Please try again later.';
      loading = false;
    }
  });

  // Icon mapping for services
  function getServiceIcon(iconClass: string): string {
    const iconMap: { [key: string]: string } = {
      'fas fa-code': '💻',
      'fas fa-globe': '🌐',
      'fas fa-mobile-alt': '📱',
      'fas fa-robot': '🤖',
      'fas fa-cloud': '☁️',
      'fas fa-shield-alt': '🔒'
    };
    return iconMap[iconClass] || '⚡';
  }

  function openCheckout(service: Service) {
    selectedService = service;
    showCheckout = true;
  }

  function closeCheckout() {
    showCheckout = false;
    selectedService = null;
  }
</script>

<section id="services" class="relative py-20 px-4">
  <!-- Simple background -->
  <div class="absolute inset-0 bg-gradient-to-b from-gray-900 to-black"></div>
  
  <div class="relative max-w-6xl mx-auto">
    <!-- Section Header -->
    <div class="text-center mb-16">
      <h2 class="text-4xl md:text-5xl font-bold mb-6 text-white">
        Our <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">Services</span>
      </h2>
      <p class="text-gray-300 max-w-2xl mx-auto text-lg">
        We deliver innovative solutions across a wide range of technologies, helping businesses thrive in the digital age.
      </p>
    </div>
    
    <!-- Services Grid -->
    {#if loading}
      <div class="flex justify-center items-center py-16">
        <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-purple-500"></div>
      </div>
    {:else if error}
      <div class="flex justify-center items-center py-16">
        <div class="text-red-400 text-center">
          <p class="text-lg font-semibold mb-2">⚠️ Error</p>
          <p>{error}</p>
        </div>
      </div>
    {:else}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {#each services as service}
          <div class="service-card group bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-white/20 transition-all duration-300">
            
            <!-- Icon -->
            <div class="text-center mb-6">
              <div class="w-16 h-16 mx-auto bg-purple-500/20 rounded-2xl flex items-center justify-center text-3xl border border-purple-400/30">
                {getServiceIcon(service.icon)}
              </div>
            </div>

            <!-- Service Content -->
            <div class="text-center">
              <h3 class="text-xl font-bold mb-3 text-white">
                {service.title}
              </h3>
              <p class="text-gray-300 leading-relaxed text-sm mb-6">
                {service.description}
              </p>
              
              <!-- Price Display -->
              <div class="mb-6">
                <div class="bg-green-500/10 border border-green-400/30 rounded-lg px-4 py-3">
                  <div class="text-2xl font-bold text-green-400">
                    R {service.price || '0.00'}
                  </div>
                  <div class="text-xs text-gray-400">One-time payment</div>
                </div>
              </div>
              
              <!-- Purchase Button -->
              <button
                on:click={() => openCheckout(service)}
                class="w-full px-4 py-3 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-semibold rounded-lg transition-all duration-200 hover:scale-105">
                Purchase Now
              </button>
            </div>
          </div>
        {/each}
      </div>
    {/if}
    
    <!-- Call to Action -->
    <div class="text-center mt-16 space-y-4">
      <a href="/pricing" 
         class="inline-flex items-center space-x-3 px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-bold text-lg rounded-lg transition-all duration-200 hover:scale-105">
        <span>View All Pricing & Purchase</span>
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </a>
      
      <div class="mt-4">
        <a href="#contact" 
           class="inline-flex items-center space-x-2 px-8 py-3 bg-white/10 text-white rounded-lg hover:bg-white/20 transition-colors border border-white/20">
          <span>Or Start Custom Project</span>
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
          </svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- Checkout Modal -->
{#if showCheckout && selectedService}
  <div class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 p-4">
    <div class="bg-gray-900 rounded-2xl p-6 max-w-md w-full border border-white/10">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-xl font-bold text-white">Purchase Service</h3>
        <button on:click={closeCheckout} class="text-gray-400 hover:text-white">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
      <Checkout service={selectedService} on:close={closeCheckout} />
    </div>
  </div>
{/if}

<style>
  .service-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(139, 92, 246, 0.15);
  }
</style> 