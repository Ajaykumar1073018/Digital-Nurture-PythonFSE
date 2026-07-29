import { createSlice } from '@reduxjs/toolkit';

export const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState: {
    enrolledCourses: []
  },
  reducers: {
    enroll: (state, action) => {
      // Add the course to the array if it isn't already enrolled
      const courseExists = state.enrolledCourses.find(c => c.id === action.payload.id);
      if (!courseExists) {
        state.enrolledCourses.push(action.payload);
      }
    },
    unenroll: (state, action) => {
      // Remove the course from the array by its ID
      state.enrolledCourses = state.enrolledCourses.filter(c => c.id !== action.payload);
    }
  }
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;