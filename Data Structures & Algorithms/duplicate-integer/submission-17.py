class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cop = set(nums)
        if len(cop) == len(nums):
            return False
        return True
