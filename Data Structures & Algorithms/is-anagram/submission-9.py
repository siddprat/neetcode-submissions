class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        for i in s: 
            ds[i] = ds.get(i, 0) + 1
        dt = {}
        for j in t:
            dt[j] = dt.get(j, 0) + 1
        return ds == dt


        