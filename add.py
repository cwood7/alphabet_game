n = eval(input("How many words would you like to add? "))
w = []
for i in range(n):
    w.append(input("Word " + str(i+1) + ": ").strip().lower())
infile = open("word_list.txt", "r")
raw = infile.readlines()
infile.close()
words = []
for i in raw:
    words.append(i.strip().lower())

for i in w:
        words.append(i)

outfile = open("word_list.txt", "w")
for i in words:
    outfile.write(i + "\n")
outfile.close()
