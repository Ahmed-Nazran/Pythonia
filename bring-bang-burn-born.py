from itertools import permutations, product
from pathlib import Path

def case_combinations(word):

    ver = [""]

    for char in word:
        new= []

        if char.isalpha():
            for x in ver:
                new.append(x + char.lower())
                new.append(x + char.upper())
        else:
            for x in ver:
                new.append(x + char)

        ver = new

    return ver


def main():
    n = int(input("Numbers of input: "))
  
    words = []
  
    for i in range(n):
        word = input("Input " + str(i + 1) + ": ")
        words.append(word)

    output_path = Path("wordlist.txt")
    file = output_path.open("w", encoding="utf-8")

    permus = permutations(words)

    for perm in permus:
      
        alls = []
      
        for word in perm:
            ver = case_combinations(word)
            alls.append(ver)

        for cases in product(*alls):
          
            cstring = ""
            for strn in cases:
                cstring += strn

            file.write(cstring + "\n")

    file.close()
    print("Done! Saved to wordlist.txt")

main()
