file = open('text.txt')
test = dict()
for line in file:
    x = line.split()
    for word in x: #for every word, you add it to the dictionary. if its not there then it adds it. if it is there it adds another value to it.
        test[word] = test.get(word, 0) + 1
maxWord = max(test, key=test.get)
print("Most common word:", maxWord + ":", test[maxWord])
