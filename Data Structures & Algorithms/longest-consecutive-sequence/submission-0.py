class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        numbers = sorted(list(set(nums)))

        longest = 1
        current_streak = 1
        for i in range(len(numbers) - 1):
            if numbers[i + 1] == numbers[i] + 1:
                current_streak += 1
            else:
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)