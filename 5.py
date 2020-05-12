# https://leetcode.com/problems/longest-palindromic-substring/
# 特殊情况：连续重复字符也算回文，因此每个i对应的回文起点可能有多个
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def append(dic, k, v):
            if dic.get(k):
                dic[k].append(v)
            else:
                dic[k] = [v]
        if len(s) <= 1:
            return s
        end_start_dict = {}
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == s[i-1]:
                append(end_start_dict, i, i-1)
            if i > 1 and c == s[i-2]:
                append(end_start_dict, i, i-2)
            if i-1 in end_start_dict:
                prev_starts = end_start_dict[i-1]
                for prev_start in prev_starts:
                    if prev_start > 0 and s[prev_start-1] == s[i]:
                        append(end_start_dict, i, prev_start-1)
            
        max_len = 0
        max_end = 0
        max_start = 0
        for end, starts in end_start_dict.items():
            start = starts[-1]
            cur_len = end - start + 1
            if cur_len > max_len:
                max_len = cur_len
                max_end = end
                max_start = start
        return s[max_start: max_end + 1]

if __name__ == "__main__":
    s = "bbbbb"
    sub = Solution().longestPalindrome(s)
    print(sub)