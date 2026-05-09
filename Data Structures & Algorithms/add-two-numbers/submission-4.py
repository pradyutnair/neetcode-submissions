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

        # Pointers
        i, j = l1, l2
        # Dummy node to store
        dummy = ListNode()
        curr = dummy
        carry = 0
        while i or j:
            # Current values
            vi = i.val if i else 0
            vj = j.val if j else 0

            # Sum
            total = carry + vi + vj
            # Quotient and remainder
            carry, res = total // 10, total % 10

            # Node = Remainder
            curr.next = ListNode(res)
            # Move pointers
            curr = curr.next

            if i:
                i = i.next
            if j:
                j = j.next

        # Check if carry remains and create a new node for it
        if carry:
            node = ListNode(carry)
            curr.next = node
        return dummy.next
