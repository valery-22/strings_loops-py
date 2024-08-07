def colorChange(letter):
    if letter.lower() == "r":
        print("\033[31m", end="")
    elif letter.lower() == "b":
        print("\033[0;34m", end="")
    elif letter.lower() == "g":
        print("\033[32m", end="")
    elif letter.lower() == "p":
        print("\033[35m", end="")
    elif letter.lower() == "y":
        print("\033[33m", end="")
    else:
        print()
    
sentence = input("What sentence you want rainbow-ising? ")
for letter in sentence:
    colorChange(letter.lower())
    print(letter,end="")
    print()
    
