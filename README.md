# overview
This program is for the generation of all possible english words using a given set of letters. It utilizes a already-created github file which contains a list of all words, as well as a file to handle any missed words (in my experience, I have not noticed any).

## Files
### figureWords.py
This the file that, when run, will allow for the user to enter in their desired letters. The program will then generate the possible english words that are spelled with only those letters. The operation may take substantial amounts of time for larger sets, due to the use of the permutations library.
### Extrawords
I recommend that if, upon use, it is realized that words are missing from the list of all english words, they are added to this file. Then, the figureWords program will be able to compare against those added as well.
