from random import randint

infile = open("word_list.txt", "r")
raw = infile.readlines()
infile.close()

words = []
for i in raw:
    words.append(i.strip().lower())
words.sort()

pure_prefixes = set()
for i in words:
    for j in range(len(i)+1):
        pure_prefixes.add(i[:j])
prefixes = pure_prefixes.copy()
for i in words:
    prefixes.remove(i)
#prefixes.remove("")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

tbd = list(prefixes)
for i in range(len(tbd)):
    tbd[i] = (len(tbd[i]), tbd[i])
tbd.sort(reverse = True)
winning_for_current_player = dict()
while(len(tbd) > 0):
    winning = False
    new = tbd[0][1]
    tbd.pop(0)
    for i in alphabet:
        x = new + i
        if (x in prefixes and not winning_for_current_player[x]):
            winning = True
    winning_for_current_player[new] = winning
    
def play():
    print("Welcome to the alphabet game!")
    cum = ""
    options = []
    for i in alphabet:
        x = cum + i
        if (x in prefixes and not winning_for_current_player[x]):
            options.append(i)
    if len(options) > 0:
        play = options[randint(0,len(options)-1)]
    else:
        play = "a"
        while (play == "a" or play == "i"):
            play = alphabet[randint(0,25)]
    print("I start with the letter", play)
    cum += play
    while True:
        inp = input("Please enter a letter: ").strip().lower()
        while(len(inp) != 1):
            print("Invalid input")
            inp = input("Please enter a letter: ").strip().lower()
        cum += inp
        if(not cum in prefixes):
            if(cum in words):
                print(cum, "is a word. You lose.")
                return
            else:
                print(cum, "does not work towards spelling any word. You lose.")
                return
        else:
            if(winning_for_current_player[cum]):
                options = []
                for i in alphabet:
                    x = cum + i
                    if(x in prefixes and not winning_for_current_player[x]):
                        options.append(i)
                play = options[randint(0,len(options)-1)]
                print("I respond with the letter", play)
                cum += play
            else:
                options = []
                for i in alphabet:
                    x = cum + i
                    if (x in pure_prefixes and x not in words):
                        options.append(i)
                if(len(options) > 0):
                    play = options[randint(0,len(options)-1)]
                    print("I respond with the letter", play)
                    cum += play
                else:
                    for i in alphabet:
                        x = cum + i
                        if (x in words):
                            options.append(i)
                    play = options[randint(0, len(options)-1)]
                    print("I respond with the letter", play)
                    cum += play
                    print(cum, "is a word.")
                    print("Well played.\n")
                    return
                        
                
play()
