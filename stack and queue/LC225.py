class MyStack(object):

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.queue_in) > 0:
            while len(self.queue_out) > 0:
                tmp = self.queue_out.pop()
                self.queue_in.appendleft(tmp)
            while len(self.queue_in) > 0:
                tmp = self.queue_in.pop()
                self.queue_out.appendleft(tmp)
        self.queue_in.appendleft(x)

        while len(self.queue_out) > 0:
            tmp = self.queue_out.pop()
            self.queue_in.appendleft(tmp)

        return None

    def pop(self):
        """
        :rtype: int
        """
        if len(self.queue_in) > 0:
            while len(self.queue_out) > 0:
                tmp = self.queue_out.pop()
                self.queue_in.appendleft(tmp)
            while len(self.queue_in) > 0:
                tmp = self.queue_in.pop()
                self.queue_out.appendleft(tmp)
        return self.queue_out.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue_in) > 0:
            while len(self.queue_out) > 0:
                tmp = self.queue_out.pop()
                self.queue_in.appendleft(tmp)
            while len(self.queue_in) > 0:
                tmp = self.queue_in.pop()
                self.queue_out.appendleft(tmp)
        return self.queue_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue_out) > 0 or len(self.queue_in) > 0:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()