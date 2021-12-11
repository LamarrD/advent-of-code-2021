from functools import reduce
# Find all point is a low points, points where all adjacent numbers are greater
def part1():
    number_matrix = [ list(map(int, list(line.strip()))) for line in open("day9.input").readlines()]
    low_points = get_low_points(number_matrix)
    answer = sum([low_point[0]+1 for low_point in low_points])
    print(f"The sum of the lowest points is {answer}")

def get_low_points(number_matrix):
    # Get the low points (value and coordinate, ex: 0, [0,9])
    low_points = []
    for i in range(len(number_matrix)):
        for j in range(len(number_matrix[i])):
            neighbors = []
            number = number_matrix[i][j]
            if i-1 >= 0: neighbors.append(number_matrix[i-1][j])
            if j-1 >= 0: neighbors.append(number_matrix[i][j-1])
            if i+1 < len(number_matrix): neighbors.append(number_matrix[i+1][j])
            if j+1 < len(number_matrix[i]): neighbors.append(number_matrix[i][j+1])
            if (all(neighbor > number for neighbor in neighbors)):
                low_points.append([number, [i,j]])
    return low_points
    
# Recursively get neighbors (stop at 9s)
all_neighbors = []
def get_neighbors(i, j, number_matrix):
    global all_neighbors
    neighbors = [] 
    if i-1 >= 0 and number_matrix[i-1][j] != 9 and [i-1,j] not in all_neighbors:
        neighbors.append([number_matrix[i-1][j], [i-1,j]])
    if j-1 >= 0 and number_matrix[i][j-1] != 9 and [i,j-1] not in all_neighbors:
        neighbors.append([number_matrix[i][j-1], [i,j-1]])
    if i+1 < len(number_matrix) and number_matrix[i+1][j] != 9 and [i+1,j] not in all_neighbors:
        neighbors.append([number_matrix[i+1][j], [i+1,j]])
    if j+1 < len(number_matrix[i]) and number_matrix[i][j+1] != 9 and [i,j+1] not in all_neighbors:
        neighbors.append([number_matrix[i][j+1], [i,j+1]])

    all_neighbors += [neighbor[1] for neighbor in neighbors]
    for neighbor in neighbors:
        i,j = neighbor[1]
        neighbors += get_neighbors(i, j, number_matrix)
    return neighbors

# Now we need to find the basins, which is everything (except 9s) connected to a low point
def part2():
    global all_neighbors
    number_matrix = [ list(map(int, list(line.strip()))) for line in open("day9.input").readlines()]
    low_points = get_low_points(number_matrix)
    all_neighbors += [low_point[1] for low_point in low_points]

    basins = []
    # Reach out from each low_point to see how big the basin is
    for low_point in low_points:
        i,j = low_point[1]
        neighbors = get_neighbors(i, j, number_matrix) + [low_point]
        basins.append(len(neighbors))
    
    answer = reduce((lambda x, y: x * y), sorted(basins)[-3:])
    print(f"The product of the largest basins is {answer}")

part1()
part2()