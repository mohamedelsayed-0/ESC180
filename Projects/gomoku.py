"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 16, 2025
"""

# pls ignore when i do type: ignore its so vs code will stop being so incredibly annoying with the yellow lines
#real commments r when i use """something
IMPORTANT NOTE: I did not get 100% on this project but failed some cases relating to winning with more or less than 5 pieces (didn't read it properly"""
#sorry for making ur life harder ta

"""returns true if no stones on board"""
def is_empty(board): 
    for row in board:
        for cell in row:
            if cell != " ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x): #open, semiopen, closed
    col = board[y_end][x_end]
    
    """start position"""
    y_start = y_end - (length - 1) * d_y
    x_start = x_end - (length - 1) * d_x
    
    """check b4 start"""
    y_before = y_start - d_y
    x_before = x_start - d_x
    
    """check after doing"""
    y_after = y_end + d_y
    x_after = x_end + d_x
    
    """within bounds and empty"""
    before_open = False
    after_open = False
    
    if 0 <= y_before < len(board) and 0 <= x_before < len(board[0]): # type: ignore
        if board[y_before][x_before] == " ":
            before_open = True
    
    if 0 <= y_after < len(board) and 0 <= x_after < len(board[0]): # type: ignore
        if board[y_after][x_after] == " ":
            after_open = True
    
    if before_open and after_open:
        return "OPEN"
    elif before_open or after_open:
        return "SEMIOPEN"
    else:
        return "CLOSED"

    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    
    y = y_start
    x = x_start
    current_length = 0
    
    while 0 <= y < len(board) and 0 <= x < len(board[0]): # type: ignore
        if board[y][x] == col:
            current_length += 1
        else:
            if current_length == length:
                y_end = y - d_y
                x_end = x - d_x
                boundedness = is_bounded(board, y_end, x_end, length, d_y, d_x)
                if boundedness == "OPEN":
                    open_seq_count += 1
                elif boundedness == "SEMIOPEN":
                    semi_open_seq_count += 1
            current_length = 0
        
        y += d_y
        x += d_x
    
    if current_length == length:
        y_end = y - d_y
        x_end = x - d_x
        boundedness = is_bounded(board, y_end, x_end, length, d_y, d_x)
        if boundedness == "OPEN":
            open_seq_count += 1
        elif boundedness == "SEMIOPEN":
            semi_open_seq_count += 1
    
    return open_seq_count, semi_open_seq_count

    
def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0
    board_size = len(board) #type: ignore
    
    """horizontal""" 
    for y in range(board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, y, 0, length, 0, 1)
        open_seq_count += open_c
        semi_open_seq_count += semi_c
    
    """vertical"""
    for x in range(board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, 0, x, length, 1, 0)
        open_seq_count += open_c
        semi_open_seq_count += semi_c

    """diagonal (1, 1) """
    for x in range(board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, 0, x, length, 1, 1)
        open_seq_count += open_c
        semi_open_seq_count += semi_c

    """from left column (excluding top-left corner)"""
    for y in range(1, board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, y, 0, length, 1, 1)
        open_seq_count += open_c
        semi_open_seq_count += semi_c
    
    """diagonal (1, -1)"""
    for x in range(board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, 0, x, length, 1, -1)
        open_seq_count += open_c
        semi_open_seq_count += semi_c

    """from right column (excluding top-right corner)"""
    for y in range(1, board_size): #type: ignore
        open_c, semi_c = detect_row(board, col, y, board_size - 1, length, 1, -1)
        open_seq_count += open_c
        semi_open_seq_count += semi_c
    return open_seq_count, semi_open_seq_count


"""find most optimal move for black"""
def search_max(board): 
    best_score = None #type: ignore
    move_y, move_x = 0, 0
    
    for y in range(len(board)): #type: ignore
        for x in range(len(board[0])): #type: ignore
            if board[y][x] == " ": #type: ignore

                """attempt placing black"""

                board[y][x] = "b" #type: ignore
                current_score = score(board) #type: ignore

                """undo"""

                board[y][x] = " " #type: ignore
                
                if best_score is None or current_score > best_score:
                    best_score = current_score
                    move_y, move_x = y, x
    
    return move_y, move_x #type: ignore

    
def score(board): #type: ignore
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6): #type: ignore
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


"""current status of the game"""

def is_win(board): 
    """check for 5 in a row for both colors"""

    for col in ["b", "w"]:

        """all possible sequences of length 5 or more"""

        for length in range(5, len(board) + 1): #type: ignore
            open_c, semi_c = detect_rows(board, col, length)
            if open_c > 0 or semi_c > 0:
                if col == "b":
                    return "Black won"
                else:
                    return "White won"
    
    """draw check"""

    for row in board:
        for cell in row:
            if cell == " ":
                return "Continue playing"
    
    return "Draw"


def print_board(board):
    s = "*"
    for i in range(len(board[0])-1): #type: ignore
        s += str(i%10) + "|" #type: ignore
    s += str((len(board[0])-1)%10) #type: ignore
    s += "*\n"
    
    for i in range(len(board)): #type: ignore
        s += str(i%10) #type: ignore
        for j in range(len(board[0])-1): #type: ignore
            s += str(board[i][j]) + "|" #type: ignore
        s += str(board[i][len(board[0])-1])  #type: ignore
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*" #type: ignore
    
    print(s) #type: ignore
    

def make_empty_board(sz):
    board = []
    for i in range(sz): #type: ignore
        board.append([" "]*sz)
    return board
                

def analysis(board):
    """check for black"""

    print("Black stones") #type: ignore
    for i in range(2, 6): #type: ignore
        open, semi_open = detect_rows(board, "b", i)
        print(f"Open rows of length {i}: {open} ") #type: ignore
        print(f"Semi-open rows of length {i}: {semi_open}") #type: ignore
    
    """check for white"""

    print("White stones")  #type: ignore
    for i in range(2, 6): #type: ignore
        open, semi_open = detect_rows(board, "w", i)
        print(f"Open rows of length {i}: {open}") #type: ignore
        print(f"Semi-open rows of length {i}: {semi_open}") #type: ignore
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board) #type: ignore
    board_width = len(board[0]) #type: ignore
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x)) #type: ignore
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
        
        print("Your move:") #type: ignore
        move_x = int(input("x coord: ")) #type: ignore
        move_y = int(input("y coord: ")) #type: ignore
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length): #type: ignore
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED") #type: ignore
    else:
        print("TEST CASE for is_empty FAILED") #type: ignore

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED") #type: ignore
    else:
        print("TEST CASE for is_bounded FAILED") #type: ignore


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED") #type: ignore
    else:
        print("TEST CASE for detect_row FAILED") #type: ignore

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED") #type: ignore
    else:
        print("TEST CASE for detect_rows FAILED") #type: ignore

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED") #type: ignore
    else:
        print("TEST CASE for search_max FAILED") #type: ignore

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

  
            
if __name__ == '__main__':
    easy_testset_for_main_functions()
    some_tests()
    play_gomoku(8)
