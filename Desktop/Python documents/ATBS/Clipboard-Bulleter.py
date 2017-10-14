#! /usr/bin/python3

#Bulleter.py - Adds bullets to list of items seperated by line

import pyperclip

text = pyperclip.paste()

# This part seperates the lines and adds asteriks

lines = text.split('\n')

for each in range(len(lines)):
    lines[each] = '* ' + lines[each]

text = '\n'.join(lines)

print("Your list is now bulleted")

pyperclip.copy (text)
