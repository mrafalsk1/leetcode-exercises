from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_right = len(nums) - 1
        p_left = 0

        while p_right >= p_left:
            print(nums)
            if nums[p_left] == val:
                temp = nums[p_right]
                nums[p_right] = nums[p_left]
                nums[p_left] = temp
                p_right -= 1
            else:
                p_left += 1

        return p_left


s = Solution()

inp = {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2}

inp2 = {"nums": [3, 2, 2, 3], "val": 3}

np3 = {"nums": [1], "val": 1}
k = s.removeElement(**inp2)
print(k)
