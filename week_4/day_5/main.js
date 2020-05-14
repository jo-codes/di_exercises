const calc = document.querySelector(".calc");
const keys = calc.querySelector(".keys");
const display = document.querySelector(".disp");

keys.addEventListener("click", (e) => {
  if (e.target.matches("button")) {
    const key = e.target;
    const action = key.dataset.action;
    const keyContent = key.textContent;
    let displayedNum = display.textContent;
    const previousKeyType = calc.dataset.previousKeyType;

    if (!action) {
      console.log("num");
      if (displayedNum === "0" || previousKeyType === "operator") {
        display.textContent = keyContent;
        calc.dataset.previousKeyType = "wombo";
      } else {
        display.textContent = displayedNum + keyContent;
      }
    }
    if (
      action === "add" ||
      action === "subtract" ||
      action === "multiply" ||
      action === "divide"
    ) {
      console.log("Op key");
      calc.dataset.previousKeyType = "operator";
      calc.dataset.firstValue = displayedNum;
      calc.dataset.operator = action;
    }
    if (action === "decimal") {
      console.log("deci");
      display.textContent = displayedNum + ".";
    }
    if (action === "reset") {
      console.log("reset");
      displayedNum = "0";
    }
    if (action === "clear") {
      console.log("clear");
      displayedNum = "0";
    }
    if (action === "calculate") {
      console.log("equal key");
      const firstValue = calc.dataset.firstValue;
      const operator = calc.dataset.operator;
      const secondValue = displayedNum;

      display.textContent = calculate(firstValue, operator, secondValue);
    }
  }
});

const calculate = (n1, operator, n2) => {
  let result = "";

  if (operator === "add") {
    result = parseFloat(n1) + parseFloat(n2);
  } else if (operator === "subtract") {
    result = parseFloat(n1) - parseFloat(n2);
  } else if (operator === "multiply") {
    result = parseFloat(n1) * parseFloat(n2);
  } else if (operator === "divide") {
    result = parseFloat(n1) / parseFloat(n2);
  }

  return result;
};
