<script setup>
import Header from './app/Header.vue';
import CourseCard from './components/CourseCard.vue';
</script>

<template>
  <div style="min-height: 100vh; background-color: #1a1a1a; margin: -8px; padding-bottom: 40px;">
    <Header />
    <main style="padding: 40px;">
      <h2 style="color: #fff; margin-bottom: 20px;">Available Courses</h2>
      <div style="display: flex; gap: 20px;">
        <CourseCard name="Machine Learning" code="CS101" :credits="3" />
        <CourseCard name="Web Development" code="CS102" :credits="4" />
      </div>
    </main>
  </div>
</template>