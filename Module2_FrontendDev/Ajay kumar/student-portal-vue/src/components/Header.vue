<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<template>
  <header style="background-color: #2c3e50; color: white; padding: 20px; display: flex; justify-content: space-between;">
    <h2 style="margin: 0;">Student Portal (Vue)</h2>
    <nav style="display: flex; gap: 15px; align-items: center;">
      <span style="color: #f1c40f; font-weight: bold;">Enrolled: {{ store.enrolledCourses.length }}</span>
      <RouterLink to="/" style="color: white; text-decoration: none;">Home</RouterLink>
      <RouterLink to="/courses" style="color: white; text-decoration: none;">Courses</RouterLink>
      <RouterLink to="/profile" style="color: white; text-decoration: none;">Profile</RouterLink>
    </nav>
  </header>
</template>