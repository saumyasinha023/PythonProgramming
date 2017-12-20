import timeit
class Solution(object):
    def __init__(self):
        self.array=[]
    def permuteUnique(self, nums,i):
        b=list(nums)
        if i==len(nums)-1:
            if nums not in self.array:
                self.array.append(b)
        for ind in range(i,len(nums)):
            nums[ind],nums[i]=nums[i],nums[ind]
            self.permuteUnique(nums,i+1)
            nums[ind], nums[i] = nums[i], nums[ind]
        return self.array

var=Solution()
start = timeit.default_timer()
print(var.permuteUnique([1,1,0,0,1,-1,-1,1],0))
stop = timeit.default_timer()
print(stop-start)