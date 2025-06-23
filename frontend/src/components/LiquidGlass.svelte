<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';

  export let variant: 'card' | 'panel' | 'button' | 'orb' | 'blob' = 'card';
  export let size: 'sm' | 'md' | 'lg' | 'xl' = 'md';
  export let intensity: 'light' | 'medium' | 'strong' = 'medium';
  export let animated: boolean = true;
  export let shimmer: boolean = false;
  export let morphing: boolean = false;
  export let className: string = '';

  let container: HTMLElement;
  let glassElement: HTMLElement;

  // Size configurations
  const sizes = {
    sm: 'w-16 h-16',
    md: 'w-32 h-32', 
    lg: 'w-48 h-48',
    xl: 'w-64 h-64'
  };

  // Intensity configurations
  const intensities = {
    light: {
      bg: 'bg-glass-white-5',
      blur: 'backdrop-blur-liquid',
      border: 'border-glass-primary-10',
      shadow: 'shadow-glass'
    },
    medium: {
      bg: 'bg-glass-white-10',
      blur: 'backdrop-blur-liquid-lg', 
      border: 'border-glass-primary-15',
      shadow: 'shadow-glass-lg'
    },
    strong: {
      bg: 'bg-glass-white-15',
      blur: 'backdrop-blur-liquid-xl',
      border: 'border-glass-primary-20', 
      shadow: 'shadow-glass-xl'
    }
  };

  // Variant configurations
  const variants = {
    card: 'rounded-2xl border',
    panel: 'rounded-3xl border-2', 
    button: 'rounded-xl border cursor-pointer transition-all duration-300 hover:scale-105',
    orb: 'rounded-full border-2',
    blob: 'border-2'
  };

  onMount(() => {
    if (animated && glassElement) {
      // Base floating animation
      gsap.to(glassElement, {
        y: -5,
        duration: 4,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1
      });

      // Rotation animation for orbs
      if (variant === 'orb') {
        gsap.to(glassElement, {
          rotation: 360,
          duration: 20,
          ease: 'none',
          repeat: -1
        });
      }

      // Pulse animation for buttons
      if (variant === 'button') {
        glassElement.addEventListener('mouseenter', () => {
          gsap.to(glassElement, {
            boxShadow: '0 12px 40px rgba(99, 102, 241, 0.3), 0 6px 20px rgba(139, 92, 246, 0.2)',
            duration: 0.3,
            ease: 'power2.out'
          });
        });

        glassElement.addEventListener('mouseleave', () => {
          gsap.to(glassElement, {
            boxShadow: intensities[intensity].shadow,
            duration: 0.3,
            ease: 'power2.out'
          });
        });
      }
    }
  });

  function getClasses() {
    const baseClasses = [
      intensities[intensity].bg,
      intensities[intensity].blur,
      intensities[intensity].border,
      intensities[intensity].shadow,
      variants[variant]
    ];

    if (variant !== 'blob') {
      baseClasses.push(sizes[size]);
    }

    if (shimmer) {
      baseClasses.push('relative overflow-hidden');
    }

    if (morphing) {
      baseClasses.push('animate-liquid-morph');
    }

    if (animated && variant !== 'button') {
      baseClasses.push('animate-liquid-float');
    }

    return baseClasses.join(' ');
  }
</script>

<div bind:this={container} class="relative {className}">
  <div 
    bind:this={glassElement}
    class={getClasses()}
    class:animate-liquid-pulse={animated && variant === 'orb'}
  >
    <!-- Shimmer effect overlay -->
    {#if shimmer}
      <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent animate-glass-shimmer"></div>
    {/if}

    <!-- Content slot -->
    <div class="relative z-10 h-full w-full flex items-center justify-center">
      <slot />
    </div>

    <!-- Morphing blob background -->
    {#if morphing && variant === 'blob'}
      <div class="absolute inset-0 bg-gradient-to-br from-primary/20 to-secondary/20 animate-liquid-morph"></div>
    {/if}
  </div>

  <!-- Floating glass particles for enhanced effect -->
  {#if animated && (variant === 'card' || variant === 'panel')}
    <div class="absolute inset-0 pointer-events-none overflow-hidden rounded-inherit">
      <div class="absolute top-2 right-2 w-1 h-1 bg-white/30 rounded-full animate-pulse"></div>
      <div class="absolute bottom-3 left-3 w-0.5 h-0.5 bg-primary/40 rounded-full animate-ping"></div>
      <div class="absolute top-1/2 left-1/4 w-1.5 h-1.5 bg-secondary/20 rounded-full animate-bounce"></div>
    </div>
  {/if}
</div>

<style>
  .rounded-inherit {
    border-radius: inherit;
  }

  /* Enhanced glass morphism effects */
  :global(.liquid-glass-enhanced) {
    position: relative;
    background: linear-gradient(135deg, 
      rgba(255, 255, 255, 0.1), 
      rgba(255, 255, 255, 0.05)
    );
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 
      0 8px 32px rgba(139, 92, 246, 0.12),
      inset 0 1px 0 rgba(255, 255, 255, 0.15);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  :global(.liquid-glass-enhanced::before) {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, 
      rgba(255, 255, 255, 0.15), 
      transparent
    );
    border-radius: inherit;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  :global(.liquid-glass-enhanced:hover::before) {
    opacity: 1;
  }

  :global(.liquid-glass-enhanced:hover) {
    transform: translateY(-2px);
    box-shadow: 
      0 16px 48px rgba(139, 92, 246, 0.2),
      inset 0 1px 0 rgba(255, 255, 255, 0.25);
  }

  /* Custom morphing blob shapes */
  :global(.morph-1) {
    border-radius: 60% 40% 30% 70%;
    animation: liquid-morph 8s ease-in-out infinite;
  }

  :global(.morph-2) {
    border-radius: 30% 60% 70% 40%;
    animation: liquid-morph 10s ease-in-out infinite reverse;
  }

  :global(.morph-3) {
    border-radius: 70% 30% 50% 50%;
    animation: liquid-morph 12s ease-in-out infinite;
    animation-delay: -2s;
  }
</style> 