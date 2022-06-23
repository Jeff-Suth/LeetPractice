# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
# 121, 123
num = 123

def isPalindrome(x):
    # Gah same issue, check for negatives!
    temp = int(str(x)[::-1])
    if temp == x:
        print(f"{x} is a palindrome number")
        return True
    else:
        print(f"{x} is NOT a palindrome number")
        return False

print(isPalindrome(num))