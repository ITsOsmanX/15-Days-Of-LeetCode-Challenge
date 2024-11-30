class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        sorted_list = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sorted_list.append(nums1[i])
                i += 1
            else:
                sorted_list.append(nums2[j])
                j += 1
        while i < m:
            sorted_list.append(nums1[i])
            i += 1
        
        while j < n:
            sorted_list.append(nums2[j])
            j += 1
        
        for k in range(m + n):
            nums1[k] = sorted_list[k]
