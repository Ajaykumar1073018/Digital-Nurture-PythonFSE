<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<template>
  <article style="border: 1px solid #ccc; padding: 15px; margin: 10px 0; border-radius: 5px;">
    <h3 style="color: #2980b9; margin: 0 0 10px 0;">{{ name }}</h3>
    <p>Code: <strong>{{ code }}</strong> | Credits: {{ credits }}</p>
    <slot></slot> <!-- Allows buttons to be injected from the parent -->
  </article>
</template>