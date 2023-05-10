class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if (k%2==0 or k%5 ==0):
            return -1
        n = 0
        for i in range(k):
            n = n*10 +1
            if (n%k)==0:
                return i+1
        return -1