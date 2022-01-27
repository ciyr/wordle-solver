# Wordle Solver
 This is basically a way to bruteforce your [wordle](https://www.powerlanguage.co.uk/wordle/) guesses.  
 The way this program works is by taking input from the user about the characters they have guessed till now and based on the characters in the word and those not in the word this 
 generates a list of possible 5 letter words that satisfy the given characters.   
 
 
## How To Use 
- After 2-3 guesses once you know a few of the letters in the word, enter those letters when prompted
- After this enter the lettes that are definitely not in the word (ones that are not yellow or green)
- For the positions type '.' in place of the characters you so not know so for example if you know 'e' is the 3rd letter, 'r' is 5th and nothing else, input "..e.r"
- After the first list of words is printed, simply enter the extra letters that are in / not in based on your next guess. No need to re-enter all the old ones
 

## Notes
 - List of words taken from [here](https://github.com/dwyl/english-words)  
 - P.S. Use this only when you are down to one guess and out of ideas. Otherwise it takes away the fun of the game ;)
