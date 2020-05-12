# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        cur_start = 0
        cur_end = 0

        for i, c in enumerate(s):
            repeat_index = None
            if i == cur_start:
                continue
            if c in s[cur_start:i]:
                repeat_index = s[cur_start:i].index(c) + cur_start
                cur_end = i-1
            elif i == len(s) - 1:
                cur_end = i
            if cur_end - cur_start > end - start:
                start = cur_start
                end = cur_end
            if repeat_index != None:
                cur_start = repeat_index + 1

        return end - start + 1

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = 0
        start = 0
        indexDict = {}
        for i, c in enumerate(s):
            if c in indexDict:
                start = max(start, indexDict[c] + 1)
            indexDict[c] = i
            length = max(length, i - start + 1)
        return length

if __name__ == "__main__":
    s = "abcabcbb"
    i = Solution2().lengthOfLongestSubstring(s)
    print(i)