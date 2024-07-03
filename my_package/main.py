def is_palindrome(word='dad'):
    
    """Writing a function that checks if the word/phrase is a palindrome"""
    
    return word == word[::-1]


if __name__ == "__main__":
    print(is_palindrome())
    #specific argument
    print(is_palindrome('banana'))