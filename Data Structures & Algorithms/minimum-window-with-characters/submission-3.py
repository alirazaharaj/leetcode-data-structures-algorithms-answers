from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)          # how many chars from t are still needed

        left = 0
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            # If this char is still needed, we reduce missing count
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # When all needed chars are present, try shrinking window
            while missing == 0:
                # Update best answer
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                # Remove left char and move left pointer
                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]