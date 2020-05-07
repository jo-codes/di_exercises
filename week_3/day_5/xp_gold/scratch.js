// Exercise 1

// Write a JavaScript conditional statement to sort three numbers.
// Display an alert box to show the result.

// Output : [4, 0, -1]

const sortArray = () => {
  let input = [];

  const num1 = prompt("1st num please");
  const num2 = prompt("2nd num please");
  const num3 = prompt("3rd num please");

  input.push(num1, num2, num3);
  let output = new Array(input.sort().reverse());
  alert(output);
};

// sortArray();

// UNCOMMENT above to test ^^

// Exercise 2

// Write a JavaScript conditional statement to find the sign of product of three numbers. Display an alert box with the specified sign.

const findSign = () => {
  let input = [];

  const num1 = prompt("1st num please");
  const num2 = prompt("2nd num please");
  const num3 = prompt("3rd num please");

  input.push(num1, num2, num3);

  var sum = 0;

  for (x in input) {
    sum += parseInt(input[x]);
  }

  if (sum < 0) {
    alert("the sign is - ie. the num is negative");
  } else {
    alert("the sing is + ie. the num is positive");
  }
};

// findSign();

// UNCOMMENT above to test ^^
