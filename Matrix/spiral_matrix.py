def spiralOrder(self, matrix):
        def traversal(matrix, answer, loop, rows, cols, count):
            while count < loop:
                for j in range(count, cols - count):
                    answer.append(matrix[count][j])
                for i in range(count + 1, (rows - 1) - count):
                    answer.append(matrix[i][-1 - count])
                for j in range(-1 - count, count - (cols + 1), -1):
                    answer.append(matrix[-1 - count][j])
                for i in range((rows - 2) - count, count, -1):
                    answer.append(matrix[i][count])
                count += 1
            return count

        answer = []
        count = 0
        rows = len(matrix)
        cols = len(matrix[0])

        if rows % 2 == 1 and rows == cols:
            loop = rows // 2
            count = traversal(matrix, answer, loop, rows, cols, count)
            answer.append(matrix[rows // 2][cols // 2])

        elif rows % 2 == 0 and rows == cols:
            loop = (rows / 2) - 1
            count = traversal(matrix, answer, loop, rows, cols, count)
            
            for j in range(count, cols - count):
                answer.append(matrix[count][j])
            for j in range(-1 - count, count - (cols + 1), -1):
                answer.append(matrix[-1 - count][j])

        elif rows > cols:
            loop = cols // 2
            count = traversal(matrix, answer, loop, rows, cols, count)
            if cols % 2 != 0:
                for i in range(count, rows - count):
                    answer.append(matrix[i][count])

        elif rows < cols:
            loop = rows // 2
            count = traversal(matrix, answer, loop, rows, cols, count)
            if rows % 2 != 0:
                for j in range(count, cols - count):
                    answer.append(matrix[count][j])

        return answer
