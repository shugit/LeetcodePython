class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        return self.sol(heights)
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                stack.pop()
            stack.append(i)
        return stack

    def sol2(self, heights):
        stack = []
        max_height = 0
        for i in range(len(heights)-1, -1, -1):
            if max_height >= heights[i]:
                continue
            else:
                stack.append(i)
                max_height = heights[i]
        stack.reverse()
        return stack
    def sol(self, heights):
        p = []
        res = []
        for i in range(len(heights)-1, -1, -1):
            if not p or -p[0] < heights[i]:
                res.append(i)
            while p and -p[0] <= heights[i]:
                heapq.heappop(p)
            heapq.heappush(p, -heights[i])
        return sorted(res)