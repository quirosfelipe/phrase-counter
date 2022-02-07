#!/usr/bin/env python3

from collections import defaultdict
import sys
import fileinput


def main():
    print(sys.argv)
    wordList = []
    for line in fileinput.input():
        # print(line)
        lineList = line.split()
        wordList.extend(lineList)
    # if len(sys.argv) > 2:
    #     # work in multiple fileinput here
    #     # https://docs.python.org/3/library/fileinput.html
    #     # implemetation for multiple files is done above with the fileinput library
    #     print("Usage: python main.py <path to file>")
    #     sys.exit(1)
    # elif len(sys.argv) < 2:
    #     # this block allows stdin to pass the stream of bytes to the program.
    #     # In the next example main.py is the only argument.
    #     # Ex: echo hello world food | python main.py
    #     # Ex: cat origin.txt text.txt | python main.py
    #     f = sys.stdin
    # else:
    #     # The next block reads two arguments: main.py and origin.txt
    #     # Ex: python main.py origin.txt 
    #     text_file = sys.argv[1]
    #     f = open(text_file)
    
    # s = f.read()
    # wordList = s.split()
    position = 0
    topN = 100
    myDict = defaultdict(int)
    while position < len(wordList) - 2:
        word_one = wordList[position].lower()
        word_two = wordList[position + 1].lower()
        word_three = wordList[position + 2].lower()
        myDict[
            (word_one, word_two, word_three)
        ] += 1
        position += 1
    for w in sorted(myDict, key=myDict.get, reverse=True)[:topN]:
        print(w, myDict[w])


if __name__ == "__main__":
    main()