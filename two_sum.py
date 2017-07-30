class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        l = len(nums)
        for i in range(l):
            d[nums[i]] = i
        for i in range(l):
            comp = target - nums[i]
            if d.has_key(comp):
                if i!=d[comp]:
                    return [i,d[comp]]