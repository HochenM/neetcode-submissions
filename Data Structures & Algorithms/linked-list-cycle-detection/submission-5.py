# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        newhead = head

        while newhead:
            if newhead in seen:
                return True
            seen.add(newhead)
            newhead = newhead.next


            

        return False
        


        