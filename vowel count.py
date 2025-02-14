#!/usr/bin/python3
def get_count(sentence):
    aeiou = "aeiou"
    counter = 0
    for i in sentence:
        if i in aeiou: 
            counter += 1
    return counter
