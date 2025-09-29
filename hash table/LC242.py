class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record=[0]*26
        s=list(s)
        t=list(t)
        for i in s:
            index=ord(i)-ord('a')
            record[index]+=1
        for i in t:
            index=ord(i)-ord('a')
            record[index]-=1
        for i, ele in enumerate(record):
            if ele!=0:
                return False
        return True