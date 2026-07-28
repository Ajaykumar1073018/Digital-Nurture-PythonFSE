<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'
import { getAllCourses } from '../api/courseApi'
import CourseCard from '../components/CourseCard.vue'

const store = useEnrollmentStore()
const router = useRouter()

const courses = ref([])
const searchTerm = ref('')
const isLoading = ref(true)

onMounted(async () => {
  try {
    courses.value = await getAllCourses()
  } finally {
    isLoading.value = false
  }
})

const filteredCourses = computed(() => {
  return courses.value.filter(course => 
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})

const handleEnroll = async (course) => {
  await store.fetchAndEnroll(course) // Uses the new async Pinia action
  router.push('/profile')
}
</script>

<template>
  <div>
    <h2>Available Courses</h2>
    <input v-model="searchTerm" placeholder="Search courses..." style="padding: 10px; width: 100%; margin-bottom: 20px;">
    
    <div v-if="isLoading">Loading courses from API...</div>
    
    <CourseCard v-else v-for="course in filteredCourses" :key="course.id" :name="course.name" :code="course.code" :credits="course.credits">
      <button @click="handleEnroll(course)" style="background-color: #27ae60; color: white; padding: 5px 10px; border: none; cursor: pointer;">
        Enroll
      </button>
    </CourseCard>
  </div>
</template>