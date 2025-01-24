#!/usr/bin/python3
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
letter = (input("how many letters you like in your password?\n"))
letter = int(letter)
number = (input("how many numbers you like in your password?\n"))
number = int(number)
symbol = (input("how many symbols you like in your password?\n"))
symbol = int(symbol)

password = ""
for a in range(letter):
	password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for b in range(number):
	password += random.choice("1234567890")
for c in range(symbol):
	password += random.choice("!@#$%^&*()_+")

password += random.choice(characters)
print("this is your password: ", password)