// Paint Project

var globalColor = '';

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
    let current = c[x];
    current.setAttribute(`onclick`, func);
  }
};

let fetchRGB = (e) => {
  globalColor = e.style.backgroundColor;
};

// generates colors and calls addOnclicks to add fetchRGB function to all new colored tiles

const generateColors = (target) => {
  let c = document.getElementById(target).childNodes;
  for (x = 0; x < c.length; x++) {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    let color = `rgb(${r},${g},${b})`;
    let currentNode = c[x];
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

addOnclicks('drawingGrid', 'displayColor(this)');

document.getElementById('clear').onclick = function () {
  let c = document.getElementById('drawingGrid').childNodes;
  for (x = 0; x < c.length; x++) {
    let currentNode = c[x];
    currentNode.style.backgroundColor = 'rgb(255,255,255)';
  }
};

let displayColor = (e) => {
  e.style.backgroundColor = globalColor;
};
