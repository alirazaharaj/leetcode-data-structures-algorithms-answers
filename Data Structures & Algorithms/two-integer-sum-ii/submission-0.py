class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            check = target - numbers[i]
            if check in numbers and numbers.index(check) != i:
                return [i + 1, numbers.index(check) + 1]