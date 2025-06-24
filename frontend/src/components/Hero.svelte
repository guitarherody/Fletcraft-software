<script lang="ts">
  import { navigateTo } from '../lib/router';
  
  // Simple hero component with CSS-only animations
</script>

<section id="home" class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden">
  <!-- Simple background gradient -->
  <div class="absolute inset-0 bg-gradient-to-br from-gray-900 via-purple-900/20 to-blue-900/20"></div>
  
  <!-- Main content -->
  <div class="relative z-10 max-w-6xl mx-auto text-center">
    
    <!-- Badge -->
    <div class="animate-in mb-8" style="animation-delay: 0ms;">
      <span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-white/10 text-white border border-white/20 backdrop-blur-sm">
        Welcome to Fletcraft Software
      </span>
    </div>

    <!-- Main title -->
    <h1 class="animate-in text-5xl md:text-7xl font-bold text-white mb-6" style="animation-delay: 200ms;">
      Crafting Software
      <span class="block text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">
        Excellence
      </span>
    </h1>

    <!-- Subtitle -->
    <p class="animate-in text-xl md:text-2xl text-gray-300 mb-12 max-w-3xl mx-auto leading-relaxed" style="animation-delay: 400ms;">
      Transforming ideas into powerful digital solutions with cutting-edge technology and innovative design.
    </p>

    <!-- CTA Buttons -->
    <div class="animate-in flex flex-col sm:flex-row gap-4 justify-center items-center" style="animation-delay: 600ms;">
      <button 
        on:click={() => navigateTo('/pricing')}
        class="px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg font-semibold hover:from-purple-700 hover:to-pink-700 transition-all duration-300 shadow-lg hover:shadow-purple-500/25 hover:scale-105"
      >
        Get Started
      </button>
      <button 
        on:click={() => document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' })}
        class="px-8 py-4 bg-white/10 text-white rounded-lg font-semibold backdrop-blur-sm border border-white/20 hover:bg-white/20 transition-all duration-300"
      >
        Learn More
      </button>
    </div>

    <!-- Simple feature highlights -->
    <div class="animate-in mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto" style="animation-delay: 800ms;">
      
      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm">
        <div class="text-3xl mb-4">⚡</div>
        <h3 class="text-white font-semibold mb-2">Lightning Fast</h3>
        <p class="text-gray-400 text-sm">Optimized performance and cutting-edge technology</p>
      </div>

      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm">
        <div class="text-3xl mb-4">🛡️</div>
        <h3 class="text-white font-semibold mb-2">Secure & Reliable</h3>
        <p class="text-gray-400 text-sm">Enterprise-grade security and 99.9% uptime</p>
      </div>

      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm">
        <div class="text-3xl mb-4">🎯</div>
        <h3 class="text-white font-semibold mb-2">Custom Solutions</h3>
        <p class="text-gray-400 text-sm">Tailored to your unique business needs</p>
      </div>

    </div>

  </div>

  <!-- Scroll indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
    <div class="w-6 h-10 border-2 border-white/30 rounded-full flex justify-center">
      <div class="w-1 h-3 bg-white/60 rounded-full mt-2 animate-pulse"></div>
    </div>
  </div>

</section>

<style>
  .animate-in {
    animation: fadeInUp 0.8s ease-out both;
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(2rem);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .glass-card {
    transition: all 0.3s ease;
  }

  .glass-card:hover {
    transform: translateY(-4px);
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.2);
  }

  /* Responsive text scaling */
  @media (max-width: 640px) {
    h1 {
      font-size: 2.5rem;
      line-height: 1.1;
    }
  }
</style> 