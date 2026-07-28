<script setup>
import { useEnrollmentStore } from '../stores/enrollment'
import { storeToRefs } from 'pinia'

const store = useEnrollmentStore()
// Advanced: Extract reactive refs safely without breaking reactivity
const { enrolledCourses, totalCredits } = storeToRefs(store)
const { unenroll, $reset } = store 
</script>

<template>
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <h2>Your Profile & Enrollments</h2>
      <button @click="$reset()" style="background-color: #e67e22; color: white; border: none; padding: 8px 12px; cursor: pointer;">Reset Enrollments</button>
    </div>
    
    <p><strong>Total Enrolled Credits:</strong> {{ totalCredits }}</p>
    <div v-if="enrolledCourses.length === 0">No courses enrolled yet.</div>

    <div v-for="course in enrolledCourses" :key="course.id" style="border: 1px solid #3498db; padding: 10px; margin: 10px 0;">
      <strong>{{ course.name }}</strong> ({{ course.credits }} credits)
      <button @click="unenroll(course.id)" style="float: right; background-color: #e74c3c; color: white; border: none; padding: 5px 10px; cursor: pointer;">
        Remove
      </button>
    </div>
  </div>
</template>