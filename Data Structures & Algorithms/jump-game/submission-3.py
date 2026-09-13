class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        if nums[0] == 0: return False
        n = len(nums)
        goal = n - 1
        curr_pos = goal - 1
        while True:
            if nums[curr_pos] >= goal - curr_pos:
                goal = curr_pos
            if goal == 0:
                return True
            if curr_pos < 0:
                return False
            curr_pos -= 1
        return False
        