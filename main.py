import pprint
from collections import defaultdict
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <path to file>')
        sys.exit(1)
        
    textFile = sys.argv[1]
    f = open(textFile)
    s = f.read()
    wordList = s.split()
    position = 0
    topN = 100
    myDict = defaultdict(int)
    while position < len(wordList)-2:
        myDict[(wordList[position],wordList[position+1],wordList[position+2])] += 1
        position +=1
    for w in sorted(myDict, key=myDict.get, reverse=True)[:topN]:
        print(w, myDict[w])
        # continue
    
if __name__ == "__main__":
    main()