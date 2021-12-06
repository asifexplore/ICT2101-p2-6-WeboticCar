let gameMap;
var speed = 3;
let x = 25,
    y = 75;

function setup() {
    createCanvas(510, 600).parent('canvasHolder');

    // Creates map grid
    gameMap = new GameMap(10, 10);
    console.log(gameMap);
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

function draw() {
    clear();
    background('white');

    gameMap.spawnMap(); // Render map

    // upDown();
    leftRight();

    drawCircle();
}

function drawCircle() {
    fill(256, 165, 0);
    ellipse(x, y, 40, 40);
}

function leftRight() {
    x = x + speed;

    if (x + 25 >= width || x - 25 <= 0) {
        speed = -speed;
    }
}

function upDown() {
    y = y + speed;

    if (y + 25 >= height || y - 25 <= 0) {
        speed = -speed;
    }
}

function movement() {
    if (keyCode === UP_ARROW) {
        y = y - 10;
    } else if (keyCode === DOWN_ARROW) {
        y = y + 10;
    }
    if (keyCode === LEFT_ARROW) {
        x = x - 5;
    } else if (keyCode === RIGHT_ARROW) {
        x = x + 5;
    }

}

class GameMap {
    constructor(rows, cols) {
        this.cols = cols;
        this.rows = rows;
        this.resolution = 50;
        this.grid;
        this.setObjects();
    }

    setObjects() {
        this.grid = this.create2DArray(this.cols, this.rows);

        for (let i = 0; i < this.cols; i++) {
            for (let j = 0; j < this.rows; j++) {
                this.grid[i][j] = floor(random(4));
            }
        }
    }

    create2DArray(cols, rows) {
        //Generate a 2D array to have the map spawn with objects
        let arr = new Array(cols);
        for (let i = 0; i < cols; i++) { //Creates a 2D array that is empty
            arr[i] = new Array(rows);
        }
        return arr;
    }

    spawnMap() {
        for (let i = 0; i < this.cols; i++) {
            for (let j = 0; j < this.rows; j++) {

                let x = i * this.resolution;
                let y = 50 + (j * this.resolution);
                fill('lightgray');
                stroke(0);
                rect(x, y, this.resolution, this.resolution);
            }
        }
    }
}