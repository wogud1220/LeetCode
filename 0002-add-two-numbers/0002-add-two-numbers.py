# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        result = []
        result2 = []
        def dfs(node):
            if not node:
                return
            dfs(node.next)
            result.append(node.val)

        def dfs2(node):
            if not node:
                return
            dfs2(node.next)
            result2.append(node.val)

        dfs(l1)
        dfs2(l2)

        s1 = int(''.join(map(str,result)))
        s2 = int(''.join(map(str, result2)))
        s3 = s1 + s2 # int 형태
        s3 = str(s3)
        s3 = list(map(int,s3))

        for i in s3[::-1]:
            answer.append(i)

        dummy = ListNode(0)

        cur = dummy

        for num in answer:

            cur.next = ListNode(num)

            cur = cur.next

        return dummy.next
