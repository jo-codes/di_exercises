var array = ["Banana", "Apples", "Oranges", "Blueberries"];

array.splice(0, 1);

array.sort();

array.push("Kiwi");

array.shift();

array.reverse();

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(array2[1][1]);
