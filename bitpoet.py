from random import randint
from time import sleep
from time import localtime

colossus = open("colossus.txt", "r")
lines = colossus.readlines()
nested_words = [line.split() for line in lines]
colossus.close()

# flat_list = [item for sublist in l for item in sublist]
flat_words = []
for word_list in nested_words:
    for word in word_list:
        flat_words.append(word)

flat_words = flat_words[1:-1]

poetree = {}
for word_index in range(len(flat_words) - 1):
    word = flat_words[word_index]

    if word_index == len(flat_words) - 1:
        poetree[word] = []
        break

    if word in poetree:
        poetree[word].append(flat_words[word_index + 1])
    else:
        poetree[word] = []

root_words = list(poetree.keys())[0:-2]
root_index = randint(0, len(root_words) - 1)
root = root_words[root_index]

poem = root.title()
poeming = True

while(poeming):
    if len(poem.split()) > 400:
        poeming = False

    if poetree[root]:
        next_root = poetree[root][randint(1, len(poetree[root])) - 1]
    else:
        next_root = poetree.keys()[randint(1, len(poetree.keys())) -1]

    if(next_root.isdigit()):
        poeming = False
    else:
        poem += " " + next_root
        root = next_root

print(poem)

#outfile = open("poem"+str(localtime().tm_year)+"-"+str(localtime().tm_mon)+"-"+str(localtime().tm_mday)+'-'+
#               str(localtime().tm_hour)+'-'+str(localtime().tm_min)+"-"+str(localtime().tm_sec)+".txt", "w+")
#outfile.writelines(poem)
#outfile.close()
