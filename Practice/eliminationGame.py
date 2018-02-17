#
#
# Each time loop gets traversed, “remaining” terms get halved.
#
# Each time loop gets traversed, “left” toggles between “True” and False
#
# Head may or may not be affected when traversed.
# 3.1 head always gets update in two cases
# 3.1.1. moving from left - easy to understand, first item always gets popped
# 3.1.2. moving from right, if number of items “remaining” are odd - this needs a little understanding. To simplify visualization, assume elimination from right, happens from “left”, so that the last item must be always eliminated. (Or think that “left” elimination - first item must always be eliminated, “right” elimination - “last” item must always be eliminated). Now the last item is either at “even” position or at “odd” position (after previous elimination). If the last item is at odd, then elimination must begin at first odd place(in the current configuration) - which is head. So head gets updated in this case.
#
# By what value should head be updated?
# 4.1. It depends on “round number”.
# 4.2. In the first round, it will be updated by 1 (because step is 1) - 2^0
# 4.3. In the second round, it will be updated (subject to point 3) by - 2^1
# 4.4. In the kth round, it will be updated by - 2^k
#
# Reasoning behind step 4 -
# 5.1. Again visualize that elimination is always from left with condition that “first” and “last” item must always be eliminated in alternating elimination round
# 5.2. In the first step, all odd places are eliminated - (1) 2 (3) 4 (5) 6 (7) 8 (9) 10 (11) 12 (13) 14 (with at most 0 factor of 2)
# 5.3. In the second round, all places with one factor of 2 gets eliminated -
# (2) 4 (6) 8 (10) 12 (14) (with at most 1 factor of 2)
# 5.4. In the third round, all places with one factor of 4 gets eliminated -
# (4) 8 (12) (with at most 2 factors of 2)
# 5.5. The reason behind this is each time number of remaining terms are getting halved, in the manner described above or considered alternatively round 1 eliminates table of 1 excluding all even, round 2 eliminates table of 2 excluding multiples of 4, round 3 eliminates table of 4 excluding multiples of 8, and so on.

class Solution():
    def lastREmaining(self,n):
        left=True
        remaining =n
        step,head=1,1
        while remaining>1:
            if (left or remaining%2==1):
                head+=step
            remaining=int(remaining/2)
            step*=2
            left=not left
        return head

S=Solution()
print(S.lastREmaining(9))