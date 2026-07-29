import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(createPinia());
app.use(router);

// Global Error Handler for Vue
app.config.errorHandler = (err, instance, info) => {
  console.error('Global Error Captured:', err);
  console.error('Component Instance:', instance);
  console.error('Error Info:', info);
  
  // Custom fallback notification logic can be triggered here
};

app.mount('#app');