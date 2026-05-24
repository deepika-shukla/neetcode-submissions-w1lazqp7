class Solution:
    def getSquares(self, n):
        listOfSquares = []
        for i in range(1, n+1):
            if i*i <= n:
                listOfSquares.append(i*i)
            else:
                break
        return listOfSquares

    def numSquares(self, n: int) -> int:
        listOfSquares = self.getSquares(n)
        print(listOfSquares)
    
        dp = [1+n] * (1+n)
        dp[0] = 0

        for i in range(1, n+1):
            for s in listOfSquares:
                if (i-s) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-s])
        return dp[n]