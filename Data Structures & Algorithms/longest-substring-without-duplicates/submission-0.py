class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        last = {}
        left = 0
        longest = 0

        for i, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = i
            longest = max(longest, i - left + 1)

        return longest
        