class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dfs1 = [0] * (n-1)
        dfs1[0] = nums[0]
        dfs1[1] = max(nums[0:2])
        dfs2 = [0] * (n-1)
        dfs2[0] = nums[1]
        dfs2[1] = max(nums[1:3])
        for i in range(2, n-1):
            dfs1[i] = max(nums[i] + dfs1[i-2], dfs1[i-1])
            dfs2[i] = max(nums[i+1] + dfs2[i-2], dfs2[i-1])
        return max(dfs1[-1], dfs2[-1])
