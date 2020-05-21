// Paint Project

const colorPicker = document.getElementById('colorPicker');
const drawingGrid = document.getElementById('drawingGrid');

// make row function to pass CSS variables for CSS grid

function makeRows(rows, cols, location) {
  location.style.setProperty('--grid-rows', rows);
  location.style.setProperty('--grid-cols', cols);
  for (c = 0; c < rows * cols; c++) {
    let cell = document.createElement('div');
    location.appendChild(cell).className = `grid-item`;
  }
}

// calling function initally

makeRows(7, 3, colorPicker);
makeRows(21, 29, drawingGrid);

// this function takes in a target, and a function to add on click

let addOnclicks = (target, func) => {
  let c = document.getElementById(target).childNodes;
  for (x = 0; x < c.length; x++) {
    var current = c[x];
    current.setAttribute(`onclick`, func);
  }
};

// this function currently just console logs, but will set global variable soon

let fetchRGB = (e) => console.log(e.style.backgroundColor);

// this is where the problem lies, passing fetchRGB...

const generateColors = (target) => {
  let c = document.getElementById(target).childNodes;
  for (x = 0; x < c.length; x++) {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    var color = `rgb(${r},${g},${b})`;
    var currentNode = c[x];
    currentNode.style.backgroundColor = color;
  }
  addOnclicks(target, `fetchRGB(this)`);
};

// inital call of generate colors

generateColors('colorPicker');

// fire mix color button

document.getElementById('mix').onclick = function () {
  generateColors('colorPicker');
};

// temp func, not sure where to go with this

let displayColor = (node) => {
  console.log(node);
};
