class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <4:
            if x == 0:
                return x
            return 1
        mid = x//2
        temp = mid
        while mid*mid >x:
            temp =mid
            mid = mid//2
        mid = temp
        if mid*mid ==x:
            return mid
        else:
            for i in range(1, mid+2):            
                if i*i == x:
                    return i
                if i*i > x:
                    return i-1
                i += 1
        # return mid