# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# l1 = [2,4,3]
# l2 = [5,6,4]

l1 = ListNode([2,4,3])
l2 = ListNode([5,6,4])

# print(l1.val) [2, 4, 3]
# print(l2.val) [5, 6, 4]

# while l1 or l2:
#     val1 = (l1.val if l1 else 0)
#     val2 = (l2.val if l2 else 0)
#     print(val1)
#     print(val2)


def addTwoNumbers(l1, l2):
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        temp = val1 + val2 + carry
        while temp >= 10:
            temp - 10
            carry += 1

        # carry, temp = divmod(val1+val2 + carry, 10)
#
#
        result_tail.next = ListNode(temp)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next

print(addTwoNumbers(l1, l2))
