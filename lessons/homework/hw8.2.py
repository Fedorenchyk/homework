import string
def is_palindrome(text):
    text = text.replace(" ", "")
    text = text.lower()

    for symbol in string.punctuation:
        text = text.replace(symbol, "")
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
