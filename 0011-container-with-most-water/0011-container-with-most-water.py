class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        stick = 0
        width = 0
        while start < end:
            stick = min(height[start], height[end])
            width = max((end - start) * stick, width)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return width