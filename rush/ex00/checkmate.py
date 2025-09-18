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
        print(i, x, y)
        if i != x:
            moves.append((i, y))
        if i != y:
            moves.append((x, i))

    return moves


def checkmate(board: str) -> str:
    '''Check if KING got checkmate return "Success" if true else "Fail"'''

    size = check_square_board(board)

    print(board)

    if not size:
        return "Fail"

    king_pos = get_pos(board, "K")
    x, y = king_pos

    print("King pos:", king_pos)
    # if not king_pos:
    #     return ""

    all_moves = []

    if "P" in board:
        moves = get_possible_pawn_moves(board, get_pos(board, "P"), size)

        for y in range(size):
            for x in range(size):
                if (x, y) in moves:
                    print("X", end="")
                else:
                    print(".", end="")
            print()

        all_moves.extend(moves)

    if "R" in board:
        moves = get_possible_rook_moves(board, get_pos(board, "R"), size)
        
        # for debug
        for y in range(size):
            for x in range(size):
                if (x, y) in moves:
                    print("X", end="")
                else:
                    print(".", end="")
            print()

        all_moves.extend(moves)

    print(all_moves) # for debug

    for y in range(size):
        for x in range(size):
            if (x, y) in all_moves:
                print("X", end="")
            else:
                print(".", end="")
        print()

    if king_pos in all_moves:
        return "Success"

    return "Fail"


