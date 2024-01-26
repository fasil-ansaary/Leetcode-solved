class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        if len(cards) == 1:
             return -1
        dct = {}
        c = float('Inf')
        for i in range(len(cards)):
            if cards[i] not in dct:
                dct[cards[i]] = i
            else:
                c = min(c, i-dct[cards[i]])
                dct[cards[i]] = i
        if c > len(cards):
            return -1
        return c + 1
