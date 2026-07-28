import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com', // Using the free test API
  timeout: 5000,
});

// Request Interceptor: Attach a mock auth token
apiClient.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer mock-token-123';
  console.log(`API call started: ${config.url}`);
  return config;
});

// Response Interceptor: Return data directly or throw standard error
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const customError = new Error(error.response?.data?.message || 'API request failed');
    customError.statusCode = error.response?.status || 500;
    throw customError;
  }
);

export default apiClient;