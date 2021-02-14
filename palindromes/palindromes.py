# 1.
def isPalindromeOne(string):
    reversed_string = ""
    for s in reversed(range(len(string))):
        reversed_string += string[s]
    return string == reversed_string
## call function:
# print(isPalindromeOne("aba"))
# print(isPalindromeOne("ojo"))
# print(isPalindromeOne("bless"))
# print(isPalindromeOne("a"))
## Time Complexity: O(n^2)
# In python, strings are immutable. Hence, when I add a character to the string, 
# it means I am recreating the whole string. This operation is done in linear time, O(n).
# which means that as the input size, n, increases, so will the time it takes the algorithm to run.
# But note that it is done within a loop which runs for n times,
# Hence, O(n) * n = O(n^2)
## Space Complexity: O(n)
# n characters are stored in reversed_string. As n increases, so will the space, hence O(n)

# 2.
def isPalindromeTwo(string):
    reversed_string = []
    for s in reversed(range(len(string))):
        reversed_string.append(string[s])
    return string == "".join(reversed_string)
## call function:
print(isPalindromeTwo("aba"))
print(isPalindromeTwo("ojo"))
print(isPalindromeTwo("bless"))
print(isPalindromeTwo("a"))