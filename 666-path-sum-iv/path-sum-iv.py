class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        root = Node(nums[0]-110)
        h = {}
        def dfs(cur, curDepth, depth, pos, val):
            if curDepth == depth:
                return Node(val)
            if pos%2 == 1:
                cur.left = dfs(cur, curDepth + 1, depth, pos, val)
            else:
                cur.left = dfs(cur, curDepth + 1, depth, pos, val)
            return cur

        for n in nums:
            s = str(n)
            depth = int(s[0])
            pos = int(s[1])
            val = int(s[2])
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