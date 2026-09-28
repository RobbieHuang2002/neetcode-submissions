class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # initialize the while loop 
        while  0 < m and 0 < n:
            # if m is less than n we can replace last with n 
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                # if m is gte to n then replace last with m
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -=1 
        
        
