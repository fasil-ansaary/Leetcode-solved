class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = ['I','V','X','L','C','D','M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        string = [i for i in s]
        sum_count = value[roman.index(string[0])]
        for i in range(1, len(string)):
            if value[roman.index(string[i])] > value[roman.index(string[i-1])]:
                sum_count -=value[roman.index(string[i-1])]
                sum_count += value[roman.index(string[i])] - value[roman.index(string[i-1])]
            else:
                sum_count += value[roman.index(string[i])]
        return sum_count
        