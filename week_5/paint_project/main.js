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

// i'm deleting the px argument. I'm going to specify in CSS for both individually. I want to set a minmax for each div... how to do these things?

