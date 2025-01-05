from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = (m + n) - 1

        while(i >= 0 and j >= 0):
            if(nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        print(nums1)
        """
        Do not return anything, modify nums1 in-place instead.
        """
       


s = Solution()

case1 = {
    "nums1": [1,2,3,0,0,0],
    "nums2": [2,5,6],
    "n": 3,
    "m": 3
}

case2 = {
    "nums1": [-33,-33,-33,-25,-12,-9,-3,4,9,13,21,29,30,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "nums2": [-50,-50,-49,-48,-47,-45,-43,-40,-38,-37,-36,-35,-31,-30,-26,-24,-24,-21,-19,-17,-16,-13,-10,-10,-10,-9,-8,-6,-2,0,1,1,1,7,9,10,12,12,14,15,17,17,18,19,20,21,23,24,28,29,30,31,31,33,35,35,38,39,41,42,48,49,49],
    "n": 63,
    "m": 14
}

case3 = {
    "nums1": [0],
    "nums2": [1],
    "n": 1,
    "m": 0
}

s.merge(**case2)
