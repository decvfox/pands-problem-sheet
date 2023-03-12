# es.py
# Reads in a text file and outputs the number of e's it contains
# should take the filename from an argument on the command line
# Author: Declan Fox
# ref https://realpython.com/python-command-line-arguments/
# ref https://www.w3schools.com/python/ref_string_count.asp

import sys

arg = sys.argv # arg = ['es.py', 'es.txt']
FILENAME = arg[1]

def read_text():
    with open(FILENAME) as f:
        text = f.read()
        return text

# Main
text = read_text()
count = text.count('e')
print (count)