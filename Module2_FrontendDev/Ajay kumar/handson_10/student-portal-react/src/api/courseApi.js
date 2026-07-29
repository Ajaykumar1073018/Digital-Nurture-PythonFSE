import apiClient from './apiClient';

export const courseApi = {
  async getAllCourses() {
    return await apiClient.get('/courses');
  },

  async getCourseById(id) {
    return await apiClient.get(`/courses/${id}`);
  },

  async enrollStudent(studentId, courseId) {
    return await apiClient.post('/enrollments', { studentId, courseId });
  }
};