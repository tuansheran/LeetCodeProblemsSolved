def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        current_row = 0
        step = 1
        for char in s:
            rows[current_row].append(char)
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1
            current_row += step
        return ''.join(''.join(row) for row in rows)

