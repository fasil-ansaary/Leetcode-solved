class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        partition = []
        string = ''
        while i < len(s):            
            if s[i] not in string:
                string += s[i]                
            else:
                partition.append(string)
                i -= 1
                string = ''
            i += 1
        if len(string) != 0:
            partition.append(string)
        return len(partition)
