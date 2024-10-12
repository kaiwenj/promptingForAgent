// remember to bundle the game.js to bundle.js as browser does not support require function used in Node.js
// browserify src/game.js -o public/bundle.js
// 'assets/the_ville/visuals/the_ville collision.png'

//sth wrong with the agent?
//make sure to paint the path black
//map certain locations coordinates to name of loactions
//2 mappings

const Phaser = require('phaser');
const EasyStar = require('easystarjs');

// Phaser game configuration
var config = {
    type: Phaser.AUTO,
    width: 1080,
    height: 770,
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
const TILE_SIZE = 1;
let agents = [];
let easystar;
let grid = [];
let cursors;

function preload() {
    this.load.image('collisionMap', 'assets/the_ville/visuals/resized_collision_map.png');
    this.load.image('Abigail_Chen', 'assets/characters/profile/Abigail_Chen.png');
    this.load.image('Adam_Smith', 'assets/characters/profile/Adam_Smith.png');
}

function create() {
    easystar = new EasyStar.js();
    easystar.setAcceptableTiles([0]);

    createCollisionFromImageData(this, 'collisionMap', TILE_SIZE);
    this.add.image(0, 0, 'collisionMap').setOrigin(0, 0);

    agents.push(createAgent.call(this, 'Abigail_Chen'));
    agents.push(createAgent.call(this, 'Adam_Smith'));

    cursors = this.input.keyboard.createCursorKeys();

    
    // const graphics = scene.add.graphics();
    // graphics.fillStyle(0x000000, 1);
    // for (let y = 0; y < width; y++){
        
    //     graphics.fillRect(0, y, 50, 50);
    // }
    // console.log('black')

    setInterval(() => {
        agents.forEach(agent => emitAgentLocation(agent));
    }, 4000);

    // Print the grid in the console
    printGrid();
}

function update() {
    if (cursors.left.isDown) {
        moveAgentManually(agents[0], -1, 0);
    } else if (cursors.right.isDown) {
        moveAgentManually(agents[0], 1, 0);
    } else if (cursors.up.isDown) {
        moveAgentManually(agents[0], 0, -1);
    } else if (cursors.down.isDown) {
        moveAgentManually(agents[0], 0, 1);
    }
}

function createCollisionFromImageData(scene, collisionMapKey, tileSize) {
    const collisionTexture = scene.textures.get(collisionMapKey).getSourceImage();
    const collisionCanvas = scene.textures.createCanvas('collisionCanvas', collisionTexture.width, collisionTexture.height);
    collisionCanvas.draw(0, 0, collisionTexture);

    const gridWidth = Math.floor(collisionTexture.width / tileSize);
    const gridHeight = Math.floor(collisionTexture.height / tileSize);
    grid = new Array(gridHeight).fill(0).map(() => new Array(gridWidth).fill(0));

    for (let y = 0; y < gridHeight; y++) {
        for (let x = 0; x < gridWidth; x++) {
            const pixel = collisionCanvas.getPixel(x * tileSize, y * tileSize);

            if (isPink(pixel, 230, 0, 196, 255, 100)) {
                markSurroundingTilesUnwalkable(grid, x, y, gridWidth, gridHeight);
            }
        }
    }

    easystar.setGrid(grid);
    visualizeUnwalkableTiles(scene, grid, tileSize);
}

function isPink(pixel, targetR, targetG, targetB, targetA, tolerance) {
    return (
        Math.abs(pixel.r - targetR) <= tolerance &&
        Math.abs(pixel.g - targetG) <= tolerance &&
        Math.abs(pixel.b - targetB) <= tolerance &&
        Math.abs(pixel.a - targetA) <= tolerance
    );
}

function markSurroundingTilesUnwalkable(grid, x, y, gridWidth, gridHeight) {
    for (let dy = -2; dy <= 2; dy++) {
        for (let dx = -2; dx <= 2; dx++) {
            const nx = x + dx;
            const ny = y + dy;

            if (nx >= 0 && nx < gridWidth && ny >= 0 && ny < gridHeight) {
                grid[ny][nx] = 1;
            }
        }
    }
}

function visualizeUnwalkableTiles(scene, grid, tileSize) {
   
    const graphics = scene.add.graphics();
    graphics.fillStyle(0x000000, 1);

    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {
            if (grid[y][x] === 1) {
                const rectX = x * tileSize;
                const rectY = y * tileSize;
                graphics.fillRect(rectX, rectY, tileSize, tileSize);
            }
        }
    }
}

