class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_pro = []
        right_pro = []
        for i in range(0, len(nums)):
            if i == 0:
                left_pro.append(1)
            else:
                left_pro.append(left_pro[i - 1] * nums[i - 1])
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_pro.append(1)
            else:
                right_pro.append(right_pro[-1] * nums[i + 1])              # right_pro[-1] == last element in present array like [4],[5]    
        right_pro.reverse()
        for i in range(len(nums)):
            output.append(left_pro[i] * right_pro[i])
        return output