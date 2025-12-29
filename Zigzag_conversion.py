class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        direction = 1  # 1 = down, -1 = up 

        for ch in s:
            rows[currentRow] += ch

            # change direction at top or bottom
            if currentRow == 0:
                direction = 1
            elif currentRow == numRows - 1:
                direction = -1

            currentRow += direction

        return "".join(rows)

