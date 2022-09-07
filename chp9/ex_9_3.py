'''
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn't use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don't contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

def avoids(word, forbidden_list):
    '''
    returns True if the word doesn't use any of the forbidden letters
    '''
    for letter in word:
        if letter in forbidden_list:
            return False
        return True

def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

forbidden_letters = str(input("Enter a string of forbidden letters: "))

fin = open('words.txt')

word_count = 0 
for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        word_count += 1

print("Number of words that do not contain forbidden letters: ", word_count)