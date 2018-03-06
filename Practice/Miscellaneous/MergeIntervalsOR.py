# Definition for an interval.
from collections import defaultdict


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


intervals = []


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        final=[]
        for each in intervals:
            if not final or each.start>final[-1].end:
                final.append(each)
            else:
                final[-1].end=max(each.end, final[-1].end)
        return final




intervals.append(Interval(2, 6))
intervals.append(Interval(8, 10))
intervals.append(Interval(1, 3))
intervals.append(Interval(15, 18))
S=Solution()
final=S.merge(intervals)

print(final[2].end,final[2].start)