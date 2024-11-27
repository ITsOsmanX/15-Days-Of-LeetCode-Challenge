class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(0,len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
            

        