<script setup>
import { useEnrollment } from '../services/enrollment.service';

defineProps({
  name: String,
  code: String,
  credits: Number
});

const { enrollCourse } = useEnrollment();
</script>

<template>
  <div style="border: 1px solid #ccc; padding: 20px; border-radius: 8px; width: 220px; background-color: #fff; color: #333;">
    <h3 style="margin-top: 0;">{{ name }}</h3>
    <p>Code: {{ code }}</p>
    <p>Credits: {{ credits }}</p>
    <button @click="enrollCourse" style="padding: 6px 12px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 4px;">Enroll</button>
  </div>
</template>