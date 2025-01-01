const express = require('express');
const app = express();
const port = 3000;

// Serve static files (like HTML, CSS, JS) from the "public" folder
app.use(express.static('public'));

// Define a route to serve a dynamic page
app.get('/', (req, res) => {
    res.send('<h1>Welcome to My Web App</h1><p>This is served by Node.js!</p>');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
