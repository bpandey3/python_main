#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# Definition for singly-linked list.
class ListNode(object):
    
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

    def inserAtEnd(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result


def Main():
     list =  ListNode(2)
     list.inserAtEnd(4)
     list.inserAtEnd(3)

     list2 =  ListNode(2)
     list2.inserAtEnd(6)
     list2.inserAtEnd(3)
     print()
    
     s = Solution()
     print(s.addTwoNumbers(list2,list))

Main()