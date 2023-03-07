'''
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''

def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram("man","npm"))