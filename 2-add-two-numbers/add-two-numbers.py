# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ls1, ls2 = '', ''
        while l1 != None:
            ls1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            ls2 += str(l2.val)
            l2 = l2.next
        fnl_val = [int(i) for i in str((int(ls1[::-1])+int(ls2[::-1])))[::-1]]
        i = 1
        temp_node = ListNode(fnl_val[0])
        temp_next = temp_node
        while i < len(fnl_val):
            temp = ListNode(fnl_val[i])
            temp_next.next = temp
            temp_next = temp
            i += 1
        return temp_node
