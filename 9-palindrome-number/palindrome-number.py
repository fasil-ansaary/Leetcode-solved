class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m=x
        rem=0
        while(x>0):
            div=x%10
            rem=(rem*10)+div
            x=x//10
        
        if rem==m:
            return True
        else:
            return False