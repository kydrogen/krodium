const axios = require('axios');

const message = { message: 'Hello, server!' };

axios.post('http://127.0.0.1:8000/api/chat', message)
  .then(response => {
    console.log('Server response:', response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
