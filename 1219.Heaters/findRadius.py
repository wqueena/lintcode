import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        outr = 0
        heaters.sort()
        for house in houses:
            r = 0x7FFFFFFF
            right = bisect.bisect_right(heaters, house)
            if right > 0:
                r = min(r, house - heaters[right - 1])
            left = bisect.bisect_left(heaters, house)
            if left < len(heaters):
                r = min(r, heaters[left] - house)
            outr = max(r, outr)
        return outr
