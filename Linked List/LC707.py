class ListNode():
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode(0)
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size or index < 0:
            return -1
        else:
            cur = self.dummy_head
            index_tmp = 0
            while index_tmp <= index:
                cur = cur.next
                index_tmp += 1
            return cur.value

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        New_node = ListNode(val)
        if index == 0:
            New_node.next = self.dummy_head.next
            self.dummy_head.next = New_node
            self.size += 1
        elif index <= self.size and index > 0:
            cur = self.dummy_head
            index_tmp = 0
            while index_tmp < index:
                cur = cur.next
                index_tmp += 1
            # if index <self.size:
            #     New_node.next=cur.next
            New_node.next = cur.next
            cur.next = New_node
            self.size += 1

        elif index > self.size:
            return

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= 0 and index < self.size:
            cur = self.dummy_head
            index_tmp = 0
            while index_tmp < index:
                cur = cur.next
                index_tmp += 1
            cur.next = cur.next.next
            self.size -= 1
        else:
            return
