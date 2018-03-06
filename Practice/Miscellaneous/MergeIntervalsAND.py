class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


intervals = []

class Solution():
    def merge(self,intervals):
        intervals.sort(key=lambda x:x.start)
        final=[]
        for each in intervals:
            if final and each.start<final[-1].end:
                final[-1].start=each.start
                final[-1].end=final[-1].end
            elif final and each.start>final[-1].end:
                continue
            else:
                final.append(each)
        return final


intervals.append(Interval(2, 6))
intervals.append(Interval(8, 10))
intervals.append(Interval(1, 3))
intervals.append(Interval(15, 18))
S=Solution()
final=S.merge(intervals)
print(len(final))
print(final[0].end,final[0].start)