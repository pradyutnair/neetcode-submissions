# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Brute force:
        # n1 = ''
        # n2 = ''
        # curr = l1
        # while curr:
        #     n1 += str(curr.val)
        #     curr = curr.next
        # curr = l2
        # while curr:
        #     n2 += str(curr.val)
        #     curr = curr.next
        
        # res = int(n1[::-1]) + int(n2[::-1])
        # res_str = str(res)

        # dummy = ListNode()
        # curr = dummy
        # i = len(res_str) - 1
        # while i>=0:
        #     curr.next = ListNode(int(res_str[i]))
        #     curr = curr.next
        #     i -= 1

        # return dummy.next
        
        i, j = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        while i or j:
            if i:
                vi = i.val
            else:
                vi = 0
            if j:
                vj = j.val
            else:
                vj = 0
        
            # Sum
            vsum = carry + vi + vj
            # Quotient and remainder
            carry, res = vsum // 10, vsum % 10

            curr.next = ListNode(res)
            curr = curr.next

            if i:
                i = i.next
            if j:
                j = j.next

        # Check if carry remains and create a new node for it
        if carry:
            node = ListNode(carry)
            curr.next=node
        return dummy.next





        