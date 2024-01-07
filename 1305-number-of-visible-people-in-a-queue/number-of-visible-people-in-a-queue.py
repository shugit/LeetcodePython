class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            c = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                c += 1 
            res[i] = c if not stack else c + 1
            stack.append(heights[i])
        return res