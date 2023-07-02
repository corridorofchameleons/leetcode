def maxArea(heights: list) -> int:
    max_vol = 0
    for i in range(len(heights)):
        for j in range(len(heights) - 1, i, -1):
            if heights[j] >= heights[len(heights) - 1]:
                vol = (j - i) * min([heights[i], heights[j]])
                if vol > max_vol:
                    max_vol = vol
    return max_vol


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
