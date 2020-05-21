// Paint Project

// Thinking it out.

// Need to:

// 1) Create two grids. 3 x 7 and the other should be a function taking in params for rows / columns. You can repurpose this function as "clear" with onclick. The first grid should be below a static two buttons, "New Colors" and "Clear"

// 2) You need to have a variable that is altered on click of a colored div in the first grid. You must research how to pass a variable from the onclick (most likely when you assign the color you should assign a property -- you have to look into this) to the JS, ... onclick triggers a function, function reads color property, changes variable for entire second grid to color for on DragEvent

// 3) Generate new colors. I will use Math.random to generate colors. I will call this function again onclick

const colorPicker = document.getElementById('colorPicker');
const drawingGrid = document.getElementById('drawingGrid');

function makeRows(rows, cols, location) {
  location.style.setProperty('--grid-rows', rows);
  location.style.setProperty('--grid-cols', cols);
  for (c = 0; c < rows * cols; c++) {
    let cell = document.createElement('div');
    location.appendChild(cell).className = `grid-item`;
  }
}

makeRows(7, 3, colorPicker);
makeRows(21, 29, drawingGrid);

const generateColors = (target) => {
  let c = document.getElementById(target).childNodes;
  for (x = 1; x < c.length; x++) {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    var color = `rgb(${r},${g},${b})`;
    var currentNode = c[x];
    currentNode.style.backgroundColor = color;
  }
};

generateColors('colorPicker');

document.getElementById('mix').onclick = function () {
  generateColors('colorPicker');
};

// i'm deleting the px argument. I'm going to specify in CSS for both individually. I want to set a minmax for each div... how to do these things?

// CURRENT, work out JS logic for generating a palette of colors. or rather work out functions individually and figure out how you will wire them together.

// ok, steps. start with a function, generateColors(colorpicker)... cant you manipulate this just like any other set of divs? once they're there?

// const generateColors = (target... what's target?
// target.forEachNode... needs work

// #colorpicker.children) => { var r, g, b = math.random(255) var color = `rgb(${},${},${})` ... this needs to be in loop } append style?. ok, got function. let's duck.

// YOU ARE HERE <><><><><><><><><>
// need to make function to add event listeners to every node. this will be used for both colors and for drawing. it will also be reapplied when you clear canvas or mix
// I'm going to first try to get an onclick that console logs it's own color.
// YOU ARE HERE <><><><><><><><><>

let displayColor = (node) => {
  console.log(node);
};

let addOnclicks = (target) => {
  let c = document.getElementById(target).childNodes;
  for (x = 0; x < c.length; x++) {
    var current = c[x];
    current.setAttribute(`onclick`, `fetchRGB(this)`);
  }
};

let fetchRGB = (e) => console.log(e.style.backgroundColor);

addOnclicks('colorPicker');

// you added onclicks, you have a display color function that you will later change to create an ondrag for the second grid (that part will be easy) what this really is is a problem of not understanding "this"

// small functions. one to loop through and add an onclick class? to each element after generation calling to a function in this file that simply prints color, that's it

// it's apparent you're blindly stabbing in the dark. I want to loop through onclicks adding an event listener. that listener calls a function. the function should set a variable to the clicked color and console.log it. the question is where should that variable be stored? wait... I have to add this function as an onclick to the color
