// Daily Challenge : Letter Count

//     Ask the user for several words and save them. Check if the words given are strings
//     Determine which word has the greatest number of repeated letters and console.log this word.

const checkRepeatLetters = (word) => {
  let lettersArr = word.split("");
  let alphabet = "abcdefghijklmnopqrstuvwxyz";
  alphabet = alphabet.split("");
  var dupCount = 0;
  for (x = 0; x < alphabet.length; x++) {
    for (y = 0; y < lettersArr.length; y++) {
      if (alphabet[x] == lettersArr[y]) {
        dupCount++;
      }
    }
  }
  dupCount = dupCount - word.length;
  console.log(dupCount);
};

const wordsToCheck = [];

const promptUserForWords = (numOfWords) => {
  for (x = 1; x < numOfWords + 1; x++) {
    wordsToCheck.push(prompt(`Gimme word ${x} of ${numOfWords}`));
  }
};
promptUserForWords(3);

for (x in wordsToCheck) {
  checkRepeatLetters(wordsToCheck[x]);
}

// var highest = 0;
// var highestWord = "";

// for (x in wordsToCheck) {
//   let result = checkRepeatLetters(wordsToCheck[x]);
//   if (result > highest) {
//     highest = result;
//     highestWord = wordsToCheck[x];
//   }
// }
