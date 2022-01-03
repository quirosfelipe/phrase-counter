from collections import defaultdict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path to file>")
        sys.exit(1)

    text_file = sys.argv[1]
    f = open(text_file)
    s = f.read()
    wordList = s.split()
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