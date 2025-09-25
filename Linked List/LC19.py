class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        left_node = dummy_head
        right_node = dummy_head
        iter = 0
        while iter < n and right_node.next is not None:
            right_node = right_node.next
            iter += 1
        if iter < n:
            return

        while right_node.next is not None:
            left_node = left_node.next
            right_node = right_node.next

        left_node.next = left_node.next.next

        return dummy_head.next
