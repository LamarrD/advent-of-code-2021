# We need to calculate the # of times the depth increases
def part1():
    depth_increases = 0
    depths = [int(line.strip()) for line in open('day1.input')]
    prev_depth = depths[0]
    for depth in depths:
        if prev_depth < depth:
            depth_increases += 1
        prev_depth = depth
    print(f"There were {depth_increases} depth increases")

# Now we need to count the number of times the depth increases over a window of 3 depths.
def part2():
    depth_increases = 0
    depths = [int(line.strip()) for line in open('day1.input')]
    for i in range(len(depths)-3):
        a1 = depths[i]
        b1 = depths[i+1]
        c1 = depths[i+2]
        window1 = a1 + b1 + c1

        a2 = depths[i+1]
        b2 = depths[i+2]
        c2 = depths[i+3]
        window2 = a2 + b2 + c2

        if window1 < window2:
            depth_increases += 1
    print(f"There were {depth_increases} depth increases across a 3 value window")

# 1-linerish versions 
def part1b():
    depths = [int(line.strip()) for line in open('day1.input')]
    depth_increases = len([1 for i in range(len(depths))[1:] if depths[i-1] < depths[i]])
    print(f"There were {depth_increases} depth increases")

def part2b():
    depths = [int(line.strip()) for line in open('day1.input')]
    depth_increases = len([i for i in range(len(depths)-3) if sum(depths[i:i+3]) < sum(depths[i+1:i+4])])
    print(f"There were {depth_increases} depth increases across a 3 value window")

if __name__ == "__main__":
    part1()
    part2()
