<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <Header />
  <main style="padding: 20px; max-width: 800px; margin: 0 auto; font-family: Arial, sans-serif;">
    <RouterView />
  </main>
</template>