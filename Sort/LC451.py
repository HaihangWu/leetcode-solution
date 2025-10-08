class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        return ''.join(char * freq for char, freq in sorted_chars)
