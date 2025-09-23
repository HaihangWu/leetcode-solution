class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre=None
        cur=head
        if cur is None:
            return
        while cur.next is not None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        cur.next=pre
        return cur