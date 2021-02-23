#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

myList = []

myList.insert(0, str(input("Enter a word: "))).strip()
myList.insert(1, str(input("Enter a word: "))).strip()
myList.insert(2, str(input("Enter a word: "))).strip()
myList.insert(3, str(input("Enter a word: "))).strip()
myList.insert(4, str(input("Enter a word: "))).strip()

print(myList)