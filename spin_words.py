#!/usr/bin/python3
def spin_words(sentence):
    result = []
    listy = sentence.split()

    for word in listy:
        if len(word)>= 5:
            word[i] = word[i][::-1]
        result.append(word)
    
    return ' '.join(result)
