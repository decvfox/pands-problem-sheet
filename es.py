# es.py
# Reads in a text file and outputs the number of e's it contains
# should take the filename from an argument on the command line
# Author: Declan Fox
# ref https://realpython.com/python-command-line-arguments/
# ref https://www.w3schools.com/python/ref_string_count.asp

import sys

arg = sys.argv # arg = ['es.py', 'es.txt']
FILENAME = arg[1] # FILENAME = 'es.txt'

def read_text():
    '''Function to open and read text file'''
    with open(FILENAME) as f:
        text = f.read()
        return text

# Main
text = read_text() # Calls the read_text() function
count = text.count('e') + text.count('E') # uses the string count() function to count the es
print (count) # prints the number of es