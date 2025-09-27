class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        s=list(path)
        n=len(s)
        left=0
        while left<n:
            if s[left]==".":
               s[left]=" "
            left+=1
        return "".join(s)