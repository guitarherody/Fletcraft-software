<script lang="ts">
  import { onMount } from 'svelte';
  import { currentSection } from '../lib/stores';
  import { fetchProjects, type Project } from '../lib/api';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';

  gsap.registerPlugin(ScrollTrigger);

  let selectedProject = null;
  let portfolioContainer: HTMLDivElement;
  let projects: Project[] = [];
  let loading = true;

  const projectCategories = [
    { id: 'all', name: 'All Projects', icon: '🚀' },
    { id: 'web', name: 'Web Apps', icon: '🌐' },
    { id: 'mobile', name: 'Mobile', icon: '📱' },
    { id: 'ai', name: 'AI/ML', icon: '🤖' },
    { id: 'enterprise', name: 'Enterprise', icon: '🏢' }
  ];

  let activeCategory = 'all';
  let filteredProjects: Project[] = [];

  function filterProjects(category: string) {
    activeCategory = category;
    if (category === 'all') {
      filteredProjects = projects;
    } else {
      // Simple filtering based on project title and description keywords
      filteredProjects = projects.filter(project => {
        const searchText = (project.title + ' ' + project.description).toLowerCase();
        switch(category) {
          case 'web': return searchText.includes('web') || searchText.includes('platform') || searchText.includes('dashboard');
          case 'mobile': return searchText.includes('mobile') || searchText.includes('app');
          case 'ai': return searchText.includes('ai') || searchText.includes('machine learning') || searchText.includes('intelligent');
          case 'enterprise': return searchText.includes('enterprise') || searchText.includes('crm') || searchText.includes('management');
          default: return true;
        }
      });
    }

    // Animate filtered results
    gsap.from('.project-card', {
      scale: 0.8,
      opacity: 0,
      duration: 0.5,
      stagger: 0.1,
      ease: 'power2.out'
    });
  }

  function openProjectModal(project: any) {
    selectedProject = project;
    
    // Animate modal entrance
    gsap.from('.modal-content', {
      scale: 0.9,
      opacity: 0,
      duration: 0.3,
      ease: 'power2.out'
    });
  }

  function closeProjectModal() {
    gsap.to('.modal-content', {
      scale: 0.9,
      opacity: 0,
      duration: 0.2,
      ease: 'power2.in',
      onComplete: () => {
        selectedProject = null;
      }
    });
  }

  function getStatusColor(status: string) {
    switch(status) {
      case 'completed': return 'text-green-400';
      case 'in-progress': return 'text-yellow-400';
      case 'planning': return 'text-blue-400';
      default: return 'text-gray-400';
    }
  }

  function getStatusIcon(status: string) {
    switch(status) {
      case 'completed': return '✅';
      case 'in-progress': return '🔄';
      case 'planning': return '📋';
      default: return '❓';
    }
  }

  onMount(async () => {
    // Fetch projects from API
    projects = await fetchProjects();
    filteredProjects = projects;
    loading = false;

    // Set current section for navigation
    currentSection.set('portfolio');

    // Animate section entrance
    gsap.from('.portfolio-header', {
      y: 50,
      opacity: 0,
      duration: 1,
      scrollTrigger: {
        trigger: portfolioContainer,
        start: 'top center+=100',
        toggleActions: 'play none none reverse'
      }
    });

    gsap.from('.category-filter', {
      y: 30,
      opacity: 0,
      duration: 0.8,
      stagger: 0.1,
      scrollTrigger: {
        trigger: '.category-filters',
        start: 'top center+=100',
        toggleActions: 'play none none reverse'
      }
    });

    gsap.from('.project-card', {
      y: 50,
      opacity: 0,
      duration: 0.8,
      stagger: 0.2,
      scrollTrigger: {
        trigger: '.projects-grid',
        start: 'top center+=100',
        toggleActions: 'play none none reverse'
      }
    });
  });
</script>

