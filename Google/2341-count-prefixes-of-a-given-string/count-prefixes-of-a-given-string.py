class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        i = 1
        c = 0
        while i<=len(s):
            if s[:i] in words:
                c += words.count(s[:i])
            i += 1
        return c