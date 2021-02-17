import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
# def moreBlah(s):
#     return s.split()

# blah = 'Hello this is the police. Make life easier and laugh really loud or or!'

# # print(moreBlah(words))
# # moreBlah(blah)
# splitWords = moreBlah(blah)

uniqueWords = {}
splitWords = words.replace("\n", " ").split()


for i in range(0, len(splitWords) - 1):
    if splitWords[i] in uniqueWords:
        uniqueWords[splitWords[i]].append(splitWords[i + 1])
    else:
        uniqueWords[splitWords[i]] = [splitWords[i + 1]]

wordKeys = uniqueWords.keys()

endWords = [word for word in wordKeys if len(word) > 0 and ((word[len(word) - 1] == '"' and (word[len(word) - 2] == "." or word[len(word) - 2] == "?" or word[len(word) - 2] == "!")) or (word[len(word) - 1] == '\'' and word[len(
    word) - 2] == '\"' and (word[len(word) - 3] == '.' or word[len(word) - 3] == "?" or word[len(word) - 3] == "!")) or word[len(word) - 1] == "." or word[len(word) - 1] == "?" or word[len(word) - 1] == "!")]

startWords = [word for word in wordKeys if len(word) > 0 and (word[0].isupper() or (word[0] == '"' and word[1].isupper())) and word not in endWords]

startWord = random.choice(startWords)


# TODO: construct 5 random sentences
# Your code here

key = startWord
stopped = False

for i in range(6):
    sentence = startWord
    while not stopped:
        nextWord = random.choice(uniqueWords[key])
        if nextWord not in startWords:
            sentence += " " + nextWord
        
        if nextWord in endWords:
            stopped = True
        key = nextWord
    stopped = False
    print(sentence)
    startWord = random.choice(startWords)



