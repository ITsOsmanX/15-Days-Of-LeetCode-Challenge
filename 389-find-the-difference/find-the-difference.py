class Solution(object):
    def findTheDifference(self, s, t):
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return char
            else:
                char_count[char] -= 1



                
        