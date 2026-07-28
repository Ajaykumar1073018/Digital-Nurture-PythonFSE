<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <div>
    <h2>Course Details</h2>
    <p>You are viewing the details for Course ID: <strong>{{ route.params.id }}</strong></p>
  </div>
</template>