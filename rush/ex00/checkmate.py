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


def get_possible_pawn_moves(
    board: str, pos: tuple[int, int], size: int
) -> list[tuple[int, int]]:
    """Get all possible moves for a pawn from the given position, PAWN can only move Northeast and Northwest"""

    x, y = pos

    is_corner, corner_side = check_corner(board, size, "P")

    if not is_corner:
        return [(x - 1, y - 1), (x + 1, y - 1)]

    if corner_side in ("tl", "tr"):
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

    is_corner, corner_side = check_corner(board, size, "R")

    if not is_corner:
        # if not in corner it can move in horizontal and vertical
        for i in range(size):
            if i != x:
                moves.append((i, y))
            if i != y:
                moves.append((x, i))
    else:
        if corner_side == "tl":  # move down and right
            for i in range(1, size):
                moves.append((i, 0))
                moves.append((0, i))
        elif corner_side == "tr":  # move down and left
            for i in range(size - 1):
                moves.append((i, size - 1))
                moves.append((size - 1, i))
        elif corner_side == "bl":  # move up and right
            for i in range(1, size):
                moves.append((i, size - 1))
                moves.append((size - 1, i))
        elif corner_side == "br":  # move up and left
            for i in range(size - 1):
                moves.append((i, 0))
                moves.append((0, i))

    return moves


def checkmate(board: str) -> str:
    '''Check if KING got checkmate return "Success" if true else "Fail"'''

    size = check_square_board(board)

    if not size:
        return "Fail"

    king_pos = get_pos(board, "K")

    if not king_pos:
        return ""

    all_moves = []

    if "P" in board:
        all_moves.extend(get_possible_pawn_moves(get_pos(board, "P")))

    if "R" in board:
        all_moves.extend(get_possible_rook_moves(get_pos(board, "R")))

    if king_pos in all_moves:
        return "Success"

    return "Fail"
