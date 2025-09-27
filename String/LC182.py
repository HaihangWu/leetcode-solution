class Solution(object):
    def swap(self, left,right,password):
        while left<right:
            password[left], password[right]=password[right], password[left]
            left+=1
            right-=1
        return password

    def dynamicPassword(self, password, target):
        """
        :type password: str
        :type target: int
        :rtype: str
        """
        password=list(password)
        n=len(password)
        left=0
        right=target-1
        password=self.swap(left,right,password)
        left=target
        right=n-1
        password=self.swap(left,right,password)
        left=0
        right=n-1
        password=self.swap(left,right,password)
        return ''.join(password)