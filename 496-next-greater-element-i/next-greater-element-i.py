class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        h = {}
        for n in nums2[::-1]:
            while stack and stack[-1] < n:
                stack.pop()
            h[n] = stack[-1] if stack else -1
            stack.append(n)
        return [h[n] for n in nums1]