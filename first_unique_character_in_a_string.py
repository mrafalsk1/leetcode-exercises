class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for index, character in enumerate(s):
            if counter.get(character):
                counter[character] = [index, counter[character][1] + 1]
            else:
                counter[character] = [index, 1]

        first_unique = len(s)
        for entry in counter.items():
            if entry[1][1] == 1:
                return entry[1][0]
        return -1


s = Solution()
input = "loveleetcode"
first = s.firstUniqChar(input)
print(first)
