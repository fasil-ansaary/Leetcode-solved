# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        lst.sort()
        temp_node = ListNode(lst[0])
        temp_next = temp_node
        i = 1
        while i < len(lst):
            temp = ListNode(lst[i])
            temp_next.next = temp
            temp_next = temp
            i += 1
        return temp_node
        