class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            target = -nums[i]
            cop = sorted(nums[i+1:])
            j, k = 0, (len(cop) - 1)
            while j < k:
                if cop[j] + cop[k] == target:
                    triplet = sorted([nums[i], cop[j], cop[k]])
                    if triplet not in output:
                        output.append(triplet)
                    j+=1
                    k-=1
                elif cop[j] + cop[k] < target:
                    j += 1
                else:
                    k -= 1
        return output