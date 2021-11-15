import kaboom from "https://unpkg.com/kaboom/dist/kaboom.mjs";

// Input handling and basic player movement

// Start kaboom
kaboom()

// Load assets
loadSprite("car", "static/game/car.png")
loadSprite("bg", "static/game/city.png")

// Define player movement speed (pixels per second)
const SPEED = 320

add([
    sprite("bg"),
    scale(width() / 480, height() / 240),
    origin("topleft")
]);

// Add player game object
const player = add([
    sprite("car"),
    // center() returns the center point vec2(width() / 2, height() / 2)
    pos(center()),
])

// onKeyDown() registers an event that runs every frame as long as user is holding a certain key
onKeyDown("left", () => {
    // .move() is provided by pos() component, move by pixels per second
    player.move(-SPEED, 0)
})

onKeyDown("right", () => {
    player.move(SPEED, 0)
})

onKeyDown("up", () => {
    player.move(0, -SPEED)
})

onKeyDown("down", () => {
    player.move(0, SPEED)
})

// onClick() registers an event that runs once when left mouse is clicked
onClick(() => {
    // .moveTo() is provided by pos() component, changes the position
    player.moveTo(mousePos())
})

add([
    // text() component is similar to sprite() but renders text
    text("Click the car to start playing. \nPress arrow keys to move the car", { width: width() }),
    pos(300, 12),
])