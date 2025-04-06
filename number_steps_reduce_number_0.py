class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num = num >> 1
            steps += 1
        print(steps)
        return steps


s = Solution()
num = 14
s.numberOfSteps(num)
ans = 6
