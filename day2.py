# We have a submarine that can moves a direction and a distance, we need to find out how far it gets
def part1():
    commands = [line.strip().split(' ') for line in open('day2.input')]

    x, y = 0, 0
    for command in commands:
        direction = command[0]
        distance = int(command[1])

        if direction == "down":
            y += distance
        elif direction == "up":
            y -= distance
        elif direction == "forward":
            x += distance

    print(f"The submarine is in position {x}, {y} and has traveled a total distance of {x * y} units")
    

# Now, we must keep track of a new value aim, which is modified by the up/down commands
def part2():
    commands = [line.strip().split(' ') for line in open('day2.input')]

    x, y, aim = 0, 0, 0
    for command in commands:
        direction = command[0]
        distance = int(command[1])

        if direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        elif direction == "forward":
            x += distance
            y += (distance * aim)

    print(f"The submarine is in position {x}, {y} and has traveled a total distance of {x * y} units")


if __name__ == "__main__":
    part1()
    part2()