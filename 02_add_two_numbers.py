'''
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        p1, p2, lft, head = l1, l2, 0, ListNode(0)
        res = head

        while(p1 or p2 or lft):
            val_1, val_2 = p1.val if p1 else 0, p2.val if p2 else 0
            sum = val_1 + val_2 + lft
            head.next = ListNode(sum % 10)
            lft = sum // 10
            p1, p2, head = p1.next if p1 else None, p2.next if p2 else None, head.next
        return res.next
