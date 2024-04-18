def searchMatrix(self, matrix, target):
    for r in range(len(matrix)):
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            c = (left + right) // 2
            if matrix[r][c] > target:
                right = c - 1
            elif matrix[r][c] < target:
                left = c + 1
            else:
                return True
    return False
  
