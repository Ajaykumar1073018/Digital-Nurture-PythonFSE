// src/store/store.js
import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './enrollmentSlice';

export const store = configureStore({
    reducer: {
        enrollment: enrollmentReducer
    }
});