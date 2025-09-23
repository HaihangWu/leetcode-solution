class Solution(object):
    def swapPairs(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur_node = dummy_head
        iter = 0
        while cur_node.next is not None and cur_node.next.next is not None:
            tmp = cur_node.next
            tmp1 = cur_node.next.next.next

            cur_node.next = cur_node.next.next
            cur_node.next.next = tmp
            cur_node.next.next.next = tmp1

            cur_node = cur_node.next.next

        return dummy_head.next
