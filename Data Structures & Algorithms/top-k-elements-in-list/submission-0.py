class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
        return [item[0] for item in sorted(map.items(), key=lambda item: item[1], reverse=True)[0:k]]
        