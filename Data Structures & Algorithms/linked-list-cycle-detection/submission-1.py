# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        # create one node that moves 1 node and another that jumps 2 nodes at once if they ever equal then we know it is a cycle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


        return False