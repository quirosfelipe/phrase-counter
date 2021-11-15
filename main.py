import pprint

def main():
    f = open('text.txt')
    # pprint.pprint(f)
    s = f.read()
    pprint.pprint(s)
    print(type(s))
if __name__ == "__main__":
    main()