import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCount = ref(0);

  function increment() {
    enrolledCount.value++;
  }

  function $reset() {
    enrolledCount.value = 0;
  }

  return {
    enrolledCount,
    increment,
    $reset
  };
});