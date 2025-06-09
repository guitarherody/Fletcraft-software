<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { fetchServices, type Service } from '../lib/api';

  gsap.registerPlugin(ScrollTrigger);

  let services: Service[] = [];
  let loading = true;
  let error = '';

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
    {:else if error}
      <div class="flex justify-center items-center py-16">
        <div class="text-red-500 text-center">
          <p class="text-lg font-semibold mb-2">⚠️ Error</p>
          <p>{error}</p>
        </div>
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
                <div class="service-icon text-5xl mb-6 transform transition-transform duration-300 group-hover:scale-110 group-hover:rotate-12">
                  {getServiceIcon(service.icon)}
                </div>
                <h3 class="text-xl font-bold mb-4 text-text-primary group-hover:text-primary transition-colors duration-300">
                  {service.title}
                </h3>
                <p class="text-text-secondary leading-relaxed">
                  {service.description}
                </p>
                
                <!-- Animated hover elements -->
                <div class="absolute -top-2 -right-2 w-8 h-8 bg-gradient-to-r from-primary to-secondary rounded-full opacity-0 group-hover:opacity-100 transform scale-0 group-hover:scale-100 transition-all duration-300"></div>
                <div class="absolute -bottom-2 -left-2 w-6 h-6 bg-gradient-to-r from-accent to-primary rounded-full opacity-0 group-hover:opacity-100 transform scale-0 group-hover:scale-100 transition-all duration-500"></div>
                
                <!-- Hover Arrow -->
                <div class="absolute bottom-4 right-4 opacity-0 transform translate-x-4 translate-y-4 group-hover:opacity-100 group-hover:translate-x-0 group-hover:translate-y-0 transition-all duration-300">
                  <div class="w-10 h-10 bg-gradient-to-r from-primary to-secondary rounded-full flex items-center justify-center">
                    <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                    </svg>
                  </div>
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
    @apply transform transition-all duration-500 hover:-translate-y-4;
    perspective: 1000px;
  }

  .service-card:hover {
    transform: translateY(-16px) rotateX(5deg) rotateY(5deg);
    box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.25);
  }

  .service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.1));
    border-radius: 1rem;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
  }

  .service-card:hover::before {
    opacity: 1;
  }

  .service-icon {
    filter: drop-shadow(0 4px 8px rgba(99,102,241,0.3));
  }

  /* Animated background patterns */
  .service-card::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(99,102,241,0.1), transparent);
    animation: rotate-bg 20s linear infinite;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
    border-radius: 50%;
  }

  .service-card:hover::after {
    opacity: 1;
  }

  @keyframes rotate-bg {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
</style> 