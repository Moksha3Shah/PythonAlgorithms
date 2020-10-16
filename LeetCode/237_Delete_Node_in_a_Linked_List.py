# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

def __init__(self,value,next=None):
    self.value = value
    self.next = next

def getNext(self):
    return self.next

def getValue(self):
    return self.value

class LinkedList:

def __init__(self,node):
    self.node = node

def __str__(self):
    node = self.node
    s = "[Node " + str(node.getValue())
    if node.getNext() is None:
        return s + "]"
    while node.next is not None:
        s += ", Node " + str(node.next.value)
        node = node.next
    return s + "]"

def delete(self,value):
    head = self.node
    if head.getValue() == value:
        return LinkedList(head.next)
    temp = head
    while temp.next is not None:
        if temp.next.getValue() == value:
            temp = temp.next.next
                return self
            temp.next = None
            return LinkedList(head)
        temp = temp.next
    return "Sorry node is not here!"
