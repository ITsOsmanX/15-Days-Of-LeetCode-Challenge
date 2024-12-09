class Solution(object):
    def firstUniqChar(self, s):
        repeated = []
        for i in range (0,len(s)):
            if s[i] not in s[i+1:] and s[i] not in repeated:
                return i
            else:
                repeated.append(s[i])
        return -1     

        