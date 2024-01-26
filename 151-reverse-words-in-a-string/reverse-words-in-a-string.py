class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = [i for i in s.split()]
        return " ".join(lst[::-1])