class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        step_bits = 0
        while n >= 2**bits:
            if n & 2**bits:
                step_bits += 1
            bits += 1
        return step_bits


n1 = 11
n2 = 128
n3 = 2147483645
s = Solution()
s.hammingWeight(n3)
