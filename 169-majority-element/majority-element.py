class Solution(object):
    def majorityElement(self, nums):
        temp = set(nums)
        for i in temp:
            if nums.count(i) > len(nums)/2 :
                return i
        