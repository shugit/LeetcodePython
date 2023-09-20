class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair:(index, height)
        # heights.append(0)
        max_area = 0
        for i, h in enumerate(heights):
            start_i = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                max_area = max(max_area, (i-prev_i) * prev_h)
                start_i = prev_i
            stack.append([start_i,h])
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area