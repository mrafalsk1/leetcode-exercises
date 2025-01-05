from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p_negative = 0
        p_positive = len(nums) - 1
        out = [0 for i in range(len(nums))]
         
        while(p_negative != p_positive):
            n_negative = nums[p_negative] ** 2
            n_positive = nums[p_positive] ** 2
    
            if(n_negative > n_positive):
                out[p_positive - p_negative] = n_negative 
                p_negative += 1
            else:
                out[p_positive - p_negative] = n_positive 
                p_positive -= 1

        print(out)            

s = Solution()

nums = [-4,-1,0,3,10]

s.sortedSquares(nums)
