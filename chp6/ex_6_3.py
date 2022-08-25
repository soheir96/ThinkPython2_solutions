# palindrome.py 

def first(word):
    """Returns the first character of a string."""
    return word[0]

def last(word):
    """Returns the last character of a string."""
    return word[-1]

def middle(word):
    """Returns all but the first and last character of a string."""
    return word[1:-1]

def is_palindrome(word):
    """Returns True if word is a palindrome."""

    # validate input is string
    if not isinstance(word, str):
        print("Error - Function can only take a string.")
        return None 
 
    if len(word) <= 1:
        return True
    
    if first(word) != last(word):
        return False 
    
    return is_palindrome(middle(word))

print(is_palindrome('redivider'))