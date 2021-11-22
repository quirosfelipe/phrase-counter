import pprint
from collections import defaultdict

def main():
    f = open('text.txt')
    # pprint.pprint(f)
    s = f.read()
    # pprint.pprint(s)
    # print(type(s))
    # wordList = s.split()
    # pprint.pprint(wordList)
    # print(type(wordList))
    wordList = s.split()
    position = 0
    myDict = defaultdict(int)
    while position < len(wordList)-2:
        myDict[(wordList[position],wordList[position+1],wordList[position+2])] += 1
        # print(wordList[position:position+3])
        position +=1
    pprint.pprint(myDict)
if __name__ == "__main__":
    main()