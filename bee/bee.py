# NYT spelling bee puzzle solver

import pprint

with open("word_list.txt") as wordlist_file:
    # ingest the word list as a set
    actual_words = set(word.strip().lower() for word in wordlist_file)

validLetters = set()

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
    pp = pprint.PrettyPrinter(width=60)
    pp.pprint(sortedWordList)
    print (", ".join(map(str, sortedWordList)))

print("NYT Spelling Bee Solver")

centerLetter = 'a'
validLetters =  set(['a', 'c', 'b', 'd', 'k', 'r', 'w'])

# centerLetter = input("center letter: ")
# validLetters.add(centerLetter)
# validLetters.add(input("other letters: "))

print("Your set of letters is: ", validLetters)

solve(actual_words, validLetters, centerLetter)
