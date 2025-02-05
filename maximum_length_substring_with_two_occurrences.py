class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        p_left, p_right = 0, 0

        _max = -1
        counter = {}
        counter[s[0]] = 1
        while p_right < len(s) - 1:
            p_right += 1
            if counter.get(s[p_right]):
                counter[s[p_right]] += 1
            else:
                counter[s[p_right]] = 1

            while counter[s[p_right]] == 3:
                counter[s[p_left]] -= 1
                p_left += 1

            _max = max(_max, p_right - p_left + 1)

        return _max


s = Solution()
input = "bcbbbcba"
max = s.maximumLengthSubstring(input)
print(max)
