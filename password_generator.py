#!/usr/bin/python3
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
letter = int(input("how many letters you like in your password?\n"))
number = int(input("how many numbers you like in your password?\n"))
symbol = int(input("how many symbols you like in your password?\n"))

password = ""
for a in range(letter):
	password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for b in range(number):
	password += random.choice("1234567890")
for c in range(symbol):
	password += random.choice("!@#$%^&*()_+")

password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)
print("this is your password:", password)