#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

# Part 1 - Paste text from the clipboard
text = pyperclip.paste()

# Part 2 - Do something to it
# Separate lines and add stars
lines = text.split('\n')

for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)

# Part 3 - Copy the new text to the clipboard
pyperclip.copy(text)
