const funcChoice = () => {
  const choice = prompt(
    "to check if two numbers are less than 100 and see remainder, type 1, to see if they divide evenly, type 2. ----- 1/2?"
  );
  if (choice === "1") {
    checkIf100();
  } else if (choice === "2") {
    dividesEvenly();
  } else {
    console.log("the only options are 1 and two. please refresh and try again");
  }
};

const checkIf100 = () => {
  var firstNum = parseInt(prompt("first num"));
  var secondNum = parseInt(prompt("second num"));
  if (firstNum + secondNum < 100) {
    console.log("less than 100");
    console.log(`remainder of dividing: ${firstNum % secondNum}`);
  } else {
    console.log("100 or greater");
    console.log(`remainder of dividing: ${firstNum % secondNum}`);
  }
};

const dividesEvenly = () => {
  var firstNum = prompt("first num");
  var secondNum = prompt("second num");
  if ((firstNum % secondNum) % 2 === 0) {
    console.log("Evenly divisable!");
  } else {
    console.log("Not evenly divisable!");
  }
};

// checkIf100();
// dividesEvenly();
funcChoice();
