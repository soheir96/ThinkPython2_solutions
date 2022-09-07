'''
Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?
'''

def uses_all(word, required_letters):
    '''
    returns True if the word uses all the required letters at least once
    '''
    for letter in required_letters:
        if letter not in "".join(word.split()):
            return False
    return True

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiou'):
        count += 1

print("There are", count, "words that use ALL of the letters, 'aeiou'.")