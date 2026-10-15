class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            opp = target - num
            if opp in nums:
                if nums.index(opp) != i:
                    return sorted([i, nums.index(opp)])