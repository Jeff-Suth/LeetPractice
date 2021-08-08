# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
# outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# -2147483648 to 2147483647
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 123, -123, 901000, 1534236469

num =1534236469


def reverse(x):
    # add way to deal with negative number
    # temp = str(x)[::-1]
    temp = str(x)
    if "-" in temp:
        temp_neg = temp.replace("-", "") # blank out negative since it will ruin the reversed string, we'll add it later
        temp_neg = temp_neg[::-1] # reverse the string by slice, we can concatenate it since they are both strings
        while temp_neg.find("0") == 0 and len(temp_neg) > 1: # Confirm if there is any leading zeroes
            temp_neg = temp_neg.replace("0", "", 1) # If there are, then remove leading zeroes
        temp_neg = "-" + temp_neg
        if int(temp_neg) < -2147483648:
            temp_neg = 0
        return temp_neg
    else:
        temp = temp[::-1]
        while temp.find("0") == 0 and len(temp) > 1:
            temp = temp.replace("0", "", 1)
        if int(temp) > 2147483647:
            temp = 0
        return temp


print(reverse(num))

# Type casting and slicing! Another easy problem to help boost your confidence! You're smarter than you realize :)
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# delftstack.com/howto/python/remove-substring-from-a-string-python/
