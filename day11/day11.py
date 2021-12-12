# Calculate total number of octopus flashes
octopus_matrix = [list(map(int, list(line.strip()))) for line in open("day11.input")]
def part1():
    total_flashes = 0
    steps = 100

    for _ in range(1,steps+1):
        flashed = set()
        # Increment every octopus
        for i in range(len(octopus_matrix)):
            for j in range(len(octopus_matrix[i])):
                octopus_matrix[i][j] += 1

        # Flash all octopuses with energy > 9
        for i in range(len(octopus_matrix)):
            for j in range(len(octopus_matrix[i])):
                if octopus_matrix[i][j] > 9 and (i,j) not in flashed:
                    flashed.add((i,j))
                    flashed.union(flash_octopus(i,j,flashed))
        
        # Set all octopuses that flashed to 0
        for coordinate in flashed:
            octopus_matrix[coordinate[0]][coordinate[1]] = 0

        total_flashes += len(flashed)
    print(f"There were {total_flashes} total flashes")

# Recursively flash and increment all neighbors
def flash_octopus(i,j, flashed):
    coordinates = [
        [i-1,j], [i+1,j], [i,j-1], [i,j+1],  # horizontal/vertical
        [i-1,j-1], [i-1,j+1], [i+1,j-1], [i+1,j+1]  # diagonal
    ]

    for coordinate in coordinates:
        x, y = coordinate
        # Protect against out of bounds
        if x >= 0 and y >= 0 and x < len(octopus_matrix) and y < len(octopus_matrix): 
            octopus_matrix[x][y] += 1
            if octopus_matrix[x][y] > 9 and (x,y) not in flashed:
                flashed.add((x,y)) 
                flashed.union(flash_octopus(x,y,flashed))
    return flashed


# Increase all neighbors horizontal, vertical, diagonal
def increase_neighbors(i,j,octopus_matrix):
    
    # Increase vertically and horizontally
    if i-1 > 0: octopus_matrix[i-1][j] += 1
    if i+1 > 0: octopus_matrix[i+1][j] += 1
    if j-1 > 0: octopus_matrix[i][j-1] += 1
    if i+1 > 0: octopus_matrix[i][j+1] += 1

    # Increase diagonally
    if i-1 > 0 and j-1 > 0: octopus_matrix[i-1][j-1] += 1
    if i-1 > 0 and j+1 > 0: octopus_matrix[i-1][j+1] += 1
    if i+1 > 0 and j-1 > 0: octopus_matrix[i+1][j-1] += 1
    if i+1 > 0 and j+1 > 0: octopus_matrix[i+1][j+1] += 1
    return octopus_matrix

# Determine the step when all octopuses flash, very similar to part1
def part2():
    all_flashed = False
    step = 0
    ALL_FLASHED_MATRIX = [[0] * 10]*10 
    while not all_flashed:
        flashed = set()
        # Increment every octopus
        for i in range(len(octopus_matrix)):
            for j in range(len(octopus_matrix[i])):
                octopus_matrix[i][j] += 1

        # Flash all octopuses with energy > 9
        for i in range(len(octopus_matrix)):
            for j in range(len(octopus_matrix[i])):
                if octopus_matrix[i][j] > 9 and (i,j) not in flashed:
                    flashed.add((i,j))
                    flashed.union(flash_octopus(i,j,flashed))
        
        # Set all octopuses that flashed to 0
        for coordinate in flashed:
            octopus_matrix[coordinate[0]][coordinate[1]] = 0

        if octopus_matrix == ALL_FLASHED_MATRIX:
            all_flashed = True
            print(f"Step {step} all lights flashed")
        step +=1




# part1()
part2()