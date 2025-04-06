from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        a = []
        for i in range(n + 1):
            j = i
            step_bits = 0
            while j:
                j = j & (j - 1)
                step_bits += 1
            a.append(step_bits)
        return a


s = Solution()
a = s.countBits(5)
print(a)
