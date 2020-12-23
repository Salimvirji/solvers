 NYT spelling bee puzzle solver

import pprint
import sys

with open("word_list.txt") as wordlist_file:
    # ingest the word list as a set
    actual_words = set(word.strip().lower() for word in wordlist_file)

def solve(wordset, letterset, centerLetter):
    tempSet = set()
    outputSet = set()
    for word in wordset:
        tempset = set(word)
        # minimum word length is 4 characters
        if tempset - letterset == set() and len(word) >= 4:
            tempSet.add(word)
    for potentialWord in tempSet:
        tempset2 = set(potentialWord)
        # require the center letter in the output word
        if centerLetter in tempset2:
            outputSet.add(potentialWord)
    sortedWordList = list(outputSet)
    sortedWordList.sort()
    print ("\n".join(map(str, sortedWordList)))

print("NYT Spelling Bee Solver")

#centerLetter = 'a'
#validLetters =  set(['a', 'c', 'b', 'd', 'k', 'r', 'w'])

centerLetter = ''
validLetters = set()
letters = sys.argv[1:8]
print "Letters for today: ", letters
centerLetter = letters[0]
print "Center Letter is: ", centerLetter
validLetters.add(centerLetter)
for letter in range (1,7):
        #print "validLetters", validLetters
        #print "index: ", letter
        validLetters.add(letters[letter])

solve(actual_words, validLetters, centerLetter)
