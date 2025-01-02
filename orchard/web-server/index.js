const express = require('express');
const app = express();
const port = 3000;

// Serve static files (like HTML, CSS, JS) from the "public" folder
app.use(express.static('public'));

// Define a route to serve a dynamic page
app.get('/', (req, res) => {
    res.send('<h1>Welcome to My Web App</h1><p>This is served by Node.js!</p>');
});

// Serve static files from the "public" folder
app.use(express.static('public'));

// Define routes
app.get('/Sign_up', (req, res) => {
    res.sendFile(__dirname + '/public/Sign_up.html');
});

app.get('/login', (req, res) => {
    res.sendFile(__dirname + '/public/login.html');
});

app.get('/bsignin', (req, res) => {
    res.sendFile(__dirname + '/public/bsignin.html');
});
// Define routes for different trades
//Continue This part later 

// Start the server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
