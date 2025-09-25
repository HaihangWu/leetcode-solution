# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        size_A = 0
        size_B = 0
        cur_A = headA
        cur_B = headB
        while cur_A is not None:
            cur_A = cur_A.next
            size_A += 1

        while cur_B is not None:
            cur_B = cur_B.next
            size_B += 1
        size_dif = size_A - size_B
        cur_A = headA
        cur_B = headB
        iter = 0
        while iter < abs(size_dif):
            iter += 1
            if size_dif <= 0:
                cur_B = cur_B.next
            else:
                cur_A = cur_A.next

        while cur_B is not None and cur_A is not None:
            if cur_A == cur_B:
                return cur_A
            else:
                cur_B = cur_B.next
                cur_A = cur_A.next
        return None