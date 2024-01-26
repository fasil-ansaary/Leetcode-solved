class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """        
        vowels = 'aeiou'
        init_c = len([i for i in s[0:k] if i in vowels])
        c = init_c
        l,j = 1,k
        while j<len(s):
            if s[l-1] in vowels:
                c -= 1
            if s[j] in vowels:
                c += 1
            init_c = max(init_c, c)
            l += 1
            j += 1
        return init_c