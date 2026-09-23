class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        T = [1, 2, 3]
        i = 3
        while len(T) < n:
            T.append(T[i-1] + T[i-2])
            i += 1
        return T[-1]
        