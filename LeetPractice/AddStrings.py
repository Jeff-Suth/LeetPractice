# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers
# (such as BigInteger). You must also not convert the inputs to integers directly.

num1 = "11"
num2 = "123"

def addStrings(num1, num2):
    # temp1 = int(num1)
    # temp2 = int(num2)
    # temp3 = temp1 +temp2
    # num3 = str(temp3)

    # temp1 = int(num1)
    # temp2 = int(num2)
    #
    # num3 = str(temp1 + temp2)

    temp = int(num1) + int(num2)
    return str(temp)

print(addStrings(num1, num2))