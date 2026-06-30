class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]
        letters = tuple("abcdefghijklmnopqrstuvwxyz")
        map = {}
        for i in range(len(strs)):
            key = [0] * 26
            for char in strs[i]:
                key[letters.index(char)] += 1
            key = tuple(key)
            if key not in map:
                map[key] = []
            map[key].append(i)
        return [[strs[i] for i in map[key]] for key in map]
