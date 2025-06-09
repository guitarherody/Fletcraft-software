<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { fetchServices, type Service } from '../lib/api';

  gsap.registerPlugin(ScrollTrigger);

  let services: Service[] = [];
  let loading = true;

  onMount(async () => {
    // Fetch services from API
    services = await fetchServices();
    loading = false;

    // Animate service cards only after they're rendered
    setTimeout(() => {
      const serviceCards = document.querySelectorAll('.service-card');
      const servicesGrid = document.querySelector('.services-grid');
      
      if (serviceCards.length > 0 && servicesGrid) {
        gsap.from(serviceCards, {
          scrollTrigger: {
            trigger: servicesGrid,
            start: 'top center+=100',
            toggleActions: 'play none none reverse'
          },
          y: 30,
          opacity: 0,
          duration: 0.6,
          stagger: 0.1,
          ease: 'power2.out'
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
</script>

<section id="services" class="section relative overflow-hidden bg-background">
  <!-- Background Elements -->
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(99,102,241,0.05)_0%,transparent_100%)]"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_70%_80%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>
  
  <div class="container relative">
    <!-- Section Header -->
    <div class="text-center mb-16">
      <h2 class="text-4xl md:text-5xl font-display font-bold mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Our Services
      </h2>
      <p class="text-text-secondary max-w-2xl mx-auto">
        We deliver innovative solutions across a wide range of technologies, helping businesses thrive in the digital age.
      </p>
    </div>
    
    <!-- Services Grid -->
    {#if loading}
      <div class="flex justify-center items-center py-16">
        <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-primary"></div>
      </div>
    {:else}
      <div class="services-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {#each services as service}
          <div class="service-card group">
            <div class="relative p-8 rounded-2xl bg-background border border-primary/10 hover:border-primary/20 transition-all duration-300">
              <!-- Card Background -->
              <div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-secondary/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity"></div>
              
              <!-- Card Content -->
              <div class="relative">
                <div class="text-4xl mb-4">{getServiceIcon(service.icon)}</div>
                <h3 class="text-xl font-bold mb-3 text-text-primary group-hover:text-primary transition-colors">
                  {service.title}
                </h3>
                <p class="text-text-secondary">
                  {service.description}
                </p>
                
                <!-- Hover Arrow -->
                <div class="absolute bottom-0 right-0 p-4 opacity-0 transform translate-x-4 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-300">
                  <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        {/each}
      </div>
    {/if}
    
    <!-- Call to Action -->
    <div class="text-center mt-16">
      <a href="#contact" 
         class="inline-flex items-center space-x-2 px-8 py-3 bg-primary/10 text-primary rounded-lg hover:bg-primary/20 transition-colors">
        <span>Start Your Project</span>
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
        </svg>
      </a>
    </div>
  </div>
</section>

<style>
  .service-card {
    @apply transform transition-transform duration-300 hover:-translate-y-2;
  }
</style> 