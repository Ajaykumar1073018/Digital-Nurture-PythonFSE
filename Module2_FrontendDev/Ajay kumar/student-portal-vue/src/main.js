import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

// Advanced: Global Error Handler
app.config.errorHandler = (err, instance, info) => {
  console.error('Global Error Caught:', err);
  alert(`Something went wrong: ${err.message}. Please try again later.`);
};

app.use(createPinia())
app.use(router)

app.mount('#app')