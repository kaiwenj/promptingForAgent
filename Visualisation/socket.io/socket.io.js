const express = require('express');
const path = require('path'); // so that I can preload the game assets as static files in the public directory

const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);

// Use the CORS middleware as browser doesnt support require function in node.js (from stackoverflow)
app.use(cors({
  origin: "http://127.0.0.1:8080",
  methods: ["GET", "POST"],
  allowedHeaders: ["Content-Type"],
  credentials: true
}));

// // Serve static files from the "public" directory
// app.use(express.static('public'));

let currentAgentLocation = { x: 0, y: 0 };

// Initialize socket.io with CORS configuration
const io = socketIo(server, {
  cors: {
    origin: "http://127.0.0.1:8080",
    methods: ["GET", "POST"],
    allowedHeaders: ["Content-Type"],
    credentials: true
  }
});

// app.use(express.static(path.join(__dirname, 'public')));

io.on('connection', (socket) => {
  console.log('New client connected');
  
  socket.on('agentLocation', (location) => {
    currentAgentLocation = location;
    console.log('Received agent location:', location);
    io.emit('updateLocation', currentAgentLocation); //broadcast the location
  });

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

app.get('/location', (req, res) => {
  res.json(currentAgentLocation); // Send the current location as JSON
});
// Serve socket.html at the root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'socket.html'));
});

const PORT = 4000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
