class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(amount):
            if amount==0:
                return 0
            ans=float('inf')

            if amount in memo:
                return memo[amount]

            count=0
            for i in coins:
                if i<=amount:
                    count=dfs(amount-i)
                    count+=1
                    ans=min(ans, count)
            memo[amount]=ans
            return ans
        res=dfs(amount) 
        return res if res!=float('inf') else -1