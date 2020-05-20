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
    console.log(color);
    currentNode.style.backgroundColor = color;
  }
};

generateColors('colorPicker');
// i'm deleting the px argument. I'm going to specify in CSS for both individually. I want to set a minmax for each div... how to do these things?

// CURRENT, work out JS logic for generating a palette of colors. or rather work out functions individually and figure out how you will wire them together.

// ok, steps. start with a function, generateColors(colorpicker)... cant you manipulate this just like any other set of divs? once they're there?

// const generateColors = (target... what's target?
// target.forEachNode... needs work

// #colorpicker.children) => { var r, g, b = math.random(255) var color = `rgb(${},${},${})` ... this needs to be in loop } append style?. ok, got function. let's duck.
