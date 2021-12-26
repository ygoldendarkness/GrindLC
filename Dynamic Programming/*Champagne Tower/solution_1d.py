class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0 for i in range(query_row + 1)]
        
        dp[0] = poured
        
        for row in range(1, query_row + 1):
            nextDp = [0 for i in range(query_row + 1)]
            for col in range(0, row + 1):
                dp[col] -= 1
                if dp[col] > 0:
                    nextDp[col] += dp[col] / 2
                if col > 0:
                    if dp[col-1] > 0:
                        nextDp[col] += dp[col-1] / 2
            dp = nextDp
        
        if dp[query_glass] > 1:
            return 1.0
        
        return dp[query_glass]