<script lang="ts">
  import { onMount } from 'svelte';
  import { analyticsData, currentSection } from '../lib';
  import { Chart, registerables } from 'chart.js';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';

  Chart.register(...registerables);
  gsap.registerPlugin(ScrollTrigger);

  let analyticsContainer: HTMLDivElement;
  let performanceChart: HTMLCanvasElement;
  let projectsChart: HTMLCanvasElement;
  let satisfactionChart: HTMLCanvasElement;

  // Animated counters
  let animatedVisitors = 0;
  let animatedProjects = 0;
  let animatedSatisfaction = 0;
  let animatedTeamSize = 0;

  const metrics = [
    {
      label: 'Active Projects',
      value: 12,
      icon: '🚀',
      color: 'from-primary to-secondary',
      change: '+15%'
    },
    {
      label: 'Happy Clients',
      value: 150,
      icon: '😊',
      color: 'from-secondary to-accent',
      change: '+23%'
    },
    {
      label: 'Team Members',
      value: 25,
      icon: '👥',
      color: 'from-accent to-primary',
      change: '+8%'
    },
    {
      label: 'Lines of Code',
      value: '2.5M',
      icon: '💻',
      color: 'from-primary to-accent',
      change: '+45%'
    }
  ];

  function animateCounters() {
    // Animate visitors counter
    gsap.to({ value: 0 }, {
      value: $analyticsData.visitorsToday,
      duration: 2,
      ease: 'power2.out',
      onUpdate: function() {
        animatedVisitors = Math.floor(this.targets()[0].value);
      }
    });

    // Animate projects counter
    gsap.to({ value: 0 }, {
      value: $analyticsData.projectsCompleted,
      duration: 2,
      delay: 0.2,
      ease: 'power2.out',
      onUpdate: function() {
        animatedProjects = Math.floor(this.targets()[0].value);
      }
    });

    // Animate satisfaction counter
    gsap.to({ value: 0 }, {
      value: $analyticsData.clientSatisfaction,
      duration: 2,
      delay: 0.4,
      ease: 'power2.out',
      onUpdate: function() {
        animatedSatisfaction = this.targets()[0].value.toFixed(1);
      }
    });

    // Animate team size counter
    gsap.to({ value: 0 }, {
      value: $analyticsData.teamSize,
      duration: 2,
      delay: 0.6,
      ease: 'power2.out',
      onUpdate: function() {
        animatedTeamSize = Math.floor(this.targets()[0].value);
      }
    });
  }

  function createPerformanceChart() {
    const ctx = performanceChart.getContext('2d');
    return new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Project Delivery',
          data: [85, 92, 88, 94, 97, 95],
          borderColor: '#6366f1',
          backgroundColor: 'rgba(99, 102, 241, 0.1)',
          tension: 0.4,
          fill: true
        }, {
          label: 'Client Satisfaction',
          data: [88, 91, 89, 96, 98, 97],
          borderColor: '#8b5cf6',
          backgroundColor: 'rgba(139, 92, 246, 0.1)',
          tension: 0.4,
          fill: true
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            labels: {
              color: '#94a3b8'
            }
          }
        },
        scales: {
          x: {
            ticks: { color: '#94a3b8' },
            grid: { color: 'rgba(148, 163, 184, 0.1)' }
          },
          y: {
            ticks: { color: '#94a3b8' },
            grid: { color: 'rgba(148, 163, 184, 0.1)' }
          }
        }
      }
    });
  }

  function createProjectsChart() {
    const ctx = projectsChart.getContext('2d');
    return new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Web Apps', 'Mobile', 'AI/ML', 'Enterprise'],
        datasets: [{
          data: [35, 25, 20, 20],
          backgroundColor: [
            '#6366f1',
            '#8b5cf6',
            '#ec4899',
            '#10b981'
          ],
          borderWidth: 0
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              color: '#94a3b8',
              padding: 20
            }
          }
        }
      }
    });
  }

  function createSatisfactionChart() {
    const ctx = satisfactionChart.getContext('2d');
    return new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Q1', 'Q2', 'Q3', 'Q4'],
        datasets: [{
          label: 'Satisfaction Score',
          data: [94, 96, 97, 98],
          backgroundColor: 'rgba(99, 102, 241, 0.8)',
          borderRadius: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
          x: {
            ticks: { color: '#94a3b8' },
            grid: { display: false }
          },
          y: {
            ticks: { color: '#94a3b8' },
            grid: { color: 'rgba(148, 163, 184, 0.1)' },
            beginAtZero: false,
            min: 90
          }
        }
      }
    });
  }

  onMount(() => {
    currentSection.set('analytics');

    // Animate section entrance
    gsap.from('.analytics-header', {
      y: 50,
      opacity: 0,
      duration: 1,
      scrollTrigger: {
        trigger: analyticsContainer,
        start: 'top center+=100',
        toggleActions: 'play none none reverse'
      }
    });

    gsap.from('.metric-card', {
      y: 30,
      opacity: 0,
      duration: 0.8,
      stagger: 0.1,
      scrollTrigger: {
        trigger: '.metrics-grid',
        start: 'top center+=100',
        toggleActions: 'play none none reverse',
        onEnter: animateCounters
      }
    });

    gsap.from('.chart-container', {
      y: 40,
      opacity: 0,
      duration: 0.8,
      stagger: 0.2,
      scrollTrigger: {
        trigger: '.charts-grid',
        start: 'top center+=100',
        toggleActions: 'play none none reverse'
      }
    });

    // Initialize charts
    setTimeout(() => {
      createPerformanceChart();
      createProjectsChart();
      createSatisfactionChart();
    }, 500);
  });
