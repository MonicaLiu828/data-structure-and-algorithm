class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = max(time) * totalTrips

        def can_finish(m):
            total = 0
            for each_time in time:
                total += (m // each_time)
            if total >= totalTrips:
                return True
            return False

        while l + 1 < r:
            m = (l + r) // 2
            if can_finish(m):
                r = m
            else:
                l = m
        if can_finish(l):
            return l
        else:
            return r
