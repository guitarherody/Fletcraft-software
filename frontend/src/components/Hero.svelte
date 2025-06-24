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
  
  <!-- Clean Hero Lighting -->
  <div class="hero-lighting">
    <div class="hero-glow-particle glow-1"></div>
    <div class="hero-glow-particle glow-2"></div>
    <div class="hero-glow-particle glow-3"></div>
    
    <div class="hero-light-beam beam-1"></div>
    <div class="hero-light-beam beam-2"></div>
  </div>
  
  <!-- Atmospheric Smoke -->
  <div class="hero-smoke">
    <div class="hero-smoke-particle hero-smoke-1"></div>
    <div class="hero-smoke-particle hero-smoke-2"></div>
    <div class="hero-smoke-particle hero-smoke-3"></div>
    <div class="hero-smoke-particle hero-smoke-4"></div>
    <div class="hero-smoke-particle hero-smoke-5"></div>
    <div class="hero-smoke-particle hero-smoke-6"></div>
  </div>
  
  <!-- Purple & Emerald Accent Particles -->
  <div class="hero-accent-particles">
    <div class="accent-particle purple-particle accent-1"></div>
    <div class="accent-particle emerald-particle accent-2"></div>
    <div class="accent-particle purple-particle accent-3"></div>
    <div class="accent-particle emerald-particle accent-4"></div>
    <div class="accent-particle purple-particle accent-5"></div>
    <div class="accent-particle emerald-particle accent-6"></div>
  </div>
  
  <!-- Main content -->
  <div class="relative z-10 max-w-6xl mx-auto text-center">
    
    <!-- Badge -->
    <div class="animate-in mb-8" style="animation-delay: 0ms;">
      <span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-white/10 text-white border border-emerald-400/30 backdrop-blur-sm">
        Welcome to Fletcraft Software
      </span>
    </div>

    <!-- Main title -->
    <h1 class="animate-in text-5xl md:text-7xl font-bold mb-6" style="animation-delay: 200ms;">
      <span class="block text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-purple-400 to-white">
        Crafting Software
      </span>
      <span class="block text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-violet-400">
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
        class="px-8 py-4 bg-gradient-to-r from-emerald-600 to-purple-600 text-white rounded-lg font-semibold hover:from-emerald-700 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-emerald-500/25 hover:scale-105"
      >
        Get Started
      </button>
      <button 
        on:click={() => document.getElementById('services')?.scrollIntoView({ behavior: 'smooth' })}
        class="px-8 py-4 bg-white/10 text-white rounded-lg font-semibold backdrop-blur-sm border border-purple-400/30 hover:bg-purple-500/20 hover:border-purple-400/50 transition-all duration-300"
      >
        Learn More
      </button>
    </div>

    <!-- Simple feature highlights -->
    <div class="animate-in mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto" style="animation-delay: 800ms;">
      
      <div class="glass-card p-6 rounded-2xl bg-white/5 border border-emerald-400/20 backdrop-blur-sm">
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
    <div class="w-6 h-10 border-2 border-emerald-400/50 rounded-full flex justify-center">
      <div class="w-1 h-3 bg-emerald-400/60 rounded-full mt-2 animate-pulse"></div>
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
    width: 4px;
    height: 4px;
    border-radius: 50%;
    animation: heroFireflyFloat 8s linear infinite;
  }

  /* Firefly Trail Effects for Hero Particles */
  .hero-particle::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 400%;
    height: 400%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.3;
    z-index: -1;
    filter: blur(4px);
  }

  .hero-particle::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 800%;
    height: 800%;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.1;
    z-index: -2;
    filter: blur(12px);
  }

  .particle-1 {
    top: 10%;
    left: 10%;
    background: radial-gradient(circle, rgba(255, 220, 120, 1), rgba(255, 180, 60, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 200, 80, 1),
      0 0 40px rgba(255, 160, 50, 0.8),
      0 0 60px rgba(255, 140, 40, 0.6),
      0 0 80px rgba(255, 120, 30, 0.4);
    animation-delay: 0s;
  }

  .particle-1::before {
    background: radial-gradient(circle, rgba(255, 200, 80, 0.4), rgba(255, 160, 50, 0.2), transparent);
  }

  .particle-1::after {
    background: radial-gradient(circle, rgba(255, 180, 60, 0.2), rgba(255, 140, 40, 0.1), transparent);
  }

  .particle-2 {
    top: 20%;
    right: 15%;
    background: radial-gradient(circle, rgba(200, 120, 255, 1), rgba(180, 80, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(200, 100, 255, 1),
      0 0 40px rgba(180, 80, 255, 0.8),
      0 0 60px rgba(160, 60, 255, 0.6),
      0 0 80px rgba(140, 40, 255, 0.4);
    animation-delay: 1s;
  }

  .particle-2::before {
    background: radial-gradient(circle, rgba(200, 100, 255, 0.4), rgba(180, 80, 255, 0.2), transparent);
  }

  .particle-2::after {
    background: radial-gradient(circle, rgba(200, 120, 255, 0.2), rgba(200, 100, 255, 0.1), transparent);
  }

  .particle-3 {
    top: 70%;
    left: 20%;
    background: radial-gradient(circle, rgba(120, 255, 180, 1), rgba(80, 255, 140, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(100, 255, 160, 1),
      0 0 40px rgba(80, 255, 140, 0.8),
      0 0 60px rgba(60, 255, 120, 0.6),
      0 0 80px rgba(40, 255, 100, 0.4);
    animation-delay: 2s;
  }

  .particle-3::before {
    background: radial-gradient(circle, rgba(100, 255, 160, 0.4), rgba(80, 255, 140, 0.2), transparent);
  }

  .particle-3::after {
    background: radial-gradient(circle, rgba(120, 255, 180, 0.2), rgba(100, 255, 160, 0.1), transparent);
  }

  .particle-4 {
    top: 80%;
    right: 25%;
    background: radial-gradient(circle, rgba(255, 120, 180, 1), rgba(255, 80, 140, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 100, 160, 1),
      0 0 40px rgba(255, 80, 140, 0.8),
      0 0 60px rgba(255, 60, 120, 0.6),
      0 0 80px rgba(255, 40, 100, 0.4);
    animation-delay: 0.5s;
  }

  .particle-4::before {
    background: radial-gradient(circle, rgba(255, 100, 160, 0.4), rgba(255, 80, 140, 0.2), transparent);
  }

  .particle-4::after {
    background: radial-gradient(circle, rgba(255, 120, 180, 0.2), rgba(255, 100, 160, 0.1), transparent);
  }

  .particle-5 {
    top: 30%;
    left: 80%;
    background: radial-gradient(circle, rgba(120, 220, 255, 1), rgba(80, 180, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(100, 200, 255, 1),
      0 0 40px rgba(80, 180, 255, 0.8),
      0 0 60px rgba(60, 160, 255, 0.6),
      0 0 80px rgba(40, 140, 255, 0.4);
    animation-delay: 1.5s;
  }

  .particle-5::before {
    background: radial-gradient(circle, rgba(100, 200, 255, 0.4), rgba(80, 180, 255, 0.2), transparent);
  }

  .particle-5::after {
    background: radial-gradient(circle, rgba(120, 220, 255, 0.2), rgba(100, 200, 255, 0.1), transparent);
  }

  .particle-6 {
    top: 60%;
    left: 5%;
    background: radial-gradient(circle, rgba(255, 200, 120, 1), rgba(255, 180, 80, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 180, 100, 1),
      0 0 40px rgba(255, 160, 80, 0.8),
      0 0 60px rgba(255, 140, 60, 0.6),
      0 0 80px rgba(255, 120, 40, 0.4);
    animation-delay: 2.5s;
  }

  .particle-6::before {
    background: radial-gradient(circle, rgba(255, 180, 100, 0.4), rgba(255, 160, 80, 0.2), transparent);
  }

  .particle-6::after {
    background: radial-gradient(circle, rgba(255, 200, 120, 0.2), rgba(255, 180, 100, 0.1), transparent);
  }

  .particle-7 {
    top: 40%;
    right: 5%;
    background: radial-gradient(circle, rgba(180, 120, 255, 1), rgba(160, 80, 255, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(160, 100, 255, 1),
      0 0 40px rgba(140, 80, 255, 0.8),
      0 0 60px rgba(120, 60, 255, 0.6),
      0 0 80px rgba(100, 40, 255, 0.4);
    animation-delay: 3s;
  }

  .particle-7::before {
    background: radial-gradient(circle, rgba(160, 100, 255, 0.4), rgba(140, 80, 255, 0.2), transparent);
  }

  .particle-7::after {
    background: radial-gradient(circle, rgba(180, 120, 255, 0.2), rgba(160, 100, 255, 0.1), transparent);
  }

  .particle-8 {
    top: 15%;
    left: 50%;
    background: radial-gradient(circle, rgba(255, 140, 120, 1), rgba(255, 120, 80, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 120, 100, 1),
      0 0 40px rgba(255, 100, 80, 0.8),
      0 0 60px rgba(255, 80, 60, 0.6),
      0 0 80px rgba(255, 60, 40, 0.4);
    animation-delay: 0.8s;
  }

  .particle-8::before {
    background: radial-gradient(circle, rgba(255, 120, 100, 0.4), rgba(255, 100, 80, 0.2), transparent);
  }

  .particle-8::after {
    background: radial-gradient(circle, rgba(255, 140, 120, 0.2), rgba(255, 120, 100, 0.1), transparent);
  }

  .particle-9 {
    top: 85%;
    left: 60%;
    background: radial-gradient(circle, rgba(120, 255, 200, 1), rgba(80, 255, 180, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(100, 255, 190, 1),
      0 0 40px rgba(80, 255, 180, 0.8),
      0 0 60px rgba(60, 255, 160, 0.6),
      0 0 80px rgba(40, 255, 140, 0.4);
    animation-delay: 1.8s;
  }

  .particle-9::before {
    background: radial-gradient(circle, rgba(100, 255, 190, 0.4), rgba(80, 255, 180, 0.2), transparent);
  }

  .particle-9::after {
    background: radial-gradient(circle, rgba(120, 255, 200, 0.2), rgba(100, 255, 190, 0.1), transparent);
  }

  .particle-10 {
    top: 50%;
    right: 40%;
    background: radial-gradient(circle, rgba(255, 180, 200, 1), rgba(255, 160, 180, 0.8), transparent);
    box-shadow: 
      0 0 20px rgba(255, 160, 190, 1),
      0 0 40px rgba(255, 140, 170, 0.8),
      0 0 60px rgba(255, 120, 150, 0.6),
      0 0 80px rgba(255, 100, 130, 0.4);
    animation-delay: 2.8s;
  }

  .particle-10::before {
    background: radial-gradient(circle, rgba(255, 160, 190, 0.4), rgba(255, 140, 170, 0.2), transparent);
  }

  .particle-10::after {
    background: radial-gradient(circle, rgba(255, 180, 200, 0.2), rgba(255, 160, 190, 0.1), transparent);
  }

  @keyframes heroFireflyFloat {
    0% {
      transform: translateY(0) translateX(0) scale(0.8);
      opacity: 0.4;
      filter: brightness(0.8) blur(0px);
    }
    25% {
      transform: translateY(-30px) translateX(25px) scale(1.4);
      opacity: 1;
      filter: brightness(1.8) blur(0.5px);
    }
    50% {
      transform: translateY(-15px) translateX(-15px) scale(0.6);
      opacity: 0.6;
      filter: brightness(0.6) blur(0px);
    }
    75% {
      transform: translateY(-45px) translateX(35px) scale(1.2);
      opacity: 1;
      filter: brightness(1.5) blur(0.3px);
    }
    100% {
      transform: translateY(0) translateX(0) scale(0.8);
      opacity: 0.4;
      filter: brightness(0.8) blur(0px);
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

  /* Hero Light Refraction Effects */
  .hero-refractions {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }

  .hero-refraction {
    position: absolute;
    width: 180px;
    height: 3px;
    pointer-events: none;
    transform-origin: left center;
    animation: elegantHeroRefraction 20s ease-in-out infinite;
  }

  .hero-refraction::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 248, 245, 0.15) 12%,
      rgba(255, 235, 215, 0.25) 20%,
      rgba(255, 220, 185, 0.35) 28%,
      rgba(240, 255, 240, 0.3) 36%,
      rgba(220, 240, 255, 0.35) 44%,
      rgba(235, 220, 255, 0.3) 52%,
      rgba(255, 235, 245, 0.25) 60%,
      rgba(255, 245, 250, 0.2) 68%,
      rgba(252, 252, 255, 0.15) 76%,
      transparent 100%
    );
    filter: blur(1px);
    box-shadow: 
      0 0 8px rgba(255, 255, 255, 0.15),
      0 0 16px rgba(255, 240, 245, 0.08);
  }

  .hero-refraction::after {
    content: '';
    position: absolute;
    top: -2px;
    left: 0;
    width: 100%;
    height: 7px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 255, 255, 0.08) 25%,
      rgba(255, 255, 255, 0.2) 50%,
      rgba(255, 255, 255, 0.08) 75%,
      transparent 100%
    );
    filter: blur(3px);
    opacity: 0.6;
  }

  .refraction-beam-1 {
    top: 25%;
    left: 15%;
    transform: rotate(12deg);
    animation-delay: 0s;
  }

  .refraction-beam-2 {
    top: 65%;
    right: 20%;
    transform: rotate(-18deg);
    animation-delay: 5s;
  }

  .refraction-beam-3 {
    top: 35%;
    left: 65%;
    transform: rotate(8deg);
    animation-delay: 10s;
  }

  .refraction-beam-4 {
    top: 75%;
    left: 35%;
    transform: rotate(-10deg);
    animation-delay: 15s;
  }

  /* Hero Diamond Sparkles */
  .hero-diamond-sparkle {
    position: absolute;
    width: 10px;
    height: 10px;
    pointer-events: none;
    animation: elegantHeroSparkle 12s ease-in-out infinite;
  }

  .hero-diamond-sparkle::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 1.5px;
    height: 16px;
    background: linear-gradient(to bottom,
      transparent 0%,
      rgba(255, 255, 255, 0.3) 25%,
      rgba(255, 255, 255, 0.7) 50%,
      rgba(255, 255, 255, 0.3) 75%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.4px);
    box-shadow: 
      0 0 6px rgba(255, 255, 255, 0.4),
      0 0 12px rgba(255, 250, 255, 0.15);
  }

  .hero-diamond-sparkle::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 16px;
    height: 1.5px;
    background: linear-gradient(to right,
      transparent 0%,
      rgba(255, 255, 255, 0.3) 25%,
      rgba(255, 255, 255, 0.7) 50%,
      rgba(255, 255, 255, 0.3) 75%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.4px);
    box-shadow: 
      0 0 6px rgba(255, 255, 255, 0.4),
      0 0 12px rgba(255, 250, 255, 0.15);
  }

  .diamond-1 {
    top: 20%;
    left: 45%;
    animation-delay: 0s;
  }

  .diamond-2 {
    top: 65%;
    right: 25%;
    animation-delay: 4s;
  }

  .diamond-3 {
    top: 45%;
    left: 25%;
    animation-delay: 8s;
  }

  /* Enhanced Glass Orbs with refraction */
  .glass-orbs {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .glass-orb {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 25%, 
      rgba(255, 255, 255, 0.15) 0%,
      rgba(255, 255, 255, 0.08) 25%,
      rgba(240, 248, 255, 0.06) 50%,
      rgba(248, 240, 255, 0.04) 70%,
      rgba(255, 248, 240, 0.03) 85%,
      transparent 100%
    );
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 
      inset 0 1px 0 rgba(255, 255, 255, 0.25),
      0 4px 20px rgba(0, 0, 0, 0.15),
      0 0 12px rgba(255, 255, 255, 0.06);
    animation: elegantOrbFloat 16s ease-in-out infinite;
  }

  .glass-orb::before {
    content: '';
    position: absolute;
    top: 20%;
    left: 30%;
    width: 25%;
    height: 25%;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.4) 0%,
      rgba(255, 255, 255, 0.2) 50%,
      transparent 100%
    );
    filter: blur(1px);
  }

  .glass-orb::after {
    content: '';
    position: absolute;
    top: 65%;
    right: 35%;
    width: 12%;
    height: 12%;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.25) 0%,
      transparent 100%
    );
    filter: blur(0.5px);
  }

  .orb-1 {
    top: 15%;
    left: 75%;
    width: 65px;
    height: 65px;
    animation-delay: 0s;
  }

  .orb-2 {
    top: 70%;
    left: 8%;
    width: 50px;
    height: 50px;
    animation-delay: 3s;
  }

  .orb-3 {
    top: 25%;
    right: 8%;
    width: 40px;
    height: 40px;
    animation-delay: 6s;
  }

  .orb-4 {
    top: 85%;
    right: 35%;
    width: 55px;
    height: 55px;
    animation-delay: 9s;
  }

  .orb-5 {
    top: 55%;
    left: 3%;
    width: 35px;
    height: 35px;
    animation-delay: 12s;
  }

  @keyframes elegantHeroRefraction {
    0% {
      opacity: 0;
      transform: scale(0.9) translateX(-90px);
      filter: hue-rotate(0deg) brightness(0.9);
    }
    20% {
      opacity: 0.4;
      transform: scale(1) translateX(0px);
      filter: hue-rotate(30deg) brightness(1.2);
    }
    40% {
      opacity: 0.5;
      transform: scale(1.05) translateX(50px);
      filter: hue-rotate(80deg) brightness(1.4);
    }
    60% {
      opacity: 0.45;
      transform: scale(1) translateX(100px);
      filter: hue-rotate(140deg) brightness(1.3);
    }
    80% {
      opacity: 0.25;
      transform: scale(0.95) translateX(150px);
      filter: hue-rotate(200deg) brightness(1.1);
    }
    100% {
      opacity: 0;
      transform: scale(0.8) translateX(200px);
      filter: hue-rotate(240deg) brightness(0.9);
    }
  }

  @keyframes elegantHeroSparkle {
    0% {
      transform: scale(0) rotate(0deg);
      opacity: 0;
      filter: brightness(1);
    }
    25% {
      transform: scale(0.9) rotate(90deg);
      opacity: 0.7;
      filter: brightness(1.6);
    }
    50% {
      transform: scale(1.1) rotate(180deg);
      opacity: 1;
      filter: brightness(2);
    }
    75% {
      transform: scale(0.8) rotate(270deg);
      opacity: 0.5;
      filter: brightness(1.4);
    }
    100% {
      transform: scale(0) rotate(360deg);
      opacity: 0;
      filter: brightness(1);
    }
  }

  @keyframes elegantOrbFloat {
    0% {
      transform: translateY(0) translateX(0) scale(1);
      filter: hue-rotate(0deg) brightness(1);
    }
    30% {
      transform: translateY(-15px) translateX(12px) scale(1.03);
      filter: hue-rotate(60deg) brightness(1.1);
    }
    60% {
      transform: translateY(-8px) translateX(-8px) scale(0.98);
      filter: hue-rotate(120deg) brightness(1.05);
    }
    100% {
      transform: translateY(0) translateX(0) scale(1);
      filter: hue-rotate(180deg) brightness(1);
    }
  }

  /* Clean Hero Lighting */
  .hero-lighting {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .hero-glow-particle {
    position: absolute;
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 120, 60, 1) 0%,
      rgba(255, 80, 40, 0.8) 40%,
      rgba(180, 50, 30, 0.4) 70%,
      transparent 100%
    );
    filter: blur(0.4px);
    box-shadow: 
      0 0 8px rgba(255, 100, 50, 0.8),
      0 0 16px rgba(255, 80, 40, 0.4),
      0 0 24px rgba(200, 60, 30, 0.2);
    animation: ominousHeroGlow 10s ease-in-out infinite;
  }

  .hero-light-beam {
    position: absolute;
    width: 180px;
    height: 1px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 100, 50, 0.12) 20%,
      rgba(255, 120, 60, 0.3) 50%,
      rgba(255, 100, 50, 0.12) 80%,
      transparent 100%
    );
    filter: blur(0.6px);
    animation: mysteriousHeroBeamSweep 16s ease-in-out infinite;
    transform-origin: left center;
  }

  .glow-1 {
    top: 25%;
    left: 20%;
    animation-delay: 0s;
  }

  .glow-2 {
    top: 70%;
    right: 15%;
    animation-delay: 4s;
  }

  .glow-3 {
    top: 45%;
    left: 75%;
    animation-delay: 8s;
  }

  .beam-1 {
    top: 35%;
    left: -150px;
    transform: rotate(6deg);
    animation-delay: 2s;
  }

  .beam-2 {
    top: 80%;
    left: -150px;
    transform: rotate(-8deg);
    animation-delay: 10s;
  }

  @keyframes ominousHeroGlow {
    0% {
      transform: scale(0.7) translateX(0) translateY(0) rotate(0deg);
      opacity: 0.5;
      filter: blur(0.4px) brightness(1) hue-rotate(0deg);
    }
    25% {
      transform: scale(1.4) translateX(20px) translateY(-15px) rotate(90deg);
      opacity: 1.2;
      filter: blur(0.2px) brightness(1.8) hue-rotate(30deg);
    }
    50% {
      transform: scale(0.9) translateX(-10px) translateY(-25px) rotate(180deg);
      opacity: 0.8;
      filter: blur(0.5px) brightness(1.3) hue-rotate(60deg);
    }
    75% {
      transform: scale(1.6) translateX(15px) translateY(-10px) rotate(270deg);
      opacity: 1.4;
      filter: blur(0.3px) brightness(2) hue-rotate(90deg);
    }
    100% {
      transform: scale(0.7) translateX(0) translateY(0) rotate(360deg);
      opacity: 0.5;
      filter: blur(0.4px) brightness(1) hue-rotate(120deg);
    }
  }

  @keyframes mysteriousHeroBeamSweep {
    0% {
      transform: translateX(-180px) scale(0.8) rotate(0deg);
      opacity: 0;
      filter: hue-rotate(0deg) brightness(0.9);
    }
    20% {
      opacity: 0.3;
      transform: translateX(-20px) scale(1.2) rotate(2deg);
      filter: hue-rotate(25deg) brightness(1.4);
    }
    40% {
      opacity: 0.5;
      transform: translateX(35vw) scale(1.4) rotate(-3deg);
      filter: hue-rotate(50deg) brightness(1.7);
    }
    60% {
      opacity: 0.4;
      transform: translateX(70vw) scale(1.1) rotate(4deg);
      filter: hue-rotate(75deg) brightness(1.5);
    }
    80% {
      opacity: 0.2;
      transform: translateX(95vw) scale(0.9) rotate(-2deg);
      filter: hue-rotate(100deg) brightness(1.2);
    }
    100% {
      transform: translateX(calc(100vw + 180px)) scale(0.7) rotate(3deg);
      opacity: 0;
      filter: hue-rotate(120deg) brightness(0.9);
    }
  }

  /* Hero Atmospheric Smoke */
  .hero-smoke {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  .hero-smoke-particle {
    position: absolute;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(80, 40, 30, 0.08) 0%,
      rgba(100, 50, 40, 0.06) 30%,
      rgba(120, 60, 50, 0.04) 60%,
      transparent 100%
    );
    filter: blur(12px);
    animation: heroSmokeFloat 30s ease-in-out infinite;
    opacity: 0.4;
  }

  .hero-smoke-particle::before {
    content: '';
    position: absolute;
    top: -15px;
    left: -15px;
    width: 130%;
    height: 130%;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(60, 30, 25, 0.04) 0%,
      rgba(80, 40, 35, 0.03) 50%,
      transparent 100%
    );
    filter: blur(16px);
    animation: heroSmokeSwirl 35s linear infinite;
  }

  .hero-smoke-1 {
    bottom: 30%;
    left: 15%;
    animation-delay: 0s;
    transform: scale(1.2);
  }

  .hero-smoke-2 {
    bottom: 40%;
    right: 20%;
    animation-delay: 10s;
    transform: scale(0.8);
  }

  .hero-smoke-3 {
    bottom: 25%;
    left: 70%;
    animation-delay: 20s;
    transform: scale(1.5);
  }

  .hero-smoke-4 {
    bottom: 45%;
    right: 35%;
    animation-delay: 8s;
    transform: scale(1.1);
  }

  .hero-smoke-5 {
    bottom: 35%;
    left: 50%;
    animation-delay: 16s;
    transform: scale(0.9);
  }

  .hero-smoke-6 {
    bottom: 20%;
    right: 60%;
    animation-delay: 24s;
    transform: scale(1.3);
  }

  @keyframes heroSmokeFloat {
    0% {
      transform: translateY(0) translateX(0) rotate(0deg);
      opacity: 0.4;
    }
    25% {
      transform: translateY(-30vh) translateX(15px) rotate(90deg);
      opacity: 0.3;
    }
    50% {
      transform: translateY(-50vh) translateX(-10px) rotate(180deg);
      opacity: 0.2;
    }
    75% {
      transform: translateY(-70vh) translateX(20px) rotate(270deg);
      opacity: 0.15;
    }
    100% {
      transform: translateY(-90vh) translateX(-25px) rotate(360deg);
      opacity: 0;
    }
  }

  @keyframes heroSmokeSwirl {
    0% {
      transform: rotate(0deg) scale(1);
      opacity: 0.4;
    }
    50% {
      transform: rotate(180deg) scale(1.8);
      opacity: 0.2;
    }
    100% {
      transform: rotate(360deg) scale(1);
      opacity: 0.4;
    }
  }

  /* Purple & Emerald Accent Particles */
  .hero-accent-particles {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
  }

  .accent-particle {
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    filter: blur(0.8px);
    animation: accentFloat 14s ease-in-out infinite;
  }

  .purple-particle {
    background: radial-gradient(circle, 
      rgba(147, 51, 234, 1) 0%,
      rgba(126, 34, 206, 0.8) 30%,
      rgba(109, 40, 217, 0.6) 60%,
      rgba(88, 28, 135, 0.3) 80%,
      transparent 100%
    );
    box-shadow: 
      0 0 12px rgba(147, 51, 234, 0.8),
      0 0 24px rgba(126, 34, 206, 0.4),
      0 0 36px rgba(109, 40, 217, 0.2);
  }

  .emerald-particle {
    background: radial-gradient(circle, 
      rgba(16, 185, 129, 1) 0%,
      rgba(5, 150, 105, 0.8) 30%,
      rgba(4, 120, 87, 0.6) 60%,
      rgba(6, 95, 70, 0.3) 80%,
      transparent 100%
    );
    box-shadow: 
      0 0 12px rgba(16, 185, 129, 0.8),
      0 0 24px rgba(5, 150, 105, 0.4),
      0 0 36px rgba(4, 120, 87, 0.2);
  }

  /* Accent Particle Positions */
  .accent-1 {
    top: 20%;
    left: 25%;
    animation-delay: 0s;
  }

  .accent-2 {
    top: 70%;
    right: 30%;
    animation-delay: 2s;
  }

  .accent-3 {
    top: 45%;
    left: 15%;
    animation-delay: 4s;
  }

  .accent-4 {
    top: 30%;
    right: 15%;
    animation-delay: 6s;
  }

  .accent-5 {
    top: 65%;
    left: 60%;
    animation-delay: 8s;
  }

  .accent-6 {
    top: 15%;
    left: 75%;
    animation-delay: 10s;
  }

  @keyframes accentFloat {
    0% {
      transform: translateY(0) translateX(0) scale(0.8) rotate(0deg);
      opacity: 0.7;
      filter: blur(0.8px) brightness(1) hue-rotate(0deg);
    }
    25% {
      transform: translateY(-25px) translateX(15px) scale(1.4) rotate(90deg);
      opacity: 1.2;
      filter: blur(0.4px) brightness(1.6) hue-rotate(45deg);
    }
    50% {
      transform: translateY(-15px) translateX(-12px) scale(1.1) rotate(180deg);
      opacity: 0.9;
      filter: blur(0.6px) brightness(1.3) hue-rotate(90deg);
    }
    75% {
      transform: translateY(-35px) translateX(20px) scale(1.6) rotate(270deg);
      opacity: 1.4;
      filter: blur(0.3px) brightness(1.8) hue-rotate(135deg);
    }
    100% {
      transform: translateY(0) translateX(0) scale(0.8) rotate(360deg);
      opacity: 0.7;
      filter: blur(0.8px) brightness(1) hue-rotate(180deg);
    }
  }
</style> 