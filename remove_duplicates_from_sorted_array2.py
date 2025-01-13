from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_left = p_right = 2
        print(nums)
        while p_right < len(nums):
            if nums[p_right] != nums[p_left - 2]:
                nums[p_left] = nums[p_right]
                p_left += 1
            p_right += 1
            print(nums)
            
        return p_left


s = Solution()

inp1 = [1,1,1,2,2,3]
k = s.removeDuplicates(inp1)
        
