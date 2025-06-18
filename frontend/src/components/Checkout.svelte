<script lang="ts">
  import { onMount } from 'svelte';
  import { fade, fly } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  export let service: any = null;
  export let onClose: () => void;

  let customerName = '';
  let customerEmail = '';
  let customerPhone = '';
  let isProcessing = false;
  let errorMessage = '';
  let order: any = null;

  const API_BASE = import.meta.env.VITE_API_URL 
    ? `${import.meta.env.VITE_API_URL}/api`
    : 'https://fletcraft-software.onrender.com/api';

  async function createOrder() {
    if (!service) return;

    try {
      isProcessing = true;
      errorMessage = '';

      const response = await fetch(`${API_BASE}/orders/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          service: service.id,
          customer_name: customerName,
          customer_email: customerEmail,
          customer_phone: customerPhone,
          amount: service.price,
          currency: 'ZAR'
        })
      });

      if (!response.ok) {
        throw new Error('Failed to create order');
      }

      order = await response.json();
      await processPayment();
    } catch (error) {
      errorMessage = error.message || 'An error occurred while creating the order';
    } finally {
      isProcessing = false;
    }
  }

  async function processPayment() {
    if (!order) return;

    try {
      isProcessing = true;
      errorMessage = '';

      const response = await fetch(`${API_BASE}/orders/create_payfast_payment/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          order_id: order.order_id
        })
      });

      if (!response.ok) {
        throw new Error('Failed to create payment');
      }

      const paymentData = await response.json();
      
      // Create and submit the PayFast form
      const form = document.createElement('form');
      form.method = 'POST';
      form.action = paymentData.payment_url;
      form.style.display = 'none';

      Object.entries(paymentData.payment_data).forEach(([key, value]) => {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = key;
        input.value = value as string;
        form.appendChild(input);
      });

      document.body.appendChild(form);
      form.submit();
    } catch (error) {
      errorMessage = error.message || 'An error occurred while processing payment';
    } finally {
      isProcessing = false;
    }
  }

  function handleSubmit(event: Event) {
    event.preventDefault();
    if (customerName && customerEmail && service) {
      createOrder();
    }
  }
</script>

<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4" 
     on:click={onClose} 
     transition:fade={{ duration: 200 }}>
  <div class="bg-white rounded-lg shadow-xl max-w-md w-full p-6" 
       on:click|stopPropagation 
       in:fly={{ y: 50, duration: 300, easing: quintOut }}>
    
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-bold text-gray-900">Checkout</h2>
      <button 
        on:click={onClose}
        class="text-gray-400 hover:text-gray-600 transition-colors">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>

    {#if service}
      <div class="bg-gray-50 rounded-lg p-4 mb-6">
        <h3 class="font-semibold text-lg text-gray-900 mb-2">{service.title}</h3>
        <p class="text-gray-600 text-sm mb-3">{service.description}</p>
        <div class="text-2xl font-bold text-green-600">R {service.price}</div>
      </div>
    {/if}

    <form on:submit={handleSubmit} class="space-y-4">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700 mb-1">
          Full Name *
        </label>
        <input
          id="name"
          type="text"
          bind:value={customerName}
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="Enter your full name"
        />
      </div>

      <div>
        <label for="email" class="block text-sm font-medium text-gray-700 mb-1">
          Email Address *
        </label>
        <input
          id="email"
          type="email"
          bind:value={customerEmail}
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="Enter your email address"
        />
      </div>

      <div>
        <label for="phone" class="block text-sm font-medium text-gray-700 mb-1">
          Phone Number
        </label>
        <input
          id="phone"
          type="tel"
          bind:value={customerPhone}
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          placeholder="Enter your phone number"
        />
      </div>

      {#if errorMessage}
        <div class="bg-red-50 border border-red-200 rounded-md p-3">
          <p class="text-red-600 text-sm">{errorMessage}</p>
        </div>
      {/if}

      <div class="flex space-x-3 pt-4">
        <button
          type="button"
          on:click={onClose}
          class="flex-1 px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 transition-colors"
          disabled={isProcessing}>
          Cancel
        </button>
        <button
          type="submit"
          class="flex-1 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          disabled={isProcessing || !customerName || !customerEmail}>
          {#if isProcessing}
            <div class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Processing...
            </div>
          {:else}
            Pay with PayFast
          {/if}
        </button>
      </div>
    </form>

    <div class="mt-6 text-center">
      <p class="text-xs text-gray-500">
        You will be redirected to PayFast to complete your payment securely.
      </p>
    </div>
  </div>
</div> 