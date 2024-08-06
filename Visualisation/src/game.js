// remember to bundle the game.js to bundle.js as browser does not support require function used in Node.js
//browserify src/game.js -o public/bundle.js

// Import required libraries
const Phaser = require('phaser');
const io = require('socket.io-client');
const EasyStar = require('easystarjs');

console.log('Script loaded');

// Phaser game configuration
var config = {
    type: Phaser.AUTO,
    width: 1400,
    height: 800,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

// Socket.io client setup
const socket = io('http://localhost:4000');

socket.on('connect', () => {
    console.log('Connected to the server');
    socket.emit('testConnection', 'Hello, server!', (response) => {
        console.log('Server acknowledged with:', response);
    });
});

socket.on('disconnect', () => {
    console.log('Disconnected from the server');
});

socket.on('updateLocation', (location) => {
    console.log('Updated location received:', location);
});


function emitAgentLocation() {
    if (agent) {
        var agentLocation = { x: agent.x, y: agent.y };
        console.log('Emitting location:', agentLocation);
        socket.emit('agentLocation', agentLocation);
    } else {
        console.warn('Agent is not defined yet.');
    }
}

function preload() {
    console.log('Loading assets...');
    this.load.image('grass', 'assets/grass.png');
    this.load.image('house1', 'assets/house1.png');
    this.load.image('school', 'assets/school.png');
    this.load.spritesheet('dude', 'assets/person.png', { frameWidth: 300, frameHeight: 400 });
}

// Define the `agent` variable and other variables
var agent, objects = [], cursors, target, path = [], pathIndex = 0, grid, pathGraphics, easystar, moveToTarget = false, lastPathCalculationTime = 0;
var pathCalculationInterval = 1000; // Recalculate path every 1000 ms

// Create the game scene
function create() {
    this.add.tileSprite(0, 0, config.width, config.height, 'grass').setOrigin(0, 0);
    grid = createGrid(28, 16);
    easystar = new EasyStar.js();
    easystar.setGrid(grid);
    easystar.setAcceptableTiles([0]);

    // Add houses
    addObject.call(this, 200, 300, 'house1', 'house1');
    addObject.call(this, 600, 400, 'house2', 'house1');
    addObject.call(this, 900, 600, 'house3', 'house1');
    
    // Add the school
    addObject.call(this, 800, 100, 'school1', 'school');

    // Initialize agent
    agent = this.physics.add.sprite(25, 25, 'dude');
    agent.setCollideWorldBounds(true);
    agent.setScale(0.25);
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });
    this.anims.create({
        key: 'turn',
        frames: [{ key: 'dude', frame: 4 }],
        frameRate: 20
    });
    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });

    // Collision detection
    objects.forEach(object => {
        this.physics.add.collider(agent, object.sprite, handleCollision, null, this);
    });

    cursors = this.input.keyboard.createCursorKeys();
    pathGraphics = this.add.graphics();
    drawGrid.call(this);

    // Keyboard input handling
    this.input.keyboard.on('keydown', (event) => {
        switch (event.key) {
            case '1': setTargetObject.call(this, 'house1'); break;
            case '2': setTargetObject.call(this, 'house2'); break;
            case '3': setTargetObject.call(this, 'house3'); break;
            case '5': setTargetObject.call(this, 'school1'); break;
            case '6': setTargetBottomRight.call(this); break;
        }
    });

    // Start emitting agent location after agent is defined
    setInterval(emitAgentLocation, 4000); // Emit every 4 seconds
}

// Game update loop
function update(time, delta) {
    if (moveToTarget && path && path.length > 0 && pathIndex < path.length) {
        var targetCell = path[pathIndex];
        var targetX = targetCell.x * 50 + 25;
        var targetY = targetCell.y * 50 + 25;
        if (Phaser.Math.Distance.Between(agent.x, agent.y, targetX, targetY) < 10) {
            pathIndex++;
        } else {
            this.physics.moveTo(agent, targetX, targetY, 160);
        }
    } else {
        agent.setVelocity(0);
        agent.anims.play('turn');
    }
    if (moveToTarget && time > lastPathCalculationTime + pathCalculationInterval) {
        calculatePath.call(this);
        lastPathCalculationTime = time;
    }
}

// Additional helper functions...

function addObject(x, y, id, image) {
    var object = { id: id, sprite: this.physics.add.image(x, y, image).setImmovable(true).setScale(0.5) };
    objects.push(object);
    var objX = Math.floor(x / 50);
    var objY = Math.floor(y / 50);
    grid[objY][objX] = 1;
}

function createGrid(cols, rows) {
    var grid = [];
    for (var y = 0; y < rows; y++) {
        var row = [];
        for (var x = 0; x < cols; x++) {
            row.push(0);
        }
        grid.push(row);
    }
    return grid;
}

function setTargetObject(objectId) {
    var object = objects.find(obj => obj.id === objectId);
    if (object) {
        var objX = Math.floor(object.sprite.x / 50);
        var objY = Math.floor(object.sprite.y / 50);
        target = new Phaser.Math.Vector2(objX * 50 + 25, (objY + 1) * 50 + 25);
        moveToTarget = true;
        calculatePath.call(this);
    }
}

function setTargetBottomRight() {
    target = new Phaser.Math.Vector2(config.width - 25, config.height - 25);
    moveToTarget = true;
    calculatePath.call(this);
}

function calculatePath() {
    grid = createGrid(28, 16);
    objects.forEach(object => {
        var objX = Math.floor(object.sprite.x / 50);
        var objY = Math.floor(object.sprite.y / 50);
        grid[objY][objX] = 1;
    });
    drawGrid.call(this);
    easystar.setGrid(grid);
    var start = { x: Math.floor(agent.x / 50), y: Math.floor(agent.y / 50) };
    var end = { x: Math.floor(target.x / 50), y: Math.floor(target.y / 50) };
    easystar.findPath(start.x, start.y, end.x, end.y, function (newPath) {
        if (newPath === null) {
            console.log("Path was not found.");
        } else {
            path = newPath.map(point => ({ x: point.x, y: point.y }));
            pathIndex = 0;
            console.log('Path:', path);
        }
    }.bind(this));
    easystar.calculate();
}

function drawGrid() {
    for (var y = 0; y < grid.length; y++) {
        for (var x = 0; x < grid[y].length; x++) {
            var color = grid[y][x] === 1 ? 0xff0000 : 0x00ff00;
            this.add.rectangle(x * 50 + 25, y * 50 + 25, 50, 50).setStrokeStyle(2, color).setOrigin(0.5);
        }
    }
}

function handleCollision(agent, object) {
    calculatePath.call(this);
}



//how many grids the agent can walk for within certain timeframe 15 mins maybe
//how to enter a house or  a bar
//given the location the agent can walk into the house by itself