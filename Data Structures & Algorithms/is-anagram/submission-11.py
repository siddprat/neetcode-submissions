class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        for i in s:
            dicts[i] = dicts.get(i, 0) + 1
        dictt = {}
        for j in t:
            dictt[j] = dictt.get(j, 0) + 1
        if dicts == dictt: return True
        return False
        