'''
Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?
'''

def uses_only(word, letters_list):
    '''
    returns True if the word contains only letters in the list
    '''
    for char in "".join(word.split()):
        if char not in letters_list:
            return False
    return True  

# print(uses_only('cat', 'actr'))
# print(uses_only('catarax', 'actr'))

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo'):
        count += 1

print("There are", count, "words that only use the letters 'acefhlo'.")