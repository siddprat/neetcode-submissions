class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f, b = 0, (len(numbers) - 1)
        while f < b:
            if numbers[f] + numbers[b] == target:
                return [f + 1, b + 1]
            elif numbers[f] + numbers[b] < target:
                f+=1
            else:
                b -=1