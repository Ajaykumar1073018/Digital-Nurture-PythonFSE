<script setup>
import { useEnrollmentStore } from './stores/enrollment.store.js';
import CourseCard from './components/CourseCard.vue';
</script>

<template>
  <div id="app">
    <header class="portal-header">
      <h1>Student Portal</h1>
      <nav>
        <a href="#home">Home</a>
        <a href="#courses">Courses</a>
      </nav>
    </header>

    <main class="portal-main">
      <section>
        <h2>Available Courses</h2>
        <div class="course-grid">
          <CourseCard courseId="101" name="Machine Learning" code="CS101" :credits="3" />
          <CourseCard courseId="102" name="Web Development" code="CS102" :credits="4" />
        </div>
      </section>
    </main>
  </div>
</template>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #1a1a1a;
  color: #ffffff;
}
.portal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: #ffffff;
  color: #333;
}
.portal-main {
  padding: 40px;
}
.course-grid {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}
</style>