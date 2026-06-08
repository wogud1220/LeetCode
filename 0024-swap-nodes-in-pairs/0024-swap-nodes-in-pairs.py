# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None
        

        if head == None:
            return head
        elif head.next == None:
            return head
        start = head.next
        while cur and cur.next != None:

            adj_cur = cur.next
            cur.next = adj_cur.next
            adj_cur.next = cur
            if prev:
                prev.next = adj_cur



            prev = cur
            cur = cur.next
            
        return start