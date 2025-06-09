<script lang="ts">
  import { onMount } from 'svelte';
  import gsap from 'gsap';
  import { submitContact } from '../lib/api';
  
  let name = '';
  let email = '';
  let subject = '';
  let message = '';
  let isSubmitting = false;
  let showSuccess = false;
  let showError = false;
  let errorMessage = '';
  
  async function handleSubmit() {
    isSubmitting = true;
    showError = false;
    showSuccess = false;
    
    try {
      const success = await submitContact({
        name,
        email,
        subject,
        message
      });
      
      if (success) {
        showSuccess = true;
        name = '';
        email = '';
        subject = '';
        message = '';
      } else {
        showError = true;
        errorMessage = 'Failed to send message. Please try again.';
      }
    } catch (error) {
      showError = true;
      errorMessage = 'An error occurred. Please try again later.';
    } finally {
      isSubmitting = false;
      
      // Hide success/error messages after 5 seconds
      setTimeout(() => {
        showSuccess = false;
        showError = false;
      }, 5000);
    }
  }
  
  onMount(() => {
    // Simplified animations for better performance
    setTimeout(() => {
      const contactElements = document.querySelectorAll('.contact-element');
      const contactSection = document.querySelector('#contact');
      
      if (contactElements.length > 0 && contactSection) {
        gsap.from(contactElements, {
          y: 20,
          opacity: 0,
          duration: 0.6,
          stagger: 0.1,
          scrollTrigger: {
            trigger: contactSection,
            start: 'top center+=100',
            toggleActions: 'play none none reverse'
          }
        });
      }
    }, 50);
  });
</script>

<section id="contact" class="section relative overflow-hidden bg-background py-16 sm:py-20 lg:py-24">
  <!-- Background Elements -->
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_70%_30%,rgba(99,102,241,0.05)_0%,transparent_100%)]"></div>
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_70%,rgba(139,92,246,0.05)_0%,transparent_100%)]"></div>
  
  <div class="container relative px-4 sm:px-6 lg:px-8">
    <div class="max-w-4xl mx-auto">
      <!-- Section Header -->
      <div class="text-center mb-12 sm:mb-16 contact-element">
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-bold mb-4 sm:mb-6 bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
          Get in Touch
        </h2>
        <p class="text-text-secondary max-w-2xl mx-auto text-base sm:text-lg">
          Ready to transform your ideas into reality? Let's start a conversation about your project.
        </p>
      </div>
      
      <!-- Contact Form -->
      <div class="relative">
        <!-- Form Container -->
        <div class="bg-background/40 backdrop-blur-xl border border-primary/10 rounded-2xl p-6 sm:p-8 md:p-12 contact-element">
          <!-- Success Message -->
          {#if showSuccess}
            <div class="mb-6 p-4 bg-green-500/10 border border-green-500/20 rounded-lg">
              <p class="text-green-400 text-center text-sm sm:text-base">✅ Thank you! Your message has been sent successfully.</p>
            </div>
          {/if}
          
          <!-- Error Message -->
          {#if showError}
            <div class="mb-6 p-4 bg-red-500/10 border border-red-500/20 rounded-lg">
              <p class="text-red-400 text-center text-sm sm:text-base">❌ {errorMessage}</p>
            </div>
          {/if}
          
          <form on:submit|preventDefault={handleSubmit} class="space-y-6">
            <!-- Name Input -->
            <div class="form-group">
              <label for="name" class="block text-sm font-medium text-text-secondary mb-2">
                Your Name
              </label>
              <input
                type="text"
                id="name"
                bind:value={name}
                required
                class="w-full px-4 py-3 bg-background/40 border border-primary/10 rounded-lg focus:outline-none focus:border-primary/30 focus:ring-2 focus:ring-primary/10 transition-all text-sm sm:text-base"
                placeholder="John Doe"
              />
            </div>
            
            <!-- Email Input -->
            <div class="form-group">
              <label for="email" class="block text-sm font-medium text-text-secondary mb-2">
                Email Address
              </label>
              <input
                type="email"
                id="email"
                bind:value={email}
                required
                class="w-full px-4 py-3 bg-background/40 border border-primary/10 rounded-lg focus:outline-none focus:border-primary/30 focus:ring-2 focus:ring-primary/10 transition-all text-sm sm:text-base"
                placeholder="john@example.com"
              />
            </div>
            
            <!-- Subject Input -->
            <div class="form-group">
              <label for="subject" class="block text-sm font-medium text-text-secondary mb-2">
                Subject
              </label>
              <input
                type="text"
                id="subject"
                bind:value={subject}
                required
                class="w-full px-4 py-3 bg-background/40 border border-primary/10 rounded-lg focus:outline-none focus:border-primary/30 focus:ring-2 focus:ring-primary/10 transition-all text-sm sm:text-base"
                placeholder="Project consultation"
              />
            </div>
            
            <!-- Message Input -->
            <div class="form-group">
              <label for="message" class="block text-sm font-medium text-text-secondary mb-2">
                Your Message
              </label>
              <textarea
                id="message"
                bind:value={message}
                required
                rows="5"
                class="w-full px-4 py-3 bg-background/40 border border-primary/10 rounded-lg focus:outline-none focus:border-primary/30 focus:ring-2 focus:ring-primary/10 transition-all resize-none text-sm sm:text-base"
                placeholder="Tell us about your project..."
              ></textarea>
            </div>
            
            <!-- Submit Button -->
            <button
              type="submit"
              disabled={isSubmitting}
              class="w-full relative group overflow-hidden px-6 sm:px-8 py-3 sm:py-4 bg-gradient-to-r from-primary to-secondary rounded-lg text-white font-medium transition-all duration-300 hover:scale-[1.02] disabled:opacity-50 disabled:hover:scale-100 text-sm sm:text-base"
            >
              <span class="relative z-10 flex items-center justify-center">
                {#if isSubmitting}
                  <svg class="animate-spin -ml-1 mr-3 h-4 w-4 sm:h-5 sm:w-5 text-white" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                {/if}
                {isSubmitting ? 'Sending...' : 'Send Message'}
              </span>
              <div class="absolute inset-0 bg-gradient-to-r from-secondary to-accent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </button>
          </form>
        </div>
        
        <!-- Decorative Elements -->
        <div class="absolute -z-10 top-1/2 -left-32 sm:-left-64 w-48 h-48 sm:w-96 sm:h-96 bg-primary/10 rounded-full filter blur-3xl"></div>
        <div class="absolute -z-10 bottom-0 -right-32 sm:-right-64 w-48 h-48 sm:w-96 sm:h-96 bg-secondary/10 rounded-full filter blur-3xl"></div>
      </div>
    </div>
  </div>
</section>

<style>
  input, textarea {
    @apply text-text-primary placeholder:text-text-secondary/50;
  }
  
  .form-group {
    @apply transform transition-transform duration-300 hover:-translate-y-1;
  }
</style> 