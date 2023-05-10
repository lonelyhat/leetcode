class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 0
        for i in range(k+1):
            n = n*10 +1
            if (n%k)==0:
                return i+1
        return -1