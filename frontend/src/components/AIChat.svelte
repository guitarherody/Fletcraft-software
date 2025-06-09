<script lang="ts">
  import { onMount } from 'svelte';
  import { chatMessages, isChatOpen, isTyping, soundEnabled } from '../lib/stores';
  import { get } from 'svelte/store';
  import { Howl } from 'howler';

  let messageInput = '';
  let chatContainer: HTMLDivElement;
  let messagesContainer: HTMLDivElement;

  // Sound effects
  let messageSound: Howl;
  let openSound: Howl;

  // AI responses for different topics
  const aiResponses = {
    greeting: [
      "Hello! I'm here to help you with your software project. What can I assist you with today?",
      "Hi there! Ready to bring your digital ideas to life? Let's chat about your project needs.",
      "Welcome! I'm your AI assistant at Fletcraft Software. How can I help you today?"
    ],
    services: [
      "We offer custom software development, web applications, mobile apps, AI/ML solutions, cybersecurity, and cloud services. Which area interests you most?",
      "Our expertise spans full-stack development, mobile solutions, AI implementation, and secure cloud architectures. What's your project focus?",
      "From e-commerce platforms to AI-powered analytics - we build it all. Tell me about your vision!"
    ],
    pricing: [
      "Project costs vary based on complexity and scope. Would you like to schedule a free consultation to discuss your specific needs?",
      "We offer flexible pricing models including fixed-price projects and ongoing development partnerships. Let's discuss your requirements!",
      "Every project is unique! I can connect you with our team for a detailed quote. What's your project timeline and budget range?"
    ],
    technology: [
      "We work with cutting-edge technologies including React, Vue, Node.js, Python, AI/ML frameworks, and cloud platforms. What tech stack interests you?",
      "Our team specializes in modern frameworks, microservices architecture, and emerging technologies like blockchain and AI. Any specific tech requirements?",
      "From frontend frameworks to backend infrastructure, we've got you covered. What's your preferred technology stack?"
    ],
    timeline: [
      "Project timelines typically range from 2-6 months depending on complexity. What's your target launch date?",
      "We can deliver MVPs in 4-6 weeks and full solutions in 2-4 months. When do you need your project completed?",
      "Timeline depends on scope and features. We prioritize quality delivery. What's your ideal project timeline?"
    ]
  };

  function initSounds() {
    if (get(soundEnabled)) {
      messageSound = new Howl({
        src: ['data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmAZBDuM0+/UfzEGJIXO8tiJNwgZaLvt559NEAxQp+PwtmMcBjuM0+/UfzEGJIXO8tiJNwgZaLvt559NEAxQp+PwtmMcBj'],
        volume: 0.3
      });

      openSound = new Howl({
        src: ['data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmAZBDuM0+/UfzEGJIXO8tiJNwgZaLvt559NEAxQp+PwtmMcBj'],
        volume: 0.2
      });
    }
  }

  function getAIResponse(message: string): string {
    const lowerMessage = message.toLowerCase();
    
    if (lowerMessage.includes('hello') || lowerMessage.includes('hi') || lowerMessage.includes('hey')) {
      return getRandomResponse('greeting');
    } else if (lowerMessage.includes('service') || lowerMessage.includes('what do you do')) {
      return getRandomResponse('services');
    } else if (lowerMessage.includes('price') || lowerMessage.includes('cost') || lowerMessage.includes('budget')) {
      return getRandomResponse('pricing');
    } else if (lowerMessage.includes('technology') || lowerMessage.includes('tech') || lowerMessage.includes('framework')) {
      return getRandomResponse('technology');
    } else if (lowerMessage.includes('timeline') || lowerMessage.includes('how long') || lowerMessage.includes('when')) {
      return getRandomResponse('timeline');
    } else {
      return "That's a great question! I'd love to connect you with our team who can provide detailed information. Would you like to schedule a consultation?";
    }
  }

  function getRandomResponse(category: keyof typeof aiResponses): string {
    const responses = aiResponses[category];
    return responses[Math.floor(Math.random() * responses.length)];
  }

  function toggleChat() {
    isChatOpen.update(open => {
      const newState = !open;
      if (newState && openSound) {
        openSound.play();
      }
      return newState;
    });
  }

  function sendMessage() {
    if (!messageInput.trim()) return;

    // Add user message
    chatMessages.update(messages => [
      ...messages,
      {
        id: Date.now(),
        type: 'user',
        message: messageInput.trim(),
        timestamp: new Date()
      }
    ]);

    const userMessage = messageInput.trim();
    messageInput = '';

    // Show typing indicator
    isTyping.set(true);

    // Simulate AI thinking time
    setTimeout(() => {
      const aiResponse = getAIResponse(userMessage);
      
      chatMessages.update(messages => [
        ...messages,
        {
          id: Date.now(),
          type: 'bot',
          message: aiResponse,
          timestamp: new Date()
        }
      ]);

      isTyping.set(false);
      
      if (messageSound) {
        messageSound.play();
      }

      // Auto-scroll to bottom
      setTimeout(() => {
        if (messagesContainer) {
          messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
      }, 100);
    }, 1000 + Math.random() * 2000); // Random delay 1-3 seconds
  }

  function handleKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  }

  onMount(() => {
    initSounds();
  });

  $: if ($isChatOpen && messagesContainer) {
    setTimeout(() => {
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 100);
  }
</script>

<!-- Chat Toggle Button -->
<button
  on:click={toggleChat}
  class="fixed bottom-6 right-6 z-50 w-16 h-16 bg-gradient-to-r from-primary to-secondary rounded-full shadow-lg hover:shadow-xl transform hover:scale-110 transition-all duration-300 flex items-center justify-center group"
  aria-label="Toggle AI Chat"
>
  {#if $isChatOpen}
    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
    </svg>
  {:else}
    <svg class="w-6 h-6 text-white group-hover:animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
    </svg>
  {/if}
</button>

<!-- Chat Window -->
{#if $isChatOpen}
  <div bind:this={chatContainer} class="fixed bottom-24 right-6 w-96 h-[500px] bg-background/95 backdrop-blur-xl border border-primary/20 rounded-2xl shadow-2xl z-40 flex flex-col overflow-hidden">
    <!-- Chat Header -->
    <div class="p-4 border-b border-primary/10 bg-gradient-to-r from-primary/10 to-secondary/10">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-full bg-gradient-to-r from-primary to-secondary flex items-center justify-center">
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
          </svg>
        </div>
        <div>
          <h3 class="font-semibold text-text-primary">AI Assistant</h3>
          <p class="text-xs text-text-secondary">Always here to help</p>
        </div>
      </div>
    </div>

    <!-- Messages Container -->
    <div bind:this={messagesContainer} class="flex-1 overflow-y-auto p-4 space-y-4">
      {#each $chatMessages as message}
        <div class="flex {message.type === 'user' ? 'justify-end' : 'justify-start'}">
          <div class="max-w-[80%] p-3 rounded-lg {message.type === 'user' 
            ? 'bg-gradient-to-r from-primary to-secondary text-white ml-4' 
            : 'bg-primary/10 text-text-primary mr-4'}">
            <p class="text-sm">{message.message}</p>
            <span class="text-xs opacity-70">
              {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </span>
          </div>
        </div>
      {/each}

      {#if $isTyping}
        <div class="flex justify-start">
          <div class="bg-primary/10 text-text-primary p-3 rounded-lg mr-4">
            <div class="flex space-x-1">
              <div class="w-2 h-2 bg-primary rounded-full animate-bounce"></div>
              <div class="w-2 h-2 bg-primary rounded-full animate-bounce" style="animation-delay: 0.1s"></div>
              <div class="w-2 h-2 bg-primary rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
            </div>
          </div>
        </div>
      {/if}
    </div>

    <!-- Input Area -->
    <div class="p-4 border-t border-primary/10">
      <div class="flex space-x-2">
        <input
          bind:value={messageInput}
          on:keypress={handleKeyPress}
          placeholder="Ask me anything about our services..."
          class="flex-1 px-3 py-2 bg-background/60 border border-primary/20 rounded-lg focus:outline-none focus:border-primary/40 text-text-primary placeholder:text-text-secondary/60"
        />
        <button
          on:click={sendMessage}
          disabled={!messageInput.trim()}
          class="px-4 py-2 bg-gradient-to-r from-primary to-secondary text-white rounded-lg hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
{/if}

<style>
  /* Custom scrollbar for chat messages */
  :global(.chat-messages::-webkit-scrollbar) {
    width: 4px;
  }
  
  :global(.chat-messages::-webkit-scrollbar-track) {
    background: transparent;
  }
  
  :global(.chat-messages::-webkit-scrollbar-thumb) {
    background: rgba(99, 102, 241, 0.3);
    border-radius: 2px;
  }
</style> 