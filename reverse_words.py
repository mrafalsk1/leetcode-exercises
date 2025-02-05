class Solution:
    def reverseWords(self, s: str):
        p_left, p_right = 0, 0
        res = ""
        while p_right < len(s):
            if s[p_right] != " ":
                p_right += 1
            else:
                res += s[p_left : p_right + 1][::-1]
                p_right += 1
                p_left = p_right
                print(res)

        print(p_left, p_right)
        res += " "
        res += s[p_left:p_right][::-1]
        print(res)
        return res[1:]


s = Solution()
string = "Mr Ding"

s.reverseWords(string)
