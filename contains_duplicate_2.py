from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p_left, p_right = 0, 0

        seen = set()
        seen.add(nums[0])
        while p_right < len(nums) - 1:
            p_right += 1
            print(p_left, p_right)
            print(p_left - p_right)
            if nums[p_right] in seen:
                return True
            seen.add(nums[p_right])
            if len(seen) > k:
                if k > 0:
                    seen.remove(nums[p_left])
                else:
                    seen.clear()
                p_left += 1

        return False


input = {"nums": [1, 0, 1, 1], "k": 1}
input2 = {"nums": [1, 2, 3, 1, 2, 3], "k": 2}
input3 = {"nums": [0, 1, 2, 3, 2, 5], "k": 3}
input4 = {"nums": [1, 2, 3, 1], "k": 3}
s = Solution()
print(s.containsNearbyDuplicate(**input4))
