import apiClient from './apiClient';

export const getAllCourses = async () => {
  // Fetching mock posts and mapping them to look like courses
  const posts = await apiClient.get('/posts?_limit=5');
  return posts.map(post => ({
    id: post.id,
    name: post.title.substring(0, 25), // Mock course name
    code: `CS${post.id}01`,
    credits: Math.floor(Math.random() * 2) + 3, // 3 or 4 credits
  }));
};

export const getCourseById = async (id) => {
  return await apiClient.get(`/posts/${id}`);
};

export const enrollStudent = async (studentId, courseId) => {
  // Simulating an enrollment API call
  return await apiClient.post('/posts', { studentId, courseId });
};