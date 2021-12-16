# Fold the paper once and see how many dots there are
def part1():
    grid = fold_paper(True)
    count_dots = sum(point>0 for point in [point for row in grid for point in row])
    print(f"There are {count_dots} dots")

# Do all the folds then print the points
def part2():
    grid = fold_paper(False)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                print(" ", end="")
            else:
                print("|", end="")
        print()

# Helper function for parts 1 (one fold) and 2 (all folds)
def fold_paper(fold_one):
    points = [list(map(int, line.strip().split(','))) for line in open('day13.input') if 'fold' not in line and line != '\n']
    fold_instructions = [line.strip().split("fold along ")[1].split('=') for line in open('day13.input') if 'fold' in line]

    # Get column and row sizes based on first folds for x and y
    columns = 2 * next(int(fold[1]) for fold in fold_instructions if fold[0] == 'x') + 1
    rows = 2 * next(int(fold[1]) for fold in fold_instructions if fold[0] == 'y') + 1
    if fold_one:
        fold_instructions = fold_instructions[:1]
    grid = [[0 for i in range(columns)] for j in range(rows)]

    for point in points:
        y,x = point
        grid[x][y] = 1

    for instruction in fold_instructions:
        direction = instruction[0]
        position = int(instruction[1])

        if direction == 'y': # fold in half horizontally
            grid_past_fold = grid[position+1:]
            grid = grid[:position]
            grid_past_fold.reverse() # lets flip it so its easy to add

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j] = grid[i][j] + grid_past_fold[i][j]
        elif direction == 'x': # fold in half vertically
            for i in range(len(grid)):
                grid_line = grid[i]
                grid_line_past_fold = grid_line[position+1:]
                grid_line_past_fold.reverse()
                grid_line_before_fold = grid_line[:position]
                grid[i] = [line1 + line2 for line1, line2 in zip(grid_line_before_fold, grid_line_past_fold)]
    return grid


part1()
part2()