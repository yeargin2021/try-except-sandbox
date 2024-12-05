import string

text = open('text',"r")

translator = str.maketrans("","", string.punctuation)

wordlist = sorted(set(word.translate(translator).lower() for word in text.read().split()))

text.close()

print(wordlist)