// Daily Challenge : Letter Count

//     Ask the user for several words and save them. Check if the words given are strings
//     Determine which word has the greatest number of repeated letters and console.log this word.

const wordChecker = (word) => {
  let alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  let letters = word.split("");
  let totalDuplicates = 0;

  for (x in alphabet) {
    for (y in letters) {
      if (alphabet[x] === letters[y]) {
        if (letters.filter((n) => n == alphabet[x]).length > 1) {
          totalDuplicates++;
        }
      }
    }
  }
  return totalDuplicates;
};

let wordsToCheck = [];

const promptUserForWords = (numOfWords) => {
  for (x = 1; x < numOfWords + 1; x++) {
    wordsToCheck.push(prompt(`Gimme word ${x} of ${numOfWords}`));
  }
};

let highestCount = 0;
let higestWord = ["placeholder"];

wordsToCheck = ["time", "too", "gooooo"];

for (x in wordsToCheck) {
  let currentWordCount = wordChecker(wordsToCheck[x]);
  if (currentWordCount > highestCount) {
    console.log(currentWordCount);

    highestCount = currentWordCount;
    highestWord = wordsToCheck[x];
    console.log(highestWord);
  }
}

// promptUserForWords(3);
