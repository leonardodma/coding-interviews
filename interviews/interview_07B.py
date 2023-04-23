def is_valid_placement(queens: list[int], row: int, col: int) -> bool:
    for i, queen in enumerate(queens):
        if queen == col or abs(i - row) == abs(queen - col):
            return False

    return True


def place_queens(n: int) -> list[list[int]]:
    if n in {0, 2, 3}:
        return []

    if n == 1:
        return [[0]]

    solutions = []

    def place_queens_recursive(queens: list[int], row: int):
        if row == n:
            solutions.append(queens)
            return

        for col in range(n):
            is_valid = is_valid_placement(queens, row, col)
            if is_valid:
                place_queens_recursive(queens + [col], row + 1)

    place_queens_recursive([], 0)

    return solutions
