text = input("Text: ")
words = {}
for word in text.split(" "):
    words[word] = words.get(word, 0) + 1

for word in words:
    print(word, words[word])