function createAgent(spriteKey) {
    let gridX = Phaser.Math.Between(0, Math.floor(config.width / TILE_SIZE) - 1);
    let gridY = Phaser.Math.Between(0, Math.floor(config.height / TILE_SIZE) - 1);

    while (grid[gridY][gridX] === 1) {
        gridX = Phaser.Math.Between(0, Math.floor(config.width / TILE_SIZE) - 1);
        gridY = Phaser.Math.Between(0, Math.floor(config.height / TILE_SIZE) - 1);
    }

    const x = gridX * TILE_SIZE + TILE_SIZE / 2;
    const y = gridY * TILE_SIZE + TILE_SIZE / 2;

    const sprite = this.physics.add.sprite(x, y, spriteKey);
    sprite.setCollideWorldBounds(true);
    sprite.setScale(0.5);

    return { name: spriteKey, sprite: sprite, gridX, gridY };
}

function moveAgentManually(agent, deltaX, deltaY) {
    if (agent) {
        const newGridX = agent.gridX + deltaX;
        const newGridY = agent.gridY + deltaY;

        if (
            newGridX >= 0 && newGridX < grid[0].length && 
            newGridY >= 0 && newGridY < grid.length && 
            grid[newGridY][newGridX] === 0
        ) {
            agent.gridX = newGridX;
            agent.gridY = newGridY;
            
            const newX = newGridX * TILE_SIZE + TILE_SIZE / 2;
            const newY = newGridY * TILE_SIZE + TILE_SIZE / 2;
            agent.sprite.setPosition(newX, newY);
        } else {
            console.log("Cannot move to the unwalkable tile or out of bounds");
        }
    }
}

function emitAgentLocation(agent) {
    if (agent) {
        var agentLocation = {
            name: agent.name,
            x: agent.sprite.x,
            y: agent.sprite.y,
        };
        console.log('Agent location:', agentLocation);
    } else {
        console.warn('Agent is not defined yet.');
    }
}

// Function to print the grid in the console
function printGrid() {
    console.log("Grid:");
    grid.forEach((row, rowIndex) => {
        console.log(`Row ${rowIndex}:`, row.join(' '));
    });
}






// Commented out additional helper functions for pathfinding and collision handling
// function createGrid(collisionMap) {
//     return collisionMap; // Assuming the collisionMap is already in the correct format
// }

// function calculatePath() {
//     easystar.setGrid(grid);
//     var start = { x: Math.floor(agent.x / 50), y: Math.floor(agent.y / 50) };
//     var end = { x: Math.floor(target.x / 50), y: Math.floor(target.y / 50) };
//     easystar.findPath(start.x, start.y, end.x, end.y, function (newPath) {
//         if (newPath === null) {
//             console.log("Path was not found.");
//         } else {
//             path = newPath.map(point => ({ x: point.x, y: point.y }));
//             pathIndex = 0;
//             console.log('Path:', path);
//         }
//     }.bind(this));
//     easystar.calculate();
// }



// const io = require('socket.io-client');
// const EasyStar = require('easystarjs');
// // Socket.io client setup
// const socket = io('http://localhost:4000');

// socket.on('connect', () => {
//     console.log('Connected to the server');
//     socket.emit('testConnection', 'Hello, server!', (response) => {
//         console.log('Server acknowledged with:', response);
//     });
// });

// socket.on('disconnect', () => {
//     console.log('Disconnected from the server');
// });

// socket.on('updateLocation', (location) => {
//     console.log('Updated location received:', location);
// });

