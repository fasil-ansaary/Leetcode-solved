# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        
        i = 1
        while i < len(lst):
            key = lst[i]
            j = i-1
            while j >= 0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
            i += 1
        head = ListNode(lst[0])
        temp_head = head
        i = 1
        while i < len(lst):
            temp = ListNode(lst[i])
            temp_head.next = temp
            temp_head = temp
            i += 1
        return head


