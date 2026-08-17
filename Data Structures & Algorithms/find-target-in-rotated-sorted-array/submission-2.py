class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2 or nums[0] < nums[-1]:
            return nums.index(target) if target in nums else -1
        l = 0
        m = len(nums) // 2
        r = len(nums) - 1
        if nums[l] <= target and target <= nums[m]:
            return self.search(nums[:(m+1)], target)
        elif nums[m] <= target and target <= nums[r]:
            return m + self.search(nums[m:], target) if self.search(nums[m:], target) != -1 else -1
        elif (target >= nums[l] or target <= nums[m]) and nums[l] > nums[m]:
            return self.search(nums[:(m+1)], target)
        else:
            return m + self.search(nums[m:], target) if self.search(nums[m:], target) != -1 else -1
