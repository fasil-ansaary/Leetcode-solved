class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        dummy = []
        while i<len(s):            
            if s[i] in vowels:
                c = 0
                while j>=0:
                    if s[j] in vowels:
                        dummy.append(s[j])
                        c += 1
                        j -= 1
                        break
                    j -= 1
                if c == 0:
                    dummy.append(s[i])
            else:
                dummy.append(s[i])
            i += 1
        return "".join(dummy)
                
