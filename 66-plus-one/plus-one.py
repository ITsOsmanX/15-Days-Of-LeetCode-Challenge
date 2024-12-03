class Solution(object):
    def plusOne(self, digits):
        digits =''.join(map(str, digits))
        digits = int(digits)
        digits += 1

        digits = [int(char) for char in str(digits)]
        
        return digits