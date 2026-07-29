import axios from 'axios';

// Create a single Axios instance with configuration
const apiClient = axios.create({
  baseURL: 'https://api.example.com/v1', // Switch dev vs prod baseURL here
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request Interceptor: Attach mock authorization token
apiClient.interceptors.request.use(
  (config) => {
    const mockToken = 'Bearer mock-jwt-token-12345';
    config.headers.Authorization = mockToken;
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor: Unwrap data or standardise error objects
apiClient.interceptors.response.use(
  (response) => response.data, // Callers receive data directly, not wrapper
  (error) => {
    const standardisedError = {
      message: error.response?.data?.message || error.message || 'An unexpected error occurred',
      statusCode: error.response?.status || 500
    };
    return Promise.reject(standardisedError);
  }
);

export default apiClient;