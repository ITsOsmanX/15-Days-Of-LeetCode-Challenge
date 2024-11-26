class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_set = set(nums)
        dis_num = []
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                dis_num.append(i)
        return dis_num

