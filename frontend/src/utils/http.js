import axios from 'axios';

// https://github.com/chrisvfritz/vue-enterprise-boilerplate/issues/25#issuecomment-378577141
// Add custom configuration here.
const axiosInstance = axios.create({});

export default axiosInstance;