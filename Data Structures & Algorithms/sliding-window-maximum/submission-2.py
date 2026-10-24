from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq, ans = deque(), []

        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:  # chhote hatao
                dq.pop()
            dq.append(i)                            # naya daalo
            if dq[0] < i - k + 1:                   # bahar wala hatao
                dq.popleft()
            if i >= k - 1:                          # max likho
                ans.append(nums[dq[0]])

        return ans