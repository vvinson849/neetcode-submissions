class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dfs = [0] * len(nums)
        dfs[0] = nums[0]
        dfs[1] = max(nums[0], nums[1])
        for i in range(2, len(dfs)):
            dfs[i] = max(dfs[i-2] + nums[i], dfs[i-1])
        return dfs[-1]
        