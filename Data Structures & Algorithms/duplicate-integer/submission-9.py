class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gadang = set()
        for i in nums:
            if i in gadang:
                return True
            gadang.add(i)  
        return False
