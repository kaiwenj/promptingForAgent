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
    // this.load.image('arrow', 'assets/arrow.png');
    this.load.spritesheet('dude', 'assets/person.png', { frameWidth: 300, frameHeight: 400 });
//     this.load.image('cafe', 'assets/cafe.png');
//     this.load.image('school', 'assets/school.png');
 }

// Define the `agent` variable and other variables
var agent, houses = [], cursors, target, path = [], pathIndex = 0, grid, pathGraphics, easystar, moveToTarget = false, lastPathCalculationTime = 0;
var pathCalculationInterval = 1000; // Recalculate path every 1000 ms

// Create the game scene
function create() {
    this.add.tileSprite(0, 0, config.width, config.height, 'grass').setOrigin(0, 0);
    grid = createGrid(28, 16);
    easystar = new EasyStar.js();
    easystar.setGrid(grid);
    easystar.setAcceptableTiles([0]);
    addHouse.call(this, 200, 300, 'house1');
    addHouse.call(this, 600, 400, 'house2');
    addHouse.call(this, 900, 600, 'house3');
    // addCafe.call(this, 300, 200);
    // addSchool.call(this, 500, 500);

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
    houses.forEach(house => {
        this.physics.add.collider(agent, house.sprite, handleCollision, null, this);
    });

    cursors = this.input.keyboard.createCursorKeys();
    pathGraphics = this.add.graphics();
    drawGrid.call(this);

    // Keyboard input handling
    this.input.keyboard.on('keydown', (event) => {
        switch (event.key) {
            case '1': setTargetHouse.call(this, 'house1'); break;
            case '2': setTargetHouse.call(this, 'house2'); break;
            case '3': setTargetHouse.call(this, 'house3'); break;
            // case '4': setTargetHouse.call(this, 'cafe'); break;
            // case '5': setTargetHouse.call(this, 'school'); break;
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

function addHouse(x, y, id) {
    var house = { id: id, sprite: this.physics.add.image(x, y, 'house1').setImmovable(true).setScale(0.5) };
    houses.push(house);
    var houseX = Math.floor(x / 50);
    var houseY = Math.floor(y / 50);
    grid[houseY][houseX] = 1;
}

function addCafe(x, y) {
    var cafe = { id: 'cafe', sprite: this.physics.add.image(x, y, 'cafe').setImmovable(true).setScale(0.5) };
    houses.push(cafe);
    var cafeX = Math.floor(x / 50);
    var cafeY = Math.floor(y / 50);
    grid[cafeY][cafeX] = 1;
}

function addSchool(x, y) {
    var school = { id: 'school', sprite: this.physics.add.image(x, y, 'school').setImmovable(true).setScale(0.5) };
    houses.push(school);
    var schoolX = Math.floor(x / 50);
    var schoolY = Math.floor(y / 50);
    grid[schoolY][schoolX] = 1;
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

function setTargetHouse(houseId) {
    var house = houses.find(h => h.id === houseId);
    if (house) {
        var houseX = Math.floor(house.sprite.x / 50);
        var houseY = Math.floor(house.sprite.y / 50);
        target = new Phaser.Math.Vector2(houseX * 50 + 25, (houseY + 1) * 50 + 25);
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
    houses.forEach(house => {
        var houseX = Math.floor(house.sprite.x / 50);
        var houseY = Math.floor(house.sprite.y / 50);
        grid[houseY][houseX] = 1;
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

function handleCollision(agent, house) {
    calculatePath.call(this);
}


// function drawPath(path) {
//     pathGraphics.clear(); // Clear previous path
//     pathGraphics.lineStyle(2, 0x0000ff, 1); // Blue color for path lines

//     for (var i = 0; i < path.length - 1; i++) {
//         var fromX = path[i].x * 50 + 25;
//         var fromY = path[i].y * 50 + 25;
//         var toX = path[i + 1].x * 50 + 25;
//         var toY = path[i + 1].y * 50 + 25;

//         // Draw a line segment for each step in the path
//         pathGraphics.moveTo(fromX, fromY);
//         pathGraphics.lineTo(toX, toY);

//         // Optionally, add an arrow or some visual indicator
//         var angle = Phaser.Math.Angle.Between(fromX, fromY, toX, toY);
//         var arrow = this.add.image((fromX + toX) / 2, (fromY + toY) / 2, 'arrow').setRotation(angle).setScale(0.5);
//     }
//     pathGraphics.strokePath();
// }




//how many grids the agent can walk for within certain timeframe 15 mins maybe
//how to enter a house or  a bar
//given the location the agent can walk into the house by itself