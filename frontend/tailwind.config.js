/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: '#0a0a0a',
          light: '#ffffff'
        },
        primary: {
          DEFAULT: '#6366f1',
          dark: '#4f46e5'
        },
        secondary: {
          DEFAULT: '#8b5cf6',
          dark: '#7c3aed'
        },
        accent: {
          DEFAULT: '#ec4899',
          dark: '#db2777'
        },
        text: {
          primary: '#f8fafc',
          secondary: '#94a3b8',
          dark: '#0f172a'
        },
        // Apple Liquid Glass color palette
        glass: {
          'white-5': 'rgba(255, 255, 255, 0.05)',
          'white-10': 'rgba(255, 255, 255, 0.1)',
          'white-15': 'rgba(255, 255, 255, 0.15)',
          'white-20': 'rgba(255, 255, 255, 0.2)',
          'primary-5': 'rgba(99, 102, 241, 0.05)',
          'primary-10': 'rgba(99, 102, 241, 0.1)',
          'primary-15': 'rgba(99, 102, 241, 0.15)',
          'primary-20': 'rgba(99, 102, 241, 0.2)',
          'secondary-5': 'rgba(139, 92, 246, 0.05)',
          'secondary-10': 'rgba(139, 92, 246, 0.1)',
          'secondary-15': 'rgba(139, 92, 246, 0.15)',
          'secondary-20': 'rgba(139, 92, 246, 0.2)'
        }
      },
      fontFamily: {
        sans: ['Inter var', 'sans-serif'],
        display: ['Cal Sans', 'Inter var', 'sans-serif']
      },
      // Apple Liquid Glass backdrop filters
      backdropBlur: {
        'xs': '2px',
        'sm': '4px',
        'md': '8px',
        'lg': '16px',
        'xl': '24px',
        '2xl': '32px',
        '3xl': '48px',
        'liquid': '20px',
        'liquid-lg': '30px',
        'liquid-xl': '40px'
      },
      // Enhanced box shadows for glass morphism
      boxShadow: {
        'glass': '0 8px 32px rgba(139, 92, 246, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.08)',
        'glass-lg': '0 16px 48px rgba(139, 92, 246, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.1)',
        'glass-xl': '0 24px 64px rgba(139, 92, 246, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.12)',
        'liquid': '0 8px 32px rgba(99, 102, 241, 0.15), 0 4px 16px rgba(139, 92, 246, 0.1)',
        'liquid-hover': '0 12px 40px rgba(99, 102, 241, 0.2), 0 6px 20px rgba(139, 92, 246, 0.15)',
        'morphism': 'inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24)',
        'morphism-hover': 'inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 4px 12px rgba(99, 102, 241, 0.15), 0 2px 4px rgba(139, 92, 246, 0.1)'
      },
      animation: {
        'gradient-x': 'gradient-x 15s ease infinite',
        'gradient-y': 'gradient-y 15s ease infinite',
        'gradient-xy': 'gradient-xy 15s ease infinite',
        float: 'float 6s ease-in-out infinite',
        // Apple Liquid Glass animations
        'liquid-morph': 'liquid-morph 8s ease-in-out infinite',
        'liquid-pulse': 'liquid-pulse 4s ease-in-out infinite',
        'glass-shimmer': 'glass-shimmer 3s ease-in-out infinite',
        'liquid-float': 'liquid-float 6s ease-in-out infinite',
        'bubble-float': 'bubble-float 10s ease-in-out infinite'
      },
      keyframes: {
        'gradient-y': {
          '0%, 100%': {
            'background-size': '400% 400%',
            'background-position': 'center top'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'center center'
          }
        },
        'gradient-x': {
          '0%, 100%': {
            'background-size': '200% 200%',
            'background-position': 'left center'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right center'
          }
        },
        'gradient-xy': {
          '0%, 100%': {
            'background-size': '400% 400%',
            'background-position': 'left center'
          },
          '50%': {
            'background-size': '200% 200%',
            'background-position': 'right center'
          }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' }
        },
        // Apple Liquid Glass keyframes
        'liquid-morph': {
          '0%, 100%': {
            'border-radius': '60% 40% 30% 70%',
            'transform': 'rotate(0deg) scale(1)'
          },
          '25%': {
            'border-radius': '30% 60% 70% 40%',
            'transform': 'rotate(90deg) scale(1.05)'
          },
          '50%': {
            'border-radius': '50% 50% 50% 50%',
            'transform': 'rotate(180deg) scale(0.95)'
          },
          '75%': {
            'border-radius': '40% 70% 60% 30%',
            'transform': 'rotate(270deg) scale(1.02)'
          }
        },
        'liquid-pulse': {
          '0%, 100%': { 
            'backdrop-filter': 'blur(20px)',
            'opacity': '0.7',
            'transform': 'scale(1)'
          },
          '50%': { 
            'backdrop-filter': 'blur(30px)',
            'opacity': '0.9',
            'transform': 'scale(1.02)'
          }
        },
        'glass-shimmer': {
          '0%': { 'background-position': '-200% center' },
          '100%': { 'background-position': '200% center' }
        },
        'liquid-float': {
          '0%, 100%': { 
            'transform': 'translateY(0) rotate(0deg)',
            'backdrop-filter': 'blur(20px)'
          },
          '33%': { 
            'transform': 'translateY(-10px) rotate(2deg)',
            'backdrop-filter': 'blur(25px)'
          },
          '66%': { 
            'transform': 'translateY(-5px) rotate(-1deg)',
            'backdrop-filter': 'blur(22px)'
          }
        },
        'bubble-float': {
          '0%': { 
            'transform': 'translateY(100vh) scale(0)',
            'opacity': '0'
          },
          '10%': {
            'opacity': '0.6',
            'transform': 'translateY(90vh) scale(0.8)'
          },
          '90%': {
            'opacity': '0.3',
            'transform': 'translateY(10vh) scale(1.2)'
          },
          '100%': { 
            'transform': 'translateY(-10vh) scale(0)',
            'opacity': '0'
          }
        }
      }
    }
  },
  plugins: []
} 