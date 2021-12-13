def part1():
    # Create all the connections bi-directionally
    found_paths = []
    map_lines = [ line.strip().split('-') for line in open("day12.input").readlines()]
    connections = {}
    
    for map_line in map_lines:
        if map_line[0] not in connections: connections[map_line[0]] = set()
        if map_line[1] not in connections: connections[map_line[1]] = set()

        # Dont add start as a path through
        if map_line[0] != "start": connections[map_line[1]].add(map_line[0])
        if map_line[1] != "start": connections[map_line[0]].add(map_line[1])
    
    # First step
    for first_step in connections['start']:
        # Recursively explore every path from start
        path = ["start", first_step]
        traverse_path_from_step(first_step, connections, path, found_paths)

    print(f"The answer is: {len(found_paths)}")

# Recursion again, 
def traverse_path_from_step(step, connections, path, found_paths, max_small_visits=1):

    # Base case if step is end you can stop and add it
    if step == "end" and path not in found_paths:
        found_paths.append(path)
    else:
        # When you call the function, input should be "smaller", in this case we're only traversing steps that are 
        # uppercase or not in the path already
        next_steps = []
        step_counts = [path.count(step) for step in set(path) if step.islower()]
        for next_step in connections[step]:
            # you've already visited two small caves, and im a small cave that has been visited once, dont add me
            if (not (max_small_visits in step_counts and next_step in path)) or next_step.isupper():
                next_steps.append(next_step)
        for next_step in next_steps:
            traverse_path_from_step(next_step, connections, path+[next_step], found_paths, max_small_visits)


# Now we can visit a small cave twice
def part2():
    found_paths = []
    map_lines = [ line.strip().split('-') for line in open("day12.input").readlines()]
    connections = {}
    
    for map_line in map_lines:
        if map_line[0] not in connections: connections[map_line[0]] = set()
        if map_line[1] not in connections: connections[map_line[1]] = set()
        if map_line[0] != "start": connections[map_line[1]].add(map_line[0])
        if map_line[1] != "start": connections[map_line[0]].add(map_line[1])
    
    # First step
    for first_step in connections['start']:
        # Recursively explore every path from start
        path = ["start", first_step]
        traverse_path_from_step(first_step, connections, path, found_paths, 2)

    print(f"The answer is: {len(found_paths)}")


part1()
part2()