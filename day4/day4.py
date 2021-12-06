# Check if a board has a winning combo
def check_board_won(board, called_numbers):
    # Check if board won horizontally
    for i in range(5):
        row = board[i*5:(i+1)*5] 
        if set(row) <= set(called_numbers):
            return board

    # Check if board won vertically
    for i in range(5):
        column = board[i::5]
        if set(column) <= set(called_numbers):
            return board

    # Check if board won diagonally 
    for i in range(5):
        diag1 = [board[0], board[6], board[12], board[19], board[24]]
        diag2 = [board[4], board[8], board[12], board[16], board[20]]
        if set(diag1) <= set(called_numbers or set(diag2) <= set(called_numbers)):
            return board

# Mark number in board
# Call each number
def call_numbers(numbers_to_call, bingo_boards):
    numbers_called = []
    winning_boards = []
    for number in numbers_to_call:
        numbers_called.append(number)
        # Check each board to see if they won
        for board in bingo_boards:
            board_won = check_board_won(board.split(','), numbers_called)
            if board_won is not None and board_won not in winning_boards:
                winning_boards.append(board_won)
                if len(winning_boards) == 100 or numbers_called == numbers_to_call:
                    return board_won, numbers_called



#BINGO
def part1():
    # Read bingo board
    # f = open("day4.input")
    lines = [line.strip() for line in open('day4.input') if line.strip() != '']
    numbers_to_call = lines[0].split(',')
    bingo_boards = []

    # Rading the boards and making them how we want
    i = 1
    while i < len(lines):
        board = lines[i:i+5]
        string_board = ','.join(board).replace('  ', ',').replace(' ', ',')
        bingo_boards.append(string_board)
        i += 5

    # Mark number in board
    # Call each number
    winning_board, called_numbers = call_numbers(numbers_to_call, bingo_boards)
    uncalled_numbers = set(winning_board) - set(called_numbers)
    score = sum(map(int,uncalled_numbers)) * int(called_numbers[-1])
    print(f"Score {score}")



    # Calculate winning score
    # FInd sum of unmarked numbers

    print("done")
    pass

def part2():
    pass


board = part1()
part2()