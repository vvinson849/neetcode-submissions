class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return min(nums)
        l = 0
        m = len(nums) // 2
        r = len(nums) - 1
        if nums[l] > nums[r]:
            if nums[l] < nums[m]:
                return self.findMin(nums[m:])
            else:
                return self.findMin(nums[l:(m+1)])
        else:
            return nums[0]
