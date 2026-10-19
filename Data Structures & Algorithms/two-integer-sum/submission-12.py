class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            x = target - i
            cop = nums.copy()
            cop.remove(i)
            if x in cop:
                return [nums.index(i), cop.index(x) + 1]
            