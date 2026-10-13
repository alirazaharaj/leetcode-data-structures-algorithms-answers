class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        left = 0
        max_count = 0
        count = {}
        longest = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest

