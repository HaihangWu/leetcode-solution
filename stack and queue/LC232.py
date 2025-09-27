class MyQueue(object):

    def __init__(self):
        self.stack_in = deque()
        self.stack_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while len(self.stack_out) > 0:
            tmp = self.stack_out.pop()
            self.stack_in.append(tmp)
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # if len(self.stack_out)==0:
        while len(self.stack_in) > 0:
            tmp = self.stack_in.pop()
            self.stack_out.append(tmp)
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        # if len(self.stack_out)==0:
        #     while len(self.stack_in) >0:
        #         tmp=self.stack_in.pop()
        #         self.stack_out.append(tmp)
        if len(self.stack_in) > 0:
            return self.stack_in[0]
        elif len(self.stack_out) > 0:
            return self.stack_out[-1]
        else:
            return None

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack_out) == 0 and len(self.stack_in) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()