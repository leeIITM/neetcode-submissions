# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        sol = ListNode(-1)
        out = sol

        carryforward = 0
        while head1 and head2:
            summ = head1.val + head2.val + carryforward
            if summ > 9:
                a = ListNode(summ % 10)
                carryforward = summ // 10
            else:
                a = ListNode(summ)
                carryforward = 0
            out.next = a
            head1 = head1.next
            head2 = head2.next
            out = out.next
        while head1:
            summ = carryforward + head1.val
            if summ > 9:
                a = ListNode(summ % 10)
                carryforward = summ // 10
                out.next = a
                out = out.next
                head1 = head1.next
            else:
                carryforward = 0
                a = ListNode(summ)
                out.next = a
                out = out.next
                head1 = head1.next
        
        while head2:
            summ = carryforward + head2.val
            if summ > 9:
                a = ListNode(summ % 10)
                carryforward = summ // 10
                out.next = a
                out = out.next
                head2 = head2.next
            else:
                carryforward = 0
                a = ListNode(summ)
                out.next = a
                out = out.next
                head2 = head2.next
    

        if carryforward > 0:
            last = ListNode(carryforward)
            out.next = last

        return sol.next
