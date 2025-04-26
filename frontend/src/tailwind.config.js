// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        primary: '#10b981',     // verde esmeralda
        accent: '#60a5fa',      // azul suave
        dark: {
          DEFAULT: '#1f2937',   // gris 800
          light: '#374151',     // gris 700
          bg: '#0f172a',        // gris 900
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
};
