# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i, j = list1, list2
        dummy = ListNode()
        curr = dummy
        while i and j:
            if i.val <= j.val:
                curr.next = i
                i = i.next
            else:
                curr.next = j
                j = j.next 
            curr = curr.next
        
        if i:
            curr.next = i
        if j:
            curr.next = j
        return dummy.next
        
        

        