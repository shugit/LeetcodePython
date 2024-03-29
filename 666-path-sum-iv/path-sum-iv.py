class Solution:
    def pathSum(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            depth = n//100
            pos = (n - depth*100)//10
            val = n % 10
            h[(depth-1, pos-1)] = val
        res = 0
        def dfs(curSum, depth, pos):
            nonlocal res
            val = h[(depth, pos)]
            left = (depth+1, pos*2)
            right = (depth+1, pos*2+1)
            if left in h and right in h:
                 dfs(curSum + val, depth+1, pos*2)
                 dfs(curSum + val, depth+1, pos*2+1)
            elif left in h:
                dfs(curSum + val, depth+1, pos*2)
            elif right in h:
                dfs(curSum + val, depth+1, pos*2+1)
            else:
                res += (curSum+val)
                return 
        dfs(0,0,0)
        return res