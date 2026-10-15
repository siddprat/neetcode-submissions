class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
            
        result = []
        for x in range(k):
            best = None
            for key in counts:
                if best is None or counts[key] > counts[best]:
                    best = key
            result.append(best)
            del counts[best]
        
        return result
        