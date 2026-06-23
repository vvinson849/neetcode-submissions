class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        maps = {}; mapt = {}
        for cs, ct in zip(s, t):
            if cs not in maps: maps[cs] = 0
            if ct not in maps: maps[ct] = 0
            if cs not in mapt: mapt[cs] = 0
            if ct not in mapt: mapt[ct] = 0
            maps[cs] += 1
            mapt[ct] += 1
        for c in maps.keys():
            if maps[c] != mapt[c]: 
                return False
        return True
        