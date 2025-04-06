from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        xor_nums = 0
        xor_0_size = 0
        for n in nums:
            xor_nums = xor_nums ^ n
        for i in range(size + 1):
            xor_0_size = xor_0_size ^ i
        return xor_0_size ^ xor_nums


nums1 = [3, 0, 1]
ans = 2
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
s = Solution()
a = s.missingNumber(nums2)
print(a)
