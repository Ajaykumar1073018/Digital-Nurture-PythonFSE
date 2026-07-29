import { ref } from 'vue';

const enrolledCount = ref(0);

export function useEnrollment() {
  const enrollCourse = () => {
    enrolledCount.value++;
  };

  const dropCourse = () => {
    if (enrolledCount.value > 0) {
      enrolledCount.value--;
    }
  };

  return {
    enrolledCount,
    enrollCourse,
    dropCourse
  };
}