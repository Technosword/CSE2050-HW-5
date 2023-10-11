def solve_puzzle(board, pos=0, cache=None):
    """
    Provided a board, recursively finds and returns the optimal solution to reach len(board) - 1
    :param board: Board to be solved
    :param pos: Current position (Default 0)
    :param cache: Cache of previously seen values (Default None)
    :return: Tuple of optimal solution, and number of moves needed
    """
    if cache is None:
        cache = set()
    if pos == len(board) - 1:
        return [pos], 0
    if pos in cache:
        return None, None
    fw = (pos + board[pos])
    bw = (pos - board[pos])
    cache.add(pos)
    forward_solu, forward_len, backward_solu, backward_len = None, None, None, None

    if fw < len(board):
        forward_solu, forward_len = solve_puzzle(board, pos=fw, cache=cache)

    if bw > 0:
        backward_solu, backward_len = solve_puzzle(board, pos=bw, cache=cache)

    forward_len = float('inf') if forward_len is None else forward_len
    backward_len = float('inf') if backward_len is None else backward_len

    if forward_len <= backward_len:
        if forward_solu is None:
            return None, None
        forward_solu.insert(0, pos)
        return forward_solu, forward_len + 1
    if backward_solu is None:
        return None, None
    backward_solu.insert(0, pos)
    return backward_solu, backward_len + 1


if __name__ == "__main__":
    print(solve_puzzle([1, 3, 10, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1]))
