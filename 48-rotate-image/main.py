def rotate(self, matrix: List[List[int]]) -> None:
    left, right = 0, len(matrix) -1

    while left < right:
      for i in range(right - left):
        top, bot = left, right

        # temp store top left
        top_left = matrix[top][left + i]

        matrix[top][left + i] = matrix[bot - i][left]
        matrix[bot - i][left] = matrix[bot][right - i]
        matrix[bot][right - i] = matrix[top + i][right]
        matrix[top + i][right] = top_left  # and put top left back

      right -= 1
      left += 1
