class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dfs = [0] * len(nums)
        dfs[0] = nums[0]
        dfs[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dfs[i] = max(dfs[i-2] + nums[i], dfs[i-1])
        return dfs[-1]
        