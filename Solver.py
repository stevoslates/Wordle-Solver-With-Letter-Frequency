with open("possible_words.txt", "r") as f:
    possible = f.read().split("\n")

with open("allowed_words.txt", "r") as f:
    allowed = f.read().split("\n")


def black(words, letter):
    return [ word for word in words if letter not in word ]


def yellow(words, letter, index):
    return [word for word in words if letter in word and letter != word[index]]


def green(words, letter, index):
    return [word for word in words if word[index] == letter]


def guess(word, response, words, in_word):

    for index, (letter, char) in enumerate(zip(word, response)):
        #print(index, char, letter, len(words))
        if char == 'B' and letter not in in_word:
            words = black(words, letter)    #filter out all words with this letter
        elif char == 'Y':
            in_word.append(letter)
            words = yellow(words, letter, index)
        else:
            in_word.append(letter)
            words = green(words, letter, index)
    return words

def letter_frequency(words):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    freq = {el:0 for el in alpha}
    
    for i in words:
        for char in i:
            freq[char] += 1
    
    #We return the five most frequent letters from our filtered words each time
    freq = sorted(freq, key=freq.get, reverse=True)[:5]
    
    return freq


def suggested_words(words, freq):
    suggested_words = list()
    counts = list() #this list is a parallel array so we can see how many of the most common letters appear in the word.
    
    for i in words:
        count = 0
        for j in freq:
            if j in i:  #if letter in the word then add to its counter
                count += 1
        counts.append(count)

    #lets zip them together 
    zipped = zip(words,counts)
    zipped = list(zipped)

    #gives us the words thaqt contain the greatest amount of most frequent letters
    zipped.sort(key=lambda x:x[1],reverse=True)

    #we want to return 5 suggested words - if our list is less than that however we just return the list.
    if len(zipped) < 5:
        for i in range(len(zipped)):
            suggested_words.append(zipped[i][0])
    else:
        for i in range(5):  #can change this to see how many suggetsed you would like
            suggested_words.append(zipped[i][0])
           

    return suggested_words
    

in_word = list()    #to prevent double letters
solved = False

words = possible

while solved == False:
    curr_word = input('Input your 5 letter guess: ')
    curr_response = input('What was the response (G is green, Y is yellow, B is black): ')

    words = guess(curr_word, curr_response, words, in_word)
    freq = letter_frequency(words)
    suggested = suggested_words(words,freq)

    print("Possible words are: " + str(words))
    print()
    print("Suggested words are: " + str(suggested))


