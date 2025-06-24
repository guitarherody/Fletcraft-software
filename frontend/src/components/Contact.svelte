<script lang="ts">
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
</script>

<section id="contact" class="relative py-20 px-4">
  <!-- Simple background -->
  <div class="absolute inset-0 bg-gradient-to-b from-black to-gray-900"></div>
  
  <div class="relative max-w-4xl mx-auto">
    <!-- Section Header -->
    <div class="text-center mb-16">
      <h2 class="text-4xl md:text-5xl font-bold mb-6 text-white">
        Get in <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">Touch</span>
      </h2>
      <p class="text-gray-300 max-w-2xl mx-auto text-lg">
        Ready to transform your ideas into reality? Let's start a conversation about your project.
      </p>
    </div>
    
    <!-- Contact Form -->
    <div class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-8">
      
      <!-- Success Message -->
      {#if showSuccess}
        <div class="mb-6 p-4 bg-green-500/10 border border-green-500/20 rounded-lg">
          <p class="text-green-400 text-center">✅ Thank you! Your message has been sent successfully.</p>
        </div>
      {/if}
      
      <!-- Error Message -->
      {#if showError}
        <div class="mb-6 p-4 bg-red-500/10 border border-red-500/20 rounded-lg">
          <p class="text-red-400 text-center">❌ {errorMessage}</p>
        </div>
      {/if}
      
      <form on:submit|preventDefault={handleSubmit} class="space-y-6">
        
        <!-- Name Input -->
        <div>
          <label for="name" class="block text-sm font-medium text-gray-300 mb-2">
            Your Name
          </label>
          <input
            type="text"
            id="name"
            bind:value={name}
            required
            class="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 transition-all text-white placeholder-gray-400"
            placeholder="John Doe"
          />
        </div>
        
        <!-- Email Input -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-300 mb-2">
            Email Address
          </label>
          <input
            type="email"
            id="email"
            bind:value={email}
            required
            class="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 transition-all text-white placeholder-gray-400"
            placeholder="john@example.com"
          />
        </div>
        
        <!-- Subject Input -->
        <div>
          <label for="subject" class="block text-sm font-medium text-gray-300 mb-2">
            Subject
          </label>
          <input
            type="text"
            id="subject"
            bind:value={subject}
            required
            class="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 transition-all text-white placeholder-gray-400"
            placeholder="Project consultation"
          />
        </div>
        
        <!-- Message Input -->
        <div>
          <label for="message" class="block text-sm font-medium text-gray-300 mb-2">
            Your Message
          </label>
          <textarea
            id="message"
            bind:value={message}
            required
            rows="5"
            class="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 transition-all resize-none text-white placeholder-gray-400"
            placeholder="Tell us about your project..."
          ></textarea>
        </div>
        
        <!-- Submit Button -->
        <button
          type="submit"
          disabled={isSubmitting}
          class="w-full px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 rounded-lg text-white font-medium transition-all duration-200 hover:scale-105 disabled:opacity-50 disabled:hover:scale-100"
        >
          <span class="flex items-center justify-center">
            {#if isSubmitting}
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            {/if}
            {isSubmitting ? 'Sending...' : 'Send Message'}
          </span>
        </button>
        
      </form>
    </div>
  </div>
</section> 