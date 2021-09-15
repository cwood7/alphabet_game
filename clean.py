infile = open("word_list.txt", "r")
raw = infile.readlines()
infile.close()
words = []
for i in raw:
    words.append(i.strip().lower())
words = list(set(words))
words.sort()

outfile = open("word_list.txt", "w")
for i in words:
    outfile.write(i + "\n")
outfile.close()
