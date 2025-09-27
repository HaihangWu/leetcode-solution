class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i=0
        s=list(s)
        while i< len(s):
            if (len(s)-i)>=2*k or ((len(s)-i)<2*k and (len(s)-i)>=k):
                left, right=i, i+k-1
            elif (len(s)-i)<k:
                left, right=i, len(s)-1
            while left < right:
                s[left], s[right]=s[right], s[left]
                left+=1
                right-=1

            i+=2*k
        return "".join(s)