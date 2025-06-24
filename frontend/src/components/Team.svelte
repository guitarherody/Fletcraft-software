<script lang="ts">
  import { onMount } from 'svelte';
  import { fetchTeamMembers, type TeamMember } from '../lib/api';

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
  });
</script>

<section id="team" class="relative py-20 px-4">
  <div class="absolute inset-0 bg-gradient-to-b from-gray-900 to-black"></div>
  
  <div class="relative max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <h2 class="text-4xl md:text-5xl font-bold mb-6 text-white">
        Our <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">Team</span>
      </h2>
      <p class="text-gray-300 max-w-2xl mx-auto text-lg">
        Meet the talented professionals who bring your ideas to life with passion, expertise, and innovation.
      </p>
    </div>
    
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
        {#each teamMembers as member}
          <div class="team-card bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-6 text-center hover:bg-white/10 hover:border-white/20 transition-all duration-300">
            
            <div class="w-24 h-24 mx-auto mb-4 rounded-full overflow-hidden border-4 border-purple-400/30">
              <img 
                src={member.image} 
                alt={member.name}
                class="w-full h-full object-cover"
                loading="lazy"
              />
            </div>
            
            <h3 class="text-xl font-bold mb-2 text-white">
              {member.name}
            </h3>
            <p class="text-purple-400 font-medium mb-3">
              {member.position}
            </p>
            
            <p class="text-gray-300 text-sm leading-relaxed">
              {member.bio}
            </p>
            
          </div>
        {/each}
      </div>
    {/if}
  </div>
</section>

<style>
  .team-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(139, 92, 246, 0.15);
  }
</style> 