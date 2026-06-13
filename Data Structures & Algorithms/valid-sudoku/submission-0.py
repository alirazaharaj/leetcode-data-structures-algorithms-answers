class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        def has_duplicate(arr):
            seen = set()
            for char in arr:
                if char != ".":
                    if char in seen:
                        return True
                    seen.add(char)
            return False

        # Rule 1: Saari Rows check karo
        for r in range(9):
            current_row = board[r]
            if has_duplicate(current_row):
                return False

        # Rule 2: Saare Columns check karo
        for c in range(9):
            current_col = [board[r][c] for r in range(9)]
            if has_duplicate(current_col):
                return False

        # Rule 3: Saare 3x3 Boxes check karo
        current_box = []
        for i in range(9):
            for j in range(9):
                # Formula mention in hints to get the correct row and column for each box
                r = (i // 3) * 3 + (j // 3)
                c = (i % 3) * 3 + (j % 3)

                current_box.append(board[r][c])

                if j == 8:
                    if has_duplicate(current_box):
                        return False
                    current_box = []

        return True