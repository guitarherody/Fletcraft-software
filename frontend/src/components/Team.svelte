<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { fetchTeamMembers, type TeamMember } from '../lib/api';

  gsap.registerPlugin(ScrollTrigger);

  let teamMembers: TeamMember[] = [];
  let loading = true;
  let error = '';

  onMount(async () => {
    try {
      teamMembers = await fetchTeamMembers();
      loading = false;
    } catch (err) {
      console.error('Failed to load team members:', err);
      error = 'Failed to load team members. Please try again later.';
      loading = false;
    }

    // Animate team cards only after they're rendered
    setTimeout(() => {
      const teamCards = document.querySelectorAll('.team-card');
      const teamGrid = document.querySelector('.team-grid');
      
      if (teamCards.length > 0 && teamGrid) {
        gsap.from(teamCards, {
          scrollTrigger: {
            trigger: teamGrid,
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
</script>

<section id="team" class="section relative overflow-hidden bg-background py-16 sm:py-20 lg:py-24">
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_70%_30%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>
  
  <div class="container relative px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12 sm:mb-16">
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-bold mb-4 sm:mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Our Team
      </h2>
      <p class="text-text-secondary max-w-2xl mx-auto text-base sm:text-lg">
        Meet the talented professionals who bring your ideas to life with passion, expertise, and innovation.
      </p>
    </div>
    
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
      <div class="team-grid grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        {#each teamMembers as member}
          <div class="team-card group">
            <div class="relative p-6 rounded-2xl bg-background border border-primary/10 hover:border-primary/20 transition-all duration-300 text-center">
              <div class="absolute inset-0 bg-gradient-to-br from-primary/5 to-secondary/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity"></div>
              
              <div class="relative">
                <div class="w-20 h-20 sm:w-24 sm:h-24 mx-auto mb-4 rounded-full overflow-hidden border-4 border-primary/20 group-hover:border-primary/40 transition-colors">
                  <img 
                    src={member.image} 
                    alt={member.name}
                    class="w-full h-full object-cover"
                    loading="lazy"
                  />
                </div>
                
                <h3 class="text-lg sm:text-xl font-bold mb-2 text-text-primary group-hover:text-primary transition-colors">
                  {member.name}
                </h3>
                <p class="text-primary font-medium mb-3 text-sm sm:text-base">
                  {member.position}
                </p>
                
                <p class="text-text-secondary text-sm leading-relaxed">
                  {member.bio}
                </p>
              </div>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</section>

<style>
  .team-card {
    @apply transform transition-transform duration-300 hover:-translate-y-2;
  }
</style> 