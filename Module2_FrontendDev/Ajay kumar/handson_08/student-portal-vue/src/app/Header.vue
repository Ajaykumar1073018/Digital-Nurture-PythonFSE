<script setup>
import { useEnrollment } from '../services/enrollment.service';

const { enrolledCount } = useEnrollment();
</script>

<template>
  <header style="width: 100%; padding: 20px 40px; background-color: #ffffff; border-bottom: 1px solid #ddd; box-sizing: border-box; display: flex; justify-content: space-between; align-items: center;">
    <h1 style="margin: 0; font-size: 24px; color: #333;">Student Portal</h1>
    <div style="font-weight: bold; font-size: 16px; color: #333;">
      Enrolled: {{ enrolledCount }}
    </div>
  </header>
</template>