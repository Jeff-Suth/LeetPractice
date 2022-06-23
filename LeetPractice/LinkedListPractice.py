
# class ListNode:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None

# data, nextnode
class ListNode(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = ListNode(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # found the data
            else:
                prev_node = this_node
                this_node - this_node.get_next()
        return False # didn't find the data
    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d # found it
            else:
                this_node.get_next()
        return None #didn't find it

myList = LinkedList
myList.add(5)
myList.add(3)
myList.add(8)
print(myList)
myList.remove(8)
print(myList)

# class LinkedList:
#     def __init__(self):
#         self.head = ListNode()
#     # Append something to end of LinkedList
#     def append(self, data):
#         new_node = ListNode(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
#     # Length of linked list
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next != None:
#             total += 1
#             cur = cur.next
#         return total
#     # Help display current contents of list
#     def display(self):
#         elems = []
#         cur_node = self.head
#         while cur_node.next != None:
#             cur_node = cur_node.next
#             elems.append(cur_node.data)
#         print(elems)
#     # Get number at index
#     def get(self,index):
#         if index >= self.length():
#             print("ERROR: 'Get' Index out of range!")
#             return None
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             cur_node = cur_node.next
#             if cur_idx == index:
#                 return cur_node.data
#             cur_idx += 1
#     # Erase node at certain index
#     def erase(self,index):
#         if index >= self.length():
#             print("ERROR: 'Erase' Index out of range!")
#             return
#         cur_idx = 0
#         cur_node = self.head
#         while True:
#             last_node = cur_node
#             cur_node = cur_node.next
#             if cur_idx == index:
#                 last_node.next = cur_node.next
#                 return
#             cur_idx += 1
#
#
#
# my_list = LinkedList()
#
# my_list.display()
#
# my_list.append(2)
# my_list.append(4)
# my_list.append(3)
#
# my_list.display()
#
# my_list.get(2)
#
# my_list.erase(1)
#
# my_list.display()

# What are linked lists? Can we pop the number at index[0] off and then just add the index[0] of l1 and l2 into a new
# linked list known as l3? I think it will have to be a Doubley Linked List since it needs to be reversed or some
# monkeying around with reversing the order of indices or reversing what we take out. Looks like we take out numbers
# from each linked list and then turn them into integers and then change the integers into

# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None
#
# class SLinkedList:
#    def __init__(self):
#       self.headval = None
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# # Link first Node to second node
# list1.headval.nextval = e2
#
# # Link second Node to third node
# e2.nextval = e3