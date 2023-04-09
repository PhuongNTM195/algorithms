def is_valid(board, row, col, n):
    # Kiểm tra xem vị trí (row, col) có hợp lệ không
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row, n):
    # Nếu đã đặt quân hậu vào hàng cuối cùng, trả về True
    if row == n:
        return True

    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if solve(board, row+1, n):
                return True
            board[row][col] = 0

    return False


def print_board(board):
    for row in board:
        print(row)


# Hàm chính để giải bài toán Quân Hậu
def n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]
    if solve(board, 0, n) == False:
        print("Không tìm thấy giải pháp")
        return False

    print_board(board)
    return True


# Ví dụ về bàn cờ kích thước 8x8
n_queens(8)