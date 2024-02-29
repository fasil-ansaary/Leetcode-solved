class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sub = '-'
        string_num = str(x)
        lst = [i for i in string_num]
        if '-' in lst:
            y = -1*int(''.join(lst[:0:-1]))
        else:
            y = int(''.join(lst[::-1]))
        if y >= math.pow(2,31) - 1 or y <= math.pow(-2,31):
            return 0
        return y
