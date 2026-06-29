# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next
        cur = head
        if length == n:
            return cur.next
            
    

        
        i = 0
        while i < length - n - 1:
            cur = cur.next
            i +=1
        cur.next = cur.next.next
        return head