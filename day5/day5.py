# Determine how many times lines overlap
def part1():
    overlaps = 0
    lines = [[ pair.split(',') for pair in line.strip().split(' -> ')] for line in open('day5.input')]
    grid = [[0] * 1000 for _ in range(1000)] # 2x2 representation of the grid

    for line in lines:
        x1, y1 = map(int, line[0])
        x2, y2 = map(int, line[1])
        if y1 == y2: # horizontal line (same y's)
            if x1 < x2:
                grid[y1][x1:x2+1] = [i+1 for i in grid[y1][x1:x2+1]]
            elif x1 > x2:
                grid[y1][x2:x1+1] = [i+1 for i in grid[y1][x2:x1+1]]
        elif x1 == x2: # vertical line (same x's)
            for i in range(y1, y2+1) if y1<y2 else range(y2,y1+1):
                grid[i][x1] += 1

    # Kind of dense, but we're just counting all the places lines overlap
    overlaps = sum(sum(1 for _ in row if i > 1) for row in grid)    
    print(f"{overlaps} lines overlap")

# Now same thing but add diags
def part2():
    overlaps = 0
    lines = [[ pair.split(',') for pair in line.strip().split(' -> ')] for line in open('day5.input')]
    grid = [[0] * 1000 for i in range(1000)] # 2x2 representation of the grid

    for line in lines:
        x1, y1 = map(int, line[0])
        x2, y2 = map(int, line[1])
        if y1 == y2: # horizontal line (same y's)
            if x1 < x2:
                grid[y1][x1:x2+1] = [i+1 for i in grid[y1][x1:x2+1]]
            elif x1 > x2:
                grid[y1][x2:x1+1] = [i+1 for i in grid[y1][x2:x1+1]]
        elif x1 == x2: # vertical line (same x's)
            for i in range(y1, y2+1) if y1<y2 else range(y2,y1+1):
                grid[i][x1] += 1
        elif abs((y2-y1)/(x2-x1)) == 1:
            if x2>x1:
                for i in range(x2-x1+1):
                    grid[y2+i if y2<y1 else y2-i][x2+i if x2<x1 else x2-i] += 1
            else: 
                for i in range(x1-x2+1):
                    grid[y2+i if y2<y1 else y2-i][x2+i if x2<x1 else x2-i] += 1
                    pass


    # Kind of dense, but we're just counting all the places lines overlap
    overlaps = sum(sum(1 for i in row if i > 1) for row in grid)    
    print(f"{overlaps} lines overlap")
    pass


part1()
part2()