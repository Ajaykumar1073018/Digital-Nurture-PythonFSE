import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { enrollStudent } from '../api/courseApi'

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([])

  const totalCredits = computed(() => 
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  )

  // Advanced: Async action combining API call and state update
  async function fetchAndEnroll(course) {
    try {
      // Simulate API call to enroll
      await enrollStudent(1, course.id);
      if (!enrolledCourses.value.find(c => c.id === course.id)) {
        enrolledCourses.value.push(course)
      }
    } catch (error) {
      console.error("Enrollment failed", error);
      throw error; // Let the component handle the UI error
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId)
  }

  // Advanced: Reset state
  function $reset() {
    enrolledCourses.value = []
  }

  return { enrolledCourses, totalCredits, fetchAndEnroll, unenroll, $reset }
})