def check_square_board(board: str) -> int:
    """Check if the board is valid square if valid return size of the board if not return 0"""

    if not board:
        return 0

    lines = board.split("\n")
    size = len(lines[0])

    # Check that all line have the same length
    valid = all(len(line) == size for line in lines)

    return size if valid else 0


def get_pos(board: str, piece: str) -> tuple[int, int] | None:
    """Get the position of the  in the board return (x, y) if found else None"""

    lines = board.split("\n")

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == piece:
                return (x, y)

    return None


def check_corner(board: str, size: int, char: str) -> tuple[bool, str]:
    """Check if the piece is in the corner of the board"""
    pos = get_pos(board, char)
    if not pos:
        return False

    if pos == (0, 0):
        return True, "tl"
    elif pos == (0, size - 1):
        return True, "bl"
    elif pos == (size - 1, 0):
        return True, "tr"
    elif pos == (size - 1, size - 1):
        return True, "br"

    return False, ""


def get_possible_pawn_moves(
    board: str, pos: tuple[int, int], size: int
) -> list[tuple[int, int]]:
    """Get all possible moves for a pawn from the given position, PAWN can only move Northeast and Northwest"""

    x, y = pos

    is_corner, corner_side = check_corner(board, size, "P")

    if not is_corner:
        return [(x - 1, y - 1), (x + 1, y - 1)]

    if y == 0:
        return []
    elif corner_side == "bl":
        return [(x + 1, y - 1)]
    elif corner_side == "br":
        return [(x - 1, y - 1)]


def get_possible_rook_moves(
    board: str, pos: tuple[int, int], size: int
) -> list[tuple[int, int]]:
    """Get all possible moves for a ROOK from the given position"""
    x, y = pos
    moves = []

    for i in range(size):
        if i != x:
            moves.append((i, y))
        if i != y:
            moves.append((x, i))

    return moves


def ray(
    board: str, x0: int, y0: int, dx: int, dy: int, size: int
) -> list[tuple[int, int]]:
    """Generate moves in a direction until hitting the first piece or edge"""
    moves = []
    x, y = x0, y0
    while True:
        x += dx
        y += dy
        if not (0 <= x < size and 0 <= y < size):
            break
        moves.append((x, y))
        if board.split("\n")[y][x] != ".":
            break
    return moves


def get_possible_bishop_moves(
    board: str, pos: tuple[int, int], size: int
) -> list[tuple[int, int]]:
    """Bishop moves diagonally in 4 directions until it hits the first piece and then stops"""
    x0, y0 = pos
    moves = []
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        moves.extend(ray(board, x0, y0, dx, dy, size))
    return moves


def get_possible_queen_moves(
    board: str, pos: tuple[int, int], size: int
) -> list[tuple[int, int]]:
    """Queen = Rook + Bishop (8 directions) until hitting the first piece, then stop"""
    x0, y0 = pos
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for dx, dy in directions:
        moves.extend(ray(board, x0, y0, dx, dy, size))
    return moves


def checkmate(board: str) -> str:
    '''Check if KING got checkmate return "Success" if true else "Fail"'''

    size = check_square_board(board)
    if not size:
        return "Fail"

    king_pos = get_pos(board, "K")
    if not king_pos:
        return "Fail"

    all_moves: list[tuple[int, int]] = []

    if "P" in board:
        ppos = get_pos(board, "P")
        if ppos:
            all_moves.extend(get_possible_pawn_moves(board, ppos, size))

    if "R" in board:
        rpos = get_pos(board, "R")
        if rpos:
            all_moves.extend(get_possible_rook_moves(board, rpos, size))

    if "B" in board:
        bpos = get_pos(board, "B")
        if bpos:
            all_moves.extend(get_possible_bishop_moves(board, bpos, size))

    if "Q" in board:
        qpos = get_pos(board, "Q")
        if qpos:
            all_moves.extend(get_possible_queen_moves(board, qpos, size))

    # for debug
    # for y in range(size):
    #     for x in range(size):
    #         if (x, y) in all_moves:
    #             print("X", end="")
    #         else:
    #             print(".", end="")
    #     print()

    return "Success" if king_pos in all_moves else "Fail"
