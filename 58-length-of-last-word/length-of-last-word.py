class Solution(object):
    def lengthOfLastWord(self, s):
        temp = 0
        length = 0
        
        for char in s:
            if char == " ":
                if temp > 0:
                    length = temp
                temp = 0
            else:
                temp += 1
        
        return temp if temp > 0 else length
