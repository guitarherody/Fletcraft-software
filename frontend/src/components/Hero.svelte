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

  <!-- Hero Light Refractions -->
  <div class="hero-refractions">
    <div class="hero-refraction refraction-beam-1"></div>
    <div class="hero-refraction refraction-beam-2"></div>
    <div class="hero-refraction refraction-beam-3"></div>
    <div class="hero-refraction refraction-beam-4"></div>
    <div class="hero-diamond-sparkle diamond-1"></div>
    <div class="hero-diamond-sparkle diamond-2"></div>
    <div class="hero-diamond-sparkle diamond-3"></div>
  </div>

  <!-- Floating Glass Orbs with enhanced refractions -->
  <div class="glass-orbs">{#each Array(5) as _, i}
    <div class="glass-orb orb-{i + 1}"></div>
  {/each}</div>
  
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
    width: 300px;
    height: 6px;
    pointer-events: none;
    transform-origin: left center;
    animation: heroRefractionBeam 15s ease-in-out infinite;
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
      rgba(255, 20, 147, 0.9) 8%,
      rgba(255, 69, 0, 0.9) 16%,
      rgba(255, 215, 0, 0.9) 24%,
      rgba(173, 255, 47, 0.9) 32%,
      rgba(0, 255, 127, 0.9) 40%,
      rgba(0, 191, 255, 0.9) 48%,
      rgba(138, 43, 226, 0.9) 56%,
      rgba(255, 20, 147, 0.9) 64%,
      rgba(255, 105, 180, 0.9) 72%,
      rgba(255, 182, 193, 0.7) 80%,
      transparent 100%
    );
    filter: blur(1.5px);
    box-shadow: 
      0 0 15px rgba(255, 255, 255, 0.6),
      0 0 30px rgba(255, 100, 200, 0.4);
  }

  .hero-refraction::after {
    content: '';
    position: absolute;
    top: -3px;
    left: 0;
    width: 100%;
    height: 12px;
    background: linear-gradient(90deg, 
      transparent 0%,
      rgba(255, 255, 255, 0.5) 25%,
      rgba(255, 255, 255, 1) 50%,
      rgba(255, 255, 255, 0.5) 75%,
      transparent 100%
    );
    filter: blur(4px);
    opacity: 0.4;
  }

  .refraction-beam-1 {
    top: 20%;
    left: 10%;
    transform: rotate(25deg);
    animation-delay: 0s;
  }

  .refraction-beam-2 {
    top: 60%;
    right: 15%;
    transform: rotate(-35deg);
    animation-delay: 3s;
  }

  .refraction-beam-3 {
    top: 30%;
    left: 70%;
    transform: rotate(15deg);
    animation-delay: 6s;
  }

  .refraction-beam-4 {
    top: 80%;
    left: 30%;
    transform: rotate(-20deg);
    animation-delay: 9s;
  }

  /* Hero Diamond Sparkles */
  .hero-diamond-sparkle {
    position: absolute;
    width: 16px;
    height: 16px;
    pointer-events: none;
    animation: heroDiamondSparkle 8s ease-in-out infinite;
  }

  .hero-diamond-sparkle::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 3px;
    height: 30px;
    background: linear-gradient(to bottom,
      transparent 0%,
      rgba(255, 255, 255, 0.8) 20%,
      rgba(255, 255, 255, 1) 50%,
      rgba(255, 255, 255, 0.8) 80%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.8px);
    box-shadow: 
      0 0 15px rgba(255, 255, 255, 1),
      0 0 30px rgba(255, 200, 255, 0.8),
      0 0 45px rgba(200, 255, 255, 0.6);
  }

  .hero-diamond-sparkle::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 30px;
    height: 3px;
    background: linear-gradient(to right,
      transparent 0%,
      rgba(255, 255, 255, 0.8) 20%,
      rgba(255, 255, 255, 1) 50%,
      rgba(255, 255, 255, 0.8) 80%,
      transparent 100%
    );
    transform: translate(-50%, -50%);
    filter: blur(0.8px);
    box-shadow: 
      0 0 15px rgba(255, 255, 255, 1),
      0 0 30px rgba(255, 200, 255, 0.8),
      0 0 45px rgba(200, 255, 255, 0.6);
  }

  .diamond-1 {
    top: 15%;
    left: 50%;
    animation-delay: 0s;
  }

  .diamond-2 {
    top: 70%;
    right: 20%;
    animation-delay: 2.5s;
  }

  .diamond-3 {
    top: 40%;
    left: 20%;
    animation-delay: 5s;
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
    background: radial-gradient(circle at 30% 30%, 
      rgba(255, 255, 255, 0.3) 0%,
      rgba(255, 255, 255, 0.1) 30%,
      rgba(200, 150, 255, 0.08) 60%,
      rgba(150, 200, 255, 0.05) 80%,
      transparent 100%
    );
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.2);
    box-shadow: 
      inset 0 1px 0 rgba(255, 255, 255, 0.4),
      0 8px 32px rgba(0, 0, 0, 0.2),
      0 0 20px rgba(255, 255, 255, 0.1);
    animation: orbRefractionFloat 12s ease-in-out infinite;
  }

  .glass-orb::before {
    content: '';
    position: absolute;
    top: 15%;
    left: 25%;
    width: 30%;
    height: 30%;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.6) 0%,
      rgba(255, 255, 255, 0.3) 40%,
      transparent 100%
    );
    filter: blur(2px);
  }

  .glass-orb::after {
    content: '';
    position: absolute;
    top: 60%;
    right: 30%;
    width: 15%;
    height: 15%;
    border-radius: 50%;
    background: radial-gradient(circle, 
      rgba(255, 255, 255, 0.4) 0%,
      transparent 100%
    );
    filter: blur(1px);
  }

  .orb-1 {
    top: 20%;
    left: 80%;
    width: 80px;
    height: 80px;
    animation-delay: 0s;
  }

  .orb-2 {
    top: 70%;
    left: 10%;
    width: 60px;
    height: 60px;
    animation-delay: 2s;
  }

  .orb-3 {
    top: 30%;
    right: 10%;
    width: 50px;
    height: 50px;
    animation-delay: 4s;
  }

  .orb-4 {
    top: 80%;
    right: 30%;
    width: 70px;
    height: 70px;
    animation-delay: 6s;
  }

  .orb-5 {
    top: 50%;
    left: 5%;
    width: 45px;
    height: 45px;
    animation-delay: 8s;
  }

  @keyframes heroRefractionBeam {
    0% {
      opacity: 0;
      transform: scale(0) translateX(-150px);
      filter: hue-rotate(0deg) brightness(0.8);
    }
    15% {
      opacity: 0.8;
      transform: scale(1) translateX(0px);
      filter: hue-rotate(60deg) brightness(1.8);
    }
    30% {
      opacity: 1;
      transform: scale(1.3) translateX(80px);
      filter: hue-rotate(120deg) brightness(2.2);
    }
    50% {
      opacity: 0.9;
      transform: scale(1.1) translateX(160px);
      filter: hue-rotate(240deg) brightness(2);
    }
    70% {
      opacity: 0.6;
      transform: scale(0.9) translateX(240px);
      filter: hue-rotate(300deg) brightness(1.5);
    }
    85% {
      opacity: 0.3;
      transform: scale(0.6) translateX(300px);
      filter: hue-rotate(330deg) brightness(1);
    }
    100% {
      opacity: 0;
      transform: scale(0) translateX(350px);
      filter: hue-rotate(360deg) brightness(0.8);
    }
  }

  @keyframes heroDiamondSparkle {
    0% {
      transform: scale(0) rotate(0deg);
      opacity: 0;
      filter: brightness(1) blur(0px) hue-rotate(0deg);
    }
    20% {
      transform: scale(2) rotate(90deg);
      opacity: 1;
      filter: brightness(2.5) blur(1px) hue-rotate(60deg);
    }
    40% {
      transform: scale(1.2) rotate(180deg);
      opacity: 0.8;
      filter: brightness(1.8) blur(0.5px) hue-rotate(120deg);
    }
    60% {
      transform: scale(2.5) rotate(270deg);
      opacity: 1;
      filter: brightness(3) blur(1.5px) hue-rotate(240deg);
    }
    80% {
      transform: scale(1.5) rotate(360deg);
      opacity: 0.6;
      filter: brightness(2) blur(0.8px) hue-rotate(300deg);
    }
    100% {
      transform: scale(0) rotate(450deg);
      opacity: 0;
      filter: brightness(1) blur(0px) hue-rotate(360deg);
    }
  }

  @keyframes orbRefractionFloat {
    0% {
      transform: translateY(0) translateX(0) scale(1);
      filter: hue-rotate(0deg) brightness(1);
    }
    25% {
      transform: translateY(-20px) translateX(15px) scale(1.1);
      filter: hue-rotate(90deg) brightness(1.3);
    }
    50% {
      transform: translateY(-10px) translateX(-10px) scale(0.9);
      filter: hue-rotate(180deg) brightness(1.1);
    }
    75% {
      transform: translateY(-30px) translateX(20px) scale(1.05);
      filter: hue-rotate(270deg) brightness(1.2);
    }
    100% {
      transform: translateY(0) translateX(0) scale(1);
      filter: hue-rotate(360deg) brightness(1);
    }
  }
</style> 