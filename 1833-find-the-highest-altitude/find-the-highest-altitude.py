class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        pref = [0]
        alt = 0
        for i in gain:
            alt += i
            pref.append(alt)
        return max(pref)