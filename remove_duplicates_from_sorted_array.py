from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_right = 1 
        p_left = 0

        while(p_right < len(nums)):
            print(nums)
            print(p_left,p_right)
            if(nums[p_left] < nums[p_right]): 
                temp = nums[p_right]
                nums[p_right] = nums[p_left + 1]
                nums[p_left + 1] = temp
                p_left += 1
                p_right = p_left + 1
            else:
                p_right += 1

        return p_left + 1
        print(nums)
s = Solution()

inp1 = [1,1,2]
inp2 = [0,0,1,1,1,2,2,3,3,4]

k = s.removeDuplicates(inp2)
print(k)



