<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { fetchServices, type Service } from '../lib/api';
  import Checkout from './Checkout.svelte';
  import LiquidGlass from './LiquidGlass.svelte';

  gsap.registerPlugin(ScrollTrigger);

  let services: Service[] = [];
  let loading = true;
  let error = '';
  let showCheckout = false;
  let selectedService: Service | null = null;

  onMount(async () => {
    try {
      // Fetch services from API
      services = await fetchServices();
      loading = false;
    } catch (err) {
      console.error('Failed to load services:', err);
      error = 'Failed to load services. Please try again later.';
      loading = false;
    }

    // Enhanced animate service cards only after they're rendered
    setTimeout(() => {
      const serviceCards = document.querySelectorAll('.service-card');
      const servicesGrid = document.querySelector('.services-grid');
      
      if (serviceCards.length > 0 && servicesGrid) {
        // Staggered entrance animation
        gsap.fromTo(serviceCards, 
          {
            y: 60,
            opacity: 0,
            scale: 0.8,
            rotationY: 45
          },
          {
            scrollTrigger: {
              trigger: servicesGrid,
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

        // Add continuous floating animation
        gsap.to(serviceCards, {
          y: '+=10',
          duration: 3,
          ease: 'sine.inOut',
          yoyo: true,
          repeat: -1,
          stagger: 0.2
        });

        // Icon animation on scroll
        gsap.from('.service-icon', {
          scrollTrigger: {
            trigger: servicesGrid,
            start: 'top center+=150',
            toggleActions: 'play none none reverse'
          },
          scale: 0,
          rotation: 180,
          duration: 0.6,
          stagger: 0.1,
          ease: 'elastic.out(1, 0.5)'
        });
      }
    }, 100);
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

<section id="services" class="section relative overflow-hidden bg-background py-16 sm:py-20 lg:py-24">
  <!-- Background Elements -->
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(99,102,241,0.05)_0%,transparent_100%)]"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_70%_80%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>
  
  <div class="container relative px-4 sm:px-6 lg:px-8">
    <!-- Section Header -->
    <div class="text-center mb-12 sm:mb-16">
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-bold mb-4 sm:mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Our Services
      </h2>
      <p class="text-text-secondary max-w-2xl mx-auto text-base sm:text-lg">
        We deliver innovative solutions across a wide range of technologies, helping businesses thrive in the digital age.
      </p>
    </div>
    
    <!-- Services Grid -->
    {#if loading}
      <div class="flex justify-center items-center py-16">
        <div class="animate-spin rounded-full h-12 w-12 sm:h-16 sm:w-16 border-t-2 border-b-2 border-primary"></div>
      </div>
    {:else if error}
      <div class="flex justify-center items-center py-16">
        <div class="text-red-500 text-center px-4">
          <p class="text-lg font-semibold mb-2">⚠️ Error</p>
          <p class="text-sm sm:text-base">{error}</p>
        </div>
      </div>
    {:else}
      <div class="services-grid grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        {#each services as service}
          <div class="service-card group">
            <LiquidGlass variant="card" intensity="medium" animated={true} shimmer={true} className="h-full group-hover:scale-105 transition-transform duration-500">
              <div class="relative p-6 sm:p-8 h-full flex flex-col">
                <!-- Floating Icon with Glass Effect -->
                <div class="service-icon relative mb-4 sm:mb-6">
                  <LiquidGlass variant="orb" size="sm" intensity="light" animated={true} className="w-16 h-16 mx-auto">
                    <div class="text-2xl transform transition-transform duration-300 group-hover:scale-110 group-hover:rotate-12">
                      {getServiceIcon(service.icon)}
                    </div>
                  </LiquidGlass>
                </div>

                <!-- Service Content -->
                <div class="flex-1 flex flex-col">
                  <h3 class="text-lg sm:text-xl font-bold mb-3 sm:mb-4 text-text-primary group-hover:text-primary transition-colors duration-300">
                    {service.title}
                  </h3>
                  <p class="text-text-secondary leading-relaxed text-sm sm:text-base mb-4 flex-1">
                    {service.description}
                  </p>
                  
                  <!-- Price Display with Glass Effect -->
                  {#if service.price && service.price > 0}
                    <div class="mb-4">
                      <LiquidGlass variant="button" intensity="light" className="inline-block">
                        <div class="px-4 py-2 text-center">
                          <div class="text-2xl font-bold text-green-400">
                            R {service.price}
                          </div>
                          <div class="text-xs text-text-secondary">One-time payment</div>
                        </div>
                      </LiquidGlass>
                    </div>
                  {/if}
                  
                  <!-- Enhanced Purchase Button -->
                  {#if service.price && service.price > 0}
                    <LiquidGlass variant="button" intensity="strong" shimmer={true} className="w-full mt-auto">
                      <button
                        on:click={() => openCheckout(service)}
                        class="w-full px-4 py-3 text-white font-semibold text-center transition-all duration-300 flex items-center justify-center space-x-2">
                        <span>Purchase Now</span>
                        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                        </svg>
                      </button>
                    </LiquidGlass>
                  {/if}
                </div>

                <!-- Floating Glass Particles -->
                <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <LiquidGlass variant="orb" size="sm" intensity="light" className="w-3 h-3">
                  </LiquidGlass>
                </div>
                <div class="absolute bottom-4 left-4 opacity-0 group-hover:opacity-100 transition-opacity duration-500">
                  <LiquidGlass variant="orb" size="sm" intensity="light" className="w-2 h-2">
                  </LiquidGlass>
                </div>
              </div>
            </LiquidGlass>
          </div>
        {/each}
      </div>
    {/if}
    
    <!-- Call to Action -->
    <div class="text-center mt-12 sm:mt-16">
      <a href="#contact" 
         class="inline-flex items-center space-x-2 px-6 sm:px-8 py-3 bg-primary/10 text-primary rounded-lg hover:bg-primary/20 transition-colors text-sm sm:text-base">
        <span>Start Your Project</span>
        <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </a>
    </div>
  </div>
</section>

{#if showCheckout && selectedService}
  <Checkout service={selectedService} onClose={closeCheckout} />
{/if}

<style>
  /* Enhanced service card with liquid glass effects */
  .service-card {
    perspective: 1000px;
    transform-style: preserve-3d;
  }

  .service-icon {
    filter: drop-shadow(0 4px 8px rgba(99,102,241,0.3));
  }

  /* Subtle floating animation for service cards */
  .service-card:hover {
    transform: translateY(-2px) rotateX(2deg);
  }

  /* Animated background gradient */
  .services-grid::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(99,102,241,0.05), transparent);
    animation: rotate-bg 30s linear infinite;
    opacity: 0.3;
    pointer-events: none;
    border-radius: 50%;
  }

  @keyframes rotate-bg {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  /* Performance optimizations */
  .service-card {
    will-change: transform;
    backface-visibility: hidden;
  }
</style> 