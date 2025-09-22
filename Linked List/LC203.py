class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head=ListNode(0)
        dummy_head.next=head
        cur=dummy_head
        while cur.next is not None:
            if (cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur=cur.next
        head=dummy_head.next
        return head