# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        out = head
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        head = out
        while len(stack) > 0:
            head.val = stack.pop()
            head = head.next

        return out
        