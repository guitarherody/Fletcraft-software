<script lang="ts">
  // Declare global navigation function
  declare global {
    var navigateTo: ((path: string) => void) | undefined;
  }

  function handleNavigation(path: string) {
    if (globalThis.navigateTo) {
      globalThis.navigateTo(path);
    } else {
      window.location.href = path;
    }
  }

  // Simple hero component with CSS-only animations
</script>

<section id="home" class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden">
  <!-- Darker background gradient -->
  <div class="absolute inset-0 bg-gradient-to-br from-gray-950 via-slate-900 to-gray-900"></div>
  
  <!-- Hero Particle Effects -->
  <div class="hero-particles">
    <div class="hero-particle particle-1"></div>
    <div class="hero-particle particle-2"></div>
    <div class="hero-particle particle-3"></div>
    <div class="hero-particle particle-4"></div>
    <div class="hero-particle particle-5"></div>
    <div class="hero-particle particle-6"></div>
    <div class="hero-particle particle-7"></div>
    <div class="hero-particle particle-8"></div>
    <div class="hero-particle particle-9"></div>
    <div class="hero-particle particle-10"></div>
  </div>

  <!-- Floating Orbs -->
  <div class="floating-orbs">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="orb orb-4"></div>
    <div class="orb orb-5"></div>
  </div>
  
  <!-- Main content -->
  <div class="relative z-10 max-w-6xl mx-auto text-center">
    
    <!-- Badge -->
    <div class="animate-in mb-8" style="animation-delay: 0ms;">
      <span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-white/10 text-white border border-orange-400/30 backdrop-blur-sm">
        Welcome to Fletcraft Software
      </span>
    </div>

    <!-- Main title -->
    <h1 class="animate-in text-5xl md:text-7xl font-bold text-white mb-6" style="animation-delay: 200ms;">
      Crafting Software
      <span class="block text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-red-400">
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
        on:click={() => handleNavigation('/pricing')}
        class="px-8 py-4 bg-gradient-to-r from-orange-600 to-red-600 text-white rounded-lg font-semibold hover:from-orange-700 hover:to-red-700 transition-all duration-300 shadow-lg hover:shadow-orange-500/25 hover:scale-105"
      >
        Get Started
      </button>
      <button 
        on:click={() => document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' })}
        class="px-8 py-4 bg-white/10 text-white rounded-lg font-semibold backdrop-blur-sm border border-orange-400/30 hover:bg-orange-500/20 hover:border-orange-400/50 transition-all duration-300"
      >
        Learn More
      </button>
    </div>

    <!-- Simple feature highlights -->
    <div class="animate-in mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto" style="animation-delay: 800ms;">
      
      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-orange-400/20 backdrop-blur-sm">
        <div class="text-3xl mb-4">⚡</div>
        <h3 class="text-white font-semibold mb-2">Lightning Fast</h3>
        <p class="text-gray-400 text-sm">Optimized performance and cutting-edge technology</p>
      </div>

      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-purple-400/20 backdrop-blur-sm">
        <div class="text-3xl mb-4">🛡️</div>
        <h3 class="text-white font-semibold mb-2">Secure & Reliable</h3>
        <p class="text-gray-400 text-sm">Enterprise-grade security and 99.9% uptime</p>
      </div>

      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-emerald-400/20 backdrop-blur-sm">
        <div class="text-3xl mb-4">🎯</div>
        <h3 class="text-white font-semibold mb-2">Custom Solutions</h3>
        <p class="text-gray-400 text-sm">Tailored to your unique business needs</p>
      </div>

    </div>

  </div>

  <!-- Scroll indicator -->
  <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
    <div class="w-6 h-10 border-2 border-orange-400/50 rounded-full flex justify-center">
      <div class="w-1 h-3 bg-orange-400/60 rounded-full mt-2 animate-pulse"></div>
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

  /* Hero Particle Effects */
  .hero-particles {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .hero-particle {
    position: absolute;
    width: 3px;
    height: 3px;
    border-radius: 50%;
    animation: heroFloat 6s linear infinite;
  }

  .particle-1 {
    top: 10%;
    left: 10%;
    background: radial-gradient(circle, #f97316, #ea580c);
    box-shadow: 0 0 6px #f97316;
    animation-delay: 0s;
  }

  .particle-2 {
    top: 20%;
    right: 15%;
    background: radial-gradient(circle, #a855f7, #9333ea);
    box-shadow: 0 0 6px #a855f7;
    animation-delay: 1s;
  }

  .particle-3 {
    top: 70%;
    left: 20%;
    background: radial-gradient(circle, #10b981, #059669);
    box-shadow: 0 0 6px #10b981;
    animation-delay: 2s;
  }

  .particle-4 {
    top: 80%;
    right: 25%;
    background: radial-gradient(circle, #ec4899, #be185d);
    box-shadow: 0 0 6px #ec4899;
    animation-delay: 0.5s;
  }

  .particle-5 {
    top: 30%;
    left: 80%;
    background: radial-gradient(circle, #06b6d4, #0891b2);
    box-shadow: 0 0 6px #06b6d4;
    animation-delay: 1.5s;
  }

  .particle-6 {
    top: 60%;
    left: 5%;
    background: radial-gradient(circle, #f59e0b, #d97706);
    box-shadow: 0 0 6px #f59e0b;
    animation-delay: 2.5s;
  }

  .particle-7 {
    top: 40%;
    right: 5%;
    background: radial-gradient(circle, #8b5cf6, #7c3aed);
    box-shadow: 0 0 6px #8b5cf6;
    animation-delay: 3s;
  }

  .particle-8 {
    top: 15%;
    left: 50%;
    background: radial-gradient(circle, #ef4444, #dc2626);
    box-shadow: 0 0 6px #ef4444;
    animation-delay: 0.8s;
  }

  .particle-9 {
    top: 85%;
    left: 60%;
    background: radial-gradient(circle, #14b8a6, #0f766e);
    box-shadow: 0 0 6px #14b8a6;
    animation-delay: 1.8s;
  }

  .particle-10 {
    top: 50%;
    right: 40%;
    background: radial-gradient(circle, #f472b6, #e11d48);
    box-shadow: 0 0 6px #f472b6;
    animation-delay: 2.8s;
  }

  @keyframes heroFloat {
    0% {
      transform: translateY(0) translateX(0) scale(0.8);
      opacity: 0.6;
    }
    25% {
      transform: translateY(-20px) translateX(15px) scale(1.2);
      opacity: 1;
    }
    50% {
      transform: translateY(-10px) translateX(-10px) scale(0.9);
      opacity: 0.8;
    }
    75% {
      transform: translateY(-30px) translateX(20px) scale(1.1);
      opacity: 1;
    }
    100% {
      transform: translateY(0) translateX(0) scale(0.8);
      opacity: 0.6;
    }
  }

  /* Floating Orbs */
  .floating-orbs {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }

  .orb {
    position: absolute;
    border-radius: 50%;
    animation: orbFloat 8s ease-in-out infinite;
  }

  .orb-1 {
    top: 15%;
    left: 15%;
    width: 60px;
    height: 60px;
    background: radial-gradient(circle at 30% 30%, rgba(249, 115, 22, 0.3), rgba(234, 88, 12, 0.1));
    border: 1px solid rgba(249, 115, 22, 0.2);
    backdrop-filter: blur(10px);
    animation-delay: 0s;
  }

  .orb-2 {
    top: 25%;
    right: 20%;
    width: 40px;
    height: 40px;
    background: radial-gradient(circle at 30% 30%, rgba(168, 85, 247, 0.3), rgba(147, 51, 234, 0.1));
    border: 1px solid rgba(168, 85, 247, 0.2);
    backdrop-filter: blur(8px);
    animation-delay: 1s;
  }

  .orb-3 {
    top: 60%;
    left: 10%;
    width: 80px;
    height: 80px;
    background: radial-gradient(circle at 30% 30%, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.1));
    border: 1px solid rgba(16, 185, 129, 0.2);
    backdrop-filter: blur(12px);
    animation-delay: 2s;
  }

  .orb-4 {
    top: 70%;
    right: 15%;
    width: 50px;
    height: 50px;
    background: radial-gradient(circle at 30% 30%, rgba(236, 72, 153, 0.3), rgba(190, 24, 93, 0.1));
    border: 1px solid rgba(236, 72, 153, 0.2);
    backdrop-filter: blur(10px);
    animation-delay: 1.5s;
  }

  .orb-5 {
    top: 40%;
    left: 70%;
    width: 35px;
    height: 35px;
    background: radial-gradient(circle at 30% 30%, rgba(6, 182, 212, 0.3), rgba(8, 145, 178, 0.1));
    border: 1px solid rgba(6, 182, 212, 0.2);
    backdrop-filter: blur(8px);
    animation-delay: 2.5s;
  }

  @keyframes orbFloat {
    0%, 100% {
      transform: translateY(0) translateX(0) scale(1);
      opacity: 0.6;
    }
    25% {
      transform: translateY(-30px) translateX(20px) scale(1.1);
      opacity: 0.8;
    }
    50% {
      transform: translateY(-20px) translateX(-15px) scale(0.9);
      opacity: 1;
    }
    75% {
      transform: translateY(-40px) translateX(25px) scale(1.05);
      opacity: 0.7;
    }
  }

  /* Responsive text scaling */
  @media (max-width: 640px) {
    h1 {
      font-size: 2.5rem;
      line-height: 1.1;
    }
    
    .hero-particle {
      width: 2px;
      height: 2px;
    }
    
    .orb-1, .orb-3 {
      width: 40px;
      height: 40px;
    }
    
    .orb-2, .orb-4, .orb-5 {
      width: 25px;
      height: 25px;
    }
  }
</style> 