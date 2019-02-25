def leet(s):
    return s.replace("A","4").replace("E","3").replace("G","6").replace("I","1").replace("O","0").replace("S","5").replace("Z","2")

def main():
    s = input()
    print(leet(s))

if __name__ == "__main__":
    main()