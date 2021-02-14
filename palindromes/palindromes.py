# 1.
def isPalindrome(string):
    reversed_string = ""
    for s in reversed(range(len(string))):
        reversed_string += string[s]
    return string == reversed_string

print(isPalindrome("aba"))
print(isPalindrome("ojo"))
print(isPalindrome("bless"))
