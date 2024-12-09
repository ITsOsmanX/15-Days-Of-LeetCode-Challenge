class Solution(object):
    def containsDuplicate(self, nums):
        Temp = set()
        
        for num in nums:
            if num in Temp:
                return True
            Temp.add(num)
        
        return False
