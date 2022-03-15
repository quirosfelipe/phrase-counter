#!/usr/bin/env python3

from collections import defaultdict
import sys
import fileinput
import re
import string

def createWordList(input):
    wordList = []
    for line in input:
        # print(line)
        lineList = line.lower().split()
        stripLineList = []
        for word in lineList:
            word = word.strip(string.punctuation)
            if word != '': # string is empty when a word does not contain any chars or vowels ex:'...'
                stripLineList.append(word)
        wordList.extend(stripLineList)
    return wordList


def countWords(wordList, topN = 100):
    position = 0
    wordCount = defaultdict(int)
    myDict = defaultdict(int)
    while position < len(wordList) - 2:
        word_one = wordList[position].lower()
        word_two = wordList[position + 1].lower()
        word_three = wordList[position + 2].lower()
        myDict[
            (word_one, word_two, word_three)
        ] += 1
        position += 1
    for phrase in sorted(myDict, key=myDict.get, reverse=True)[:topN]:
        wordCount[phrase] = myDict[phrase]
        #print(w, myDict[w]) 
    return wordCount


def start():
    print(sys.argv)
    wordList = createWordList(fileinput.input())
    print(countWords(wordList))
    

if __name__ == "__main__":
    start()