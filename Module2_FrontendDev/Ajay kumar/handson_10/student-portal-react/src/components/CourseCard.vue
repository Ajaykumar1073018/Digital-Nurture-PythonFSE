<script setup>
import { storeToRefs } from 'pinia';
import { useEnrollmentStore } from '../stores/enrollment.store';

const props = defineProps({
  courseId: String,
  name: String,
  code: String,
  credits: Number
});

const store = useEnrollmentStore();
// storeToRefs extracts reactive refs safely without breaking reactivity
const { loading, error } = storeToRefs(store);

const handleEnroll = () => {
  store.fetchAndEnroll('student-123', props.courseId);
};
</script>

<template>
  <div class="course-card">
    <h3>{{ name }}</h3>
    <p>Code: {{ code }}</p>
    <p>Credits: {{ credits }}</p>
    <button @click="handleEnroll" :disabled="loading">
      {{ loading ? 'Enrolling...' : 'Enroll' }}
    </button>
    <p v-if="error" class="error-text">{{ error }}</p>
  </div>
</template>