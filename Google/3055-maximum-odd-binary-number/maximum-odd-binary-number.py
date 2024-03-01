class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = [int(i) for i in s]
        lst.sort()
        fnl_str = str(lst[-1])
        lst = lst[::-1]
        lst = lst[1:]
        val = ''.join([str(elem) for elem in lst])
        val += fnl_str
        return val
        