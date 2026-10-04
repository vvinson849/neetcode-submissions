class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            offset = i if i == offset * 2 else offset
            dp[i] = 1 + dp[i - offset]
        return dp
        