</script>

<section id="analytics" bind:this={analyticsContainer} class="section relative overflow-hidden bg-background">
  <!-- Background Elements -->
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_40%_20%,rgba(99,102,241,0.05)_0%,transparent_100%)]"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_60%_80%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>

  <div class="container relative">
    <!-- Section Header -->
    <div class="text-center mb-16 analytics-header">
      <h2 class="text-4xl md:text-5xl font-display font-bold mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
        Real-Time Analytics
      </h2>
      <p class="text-text-secondary max-w-2xl mx-auto">
        Track our performance, growth, and the impact we're making in the software development industry.
      </p>
    </div>

    <!-- Key Metrics Grid -->
    <div class="metrics-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
      {#each metrics as metric}
        <div class="metric-card group">
          <div class="relative p-6 bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl hover:border-primary/20 transition-all duration-300 hover:-translate-y-1">
            <!-- Background Gradient -->
            <div class="absolute inset-0 bg-gradient-to-br {metric.color} opacity-5 rounded-2xl"></div>
            
            <!-- Content -->
            <div class="relative">
              <div class="flex items-center justify-between mb-4">
                <div class="text-3xl">{metric.icon}</div>
                <span class="text-xs px-2 py-1 bg-green-500/20 text-green-400 rounded-full">
                  {metric.change}
                </span>
              </div>
              <div class="text-2xl font-bold text-text-primary mb-1">
                {metric.value}
              </div>
              <div class="text-sm text-text-secondary">
                {metric.label}
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>

    <!-- Live Statistics -->
    <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-8 mb-16">
      <h3 class="text-xl font-bold text-text-primary mb-6 flex items-center">
        <div class="w-3 h-3 bg-green-400 rounded-full mr-3 animate-pulse"></div>
        Live Statistics
      </h3>
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 text-center">
        <div>
          <div class="text-3xl font-bold text-primary mb-2">
            {animatedVisitors.toLocaleString()}
          </div>
          <div class="text-sm text-text-secondary">Visitors Today</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-secondary mb-2">
            {animatedProjects}
          </div>
          <div class="text-sm text-text-secondary">Projects Completed</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-accent mb-2">
            {animatedSatisfaction}%
          </div>
          <div class="text-sm text-text-secondary">Client Satisfaction</div>
        </div>
        <div>
          <div class="text-3xl font-bold text-primary mb-2">
            {animatedTeamSize}
          </div>
          <div class="text-sm text-text-secondary">Team Members</div>
        </div>
      </div>
    </div>

    <!-- Charts Grid -->
    <div class="charts-grid grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Performance Trends -->
      <div class="chart-container lg:col-span-2">
        <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-6">
          <h3 class="text-lg font-semibold text-text-primary mb-4">Performance Trends</h3>
          <div class="h-64">
            <canvas bind:this={performanceChart}></canvas>
          </div>
        </div>
      </div>

      <!-- Project Distribution -->
      <div class="chart-container">
        <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-6">
          <h3 class="text-lg font-semibold text-text-primary mb-4">Project Types</h3>
          <div class="h-64">
            <canvas bind:this={projectsChart}></canvas>
          </div>
        </div>
      </div>

      <!-- Technology Stack -->
      <div class="chart-container">
        <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-6">
          <h3 class="text-lg font-semibold text-text-primary mb-4">Tech Stack Usage</h3>
          <div class="space-y-4">
            {#each [
              { name: 'React/Vue.js', percentage: 85, color: 'bg-primary' },
              { name: 'Node.js/Python', percentage: 78, color: 'bg-secondary' },
              { name: 'Cloud Platforms', percentage: 92, color: 'bg-accent' },
              { name: 'AI/ML Tools', percentage: 65, color: 'bg-green-500' }
            ] as tech}
              <div>
                <div class="flex justify-between text-sm mb-1">
                  <span class="text-text-primary">{tech.name}</span>
                  <span class="text-text-secondary">{tech.percentage}%</span>
                </div>
                <div class="w-full bg-gray-700 rounded-full h-2">
                  <div class="{tech.color} h-2 rounded-full transition-all duration-1000" style="width: {tech.percentage}%"></div>
                </div>
              </div>
            {/each}
          </div>
        </div>
      </div>

      <!-- Client Satisfaction -->
      <div class="chart-container lg:col-span-2">
        <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-6">
          <h3 class="text-lg font-semibold text-text-primary mb-4">Quarterly Satisfaction</h3>
          <div class="h-64">
            <canvas bind:this={satisfactionChart}></canvas>
          </div>
        </div>
      </div>
    </div>

    <!-- Real-time Updates -->
    <div class="mt-16 text-center">
      <div class="inline-flex items-center space-x-2 px-6 py-3 bg-primary/10 rounded-full">
        <div class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
        <span class="text-text-secondary text-sm">Data updates every 30 seconds</span>
      </div>
    </div>
  </div>
</section> 