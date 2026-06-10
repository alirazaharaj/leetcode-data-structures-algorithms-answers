class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}
        for i in range(len(nums)):
            if nums[i] in top:
                top[nums[i]] += 1
            else:
                top[nums[i]] = 1
        top = sorted(top.items(), key=lambda x: x[1], reverse=True)
        return sorted([top[i][0] for i in range(k)])