'''
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-
p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
'''

def is_triple_double(word):
    '''
    Tests if a word contains three consecutive double letters.
    '''
    i = 0
    double_letter_count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            double_letter_count += 1
            if double_letter_count == 3:
                return True 
            i = i + 2
        else:
            i = i + 1 - 2*double_letter_count
            double_letter_count = 0
    return False


def find_triple_double():
    '''
    Reads a word list and prints words with triple double letters.
    '''
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have three consecutive double letters:')
find_triple_double()