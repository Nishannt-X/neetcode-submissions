class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        def check(x):
            n=len(x)
            if n==1:
                return x[0]
            dp=[0]*n

            dp[0]=x[0]
            dp[1]=max(x[0],x[1])

            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+x[i])
            return dp[-1]
        return max(check(nums[1:]),check(nums[:-1]))
        