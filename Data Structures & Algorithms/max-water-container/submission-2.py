class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        f, b = 0, len(heights) - 1
        while(f < b):
            temp = (b-f)*min(heights[f], heights[b])
            area = max(temp, area)
            if heights[f] < heights[b]:
                f+=1
            else:
                b-=1
        return area