<section id="portfolio" bind:this={portfolioContainer} class="section relative overflow-hidden bg-background">
  <!-- Background Elements -->
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_20%_30%,rgba(99,102,241,0.05)_0%,transparent_100%)]"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_70%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>

  <div class="container relative">
    <!-- Section Header -->
    <div class="text-center mb-16 portfolio-header">
      <h2 class="text-4xl md:text-5xl font-display font-bold mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Our Portfolio
      </h2>
      <p class="text-text-secondary max-w-2xl mx-auto">
        Discover how we've helped businesses transform their ideas into successful digital solutions.
      </p>
    </div>

    <!-- Category Filters -->
    <div class="category-filters flex flex-wrap justify-center gap-4 mb-12">
      {#each projectCategories as category}
        <button
          on:click={() => filterProjects(category.id)}
          class="category-filter px-6 py-3 rounded-full transition-all duration-300 {activeCategory === category.id 
            ? 'bg-gradient-to-r from-primary to-secondary text-white' 
            : 'bg-primary/10 text-text-secondary hover:bg-primary/20 hover:text-text-primary'}"
        >
          <span class="mr-2">{category.icon}</span>
          {category.name}
        </button>
      {/each}
    </div>

    <!-- Projects Grid -->
    <div class="projects-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {#each filteredProjects as project}
        <div class="project-card group cursor-pointer" on:click={() => openProjectModal(project)}>
          <div class="relative bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl overflow-hidden hover:border-primary/20 transition-all duration-300 hover:-translate-y-2">
            <!-- Project Image -->
            <div class="aspect-video bg-gradient-to-br from-primary/20 to-secondary/20 relative overflow-hidden">
              <div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/10 group-hover:from-primary/20 group-hover:to-secondary/20 transition-all duration-300"></div>
              <div class="absolute inset-0 flex items-center justify-center">
                <div class="text-6xl opacity-50 group-hover:opacity-70 transition-opacity">
                  {project.id === 1 ? '🛒' : project.id === 2 ? '🏥' : '💳'}
                </div>
              </div>
              
              <!-- Status Badge -->
              <div class="absolute top-4 left-4">
                <span class="px-3 py-1 rounded-full text-xs font-medium bg-background/80 backdrop-blur-sm {getStatusColor(project.status)}">
                  {getStatusIcon(project.status)} {project.status.replace('-', ' ').toUpperCase()}
                </span>
              </div>

              <!-- View Details Button -->
              <div class="absolute bottom-4 right-4 opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0 transition-all duration-300">
                <button class="px-4 py-2 bg-white/20 backdrop-blur-sm rounded-lg text-white text-sm hover:bg-white/30 transition-colors">
                  View Details
                </button>
              </div>
            </div>

            <!-- Project Info -->
            <div class="p-6">
              <h3 class="text-xl font-bold mb-2 text-text-primary group-hover:text-primary transition-colors">
                {project.title}
              </h3>
              <p class="text-text-secondary mb-4 line-clamp-2">
                {project.description}
              </p>

              <!-- Tech Stack -->
              <div class="flex flex-wrap gap-2 mb-4">
                {#each project.tech.slice(0, 3) as tech}
                  <span class="px-2 py-1 bg-primary/10 text-primary text-xs rounded-full">
                    {tech}
                  </span>
                {/each}
                {#if project.tech.length > 3}
                  <span class="px-2 py-1 bg-gray-500/10 text-gray-500 text-xs rounded-full">
                    +{project.tech.length - 3}
                  </span>
                {/if}
              </div>

              <!-- Quick Metrics -->
              <div class="grid grid-cols-2 gap-4 text-center">
                <div>
                  <div class="text-lg font-bold text-primary">
                    {Object.values(project.metrics)[0]}{typeof Object.values(project.metrics)[0] === 'number' && Object.values(project.metrics)[0] < 100 ? '%' : ''}
                  </div>
                  <div class="text-xs text-text-secondary">
                    {Object.keys(project.metrics)[0]}
                  </div>
                </div>
                <div>
                  <div class="text-lg font-bold text-secondary">
                    {Object.values(project.metrics)[1]}{typeof Object.values(project.metrics)[1] === 'number' && Object.values(project.metrics)[1] < 100 ? '%' : ''}
                  </div>
                  <div class="text-xs text-text-secondary">
                    {Object.keys(project.metrics)[1]}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>

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

<!-- Project Modal -->
{#if selectedProject}
  <div class="fixed inset-0 bg-background/80 backdrop-blur-sm z-50 flex items-center justify-center p-4" on:click={closeProjectModal}>
    <div class="modal-content bg-background border border-primary/20 rounded-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto" on:click|stopPropagation>
      <!-- Modal Header -->
      <div class="p-6 border-b border-primary/10">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-2xl font-bold text-text-primary mb-2">{selectedProject.title}</h3>
            <p class="text-text-secondary">{selectedProject.description}</p>
          </div>
          <button on:click={closeProjectModal} class="p-2 hover:bg-primary/10 rounded-lg transition-colors">
            <svg class="w-6 h-6 text-text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Modal Content -->
      <div class="p-6">
        <!-- Project Image -->
        <div class="aspect-video bg-gradient-to-br from-primary/20 to-secondary/20 rounded-xl mb-6 relative overflow-hidden">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-8xl opacity-50">
              {selectedProject.id === 1 ? '🛒' : selectedProject.id === 2 ? '🏥' : '💳'}
            </div>
          </div>
        </div>

        <!-- Project Details -->
        <div class="grid md:grid-cols-2 gap-8">
          <!-- Tech Stack -->
          <div>
            <h4 class="text-lg font-semibold mb-4 text-text-primary">Technology Stack</h4>
            <div class="flex flex-wrap gap-2">
              {#each selectedProject.tech as tech}
                <span class="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm">
                  {tech}
                </span>
              {/each}
            </div>
          </div>

          <!-- Project Metrics -->
          <div>
            <h4 class="text-lg font-semibold mb-4 text-text-primary">Project Metrics</h4>
            <div class="space-y-4">
              {#each Object.entries(selectedProject.metrics) as [key, value]}
                <div class="flex justify-between items-center">
                  <span class="text-text-secondary capitalize">{key.replace(/([A-Z])/g, ' $1')}</span>
                  <span class="font-semibold text-primary">
                    {value}{typeof value === 'number' && value < 100 ? '%' : ''}
                  </span>
                </div>
              {/each}
            </div>
          </div>
        </div>

        <!-- Case Study Content -->
        <div class="mt-8">
          <h4 class="text-lg font-semibold mb-4 text-text-primary">Case Study</h4>
          <div class="prose prose-invert max-w-none">
            <p class="text-text-secondary leading-relaxed">
              This project showcases our expertise in building scalable, user-centric solutions. 
              We implemented cutting-edge technologies and best practices to deliver exceptional results 
              that exceeded client expectations and drove significant business growth.
            </p>
            <p class="text-text-secondary leading-relaxed mt-4">
              The solution includes advanced features like real-time data processing, intelligent 
              recommendations, and robust security measures, all optimized for performance and scalability.
            </p>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex gap-4 mt-8">
          <button class="px-6 py-3 bg-gradient-to-r from-primary to-secondary text-white rounded-lg hover:opacity-90 transition-opacity">
            View Live Demo
          </button>
          <button class="px-6 py-3 border border-primary/20 text-primary rounded-lg hover:bg-primary/5 transition-colors">
            Read Full Case Study
          </button>
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style> 