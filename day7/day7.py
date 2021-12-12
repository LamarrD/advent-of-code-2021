# Make all the crab positions the same using the least amount of fuel
def part1():
    crab_positions = list(map(int, open("day7.input").readline().split(',')))
    positions = list(range(min(crab_positions), max(crab_positions)))
    fuel_for_position = [fuel_to_get_to_position_part1(crab_positions,position) for position in positions]
    print(f"the fuel to get to the position is {min(fuel_for_position)}")

def fuel_to_get_to_position_part1(crab_positions, position):
    fuel = sum([abs(position-crab_position) for crab_position in crab_positions])
    return fuel


# Now each crab step costs more
# (0,0) (1,1), (2,3), (3,6), (4,10), (5,15), (6,21), (7,28),
# (8,36), (9,45), (10,55) (11,66)
def part2():
    crab_positions = list(map(int, open("day7.input").readline().split(',')))
    positions = list(range(min(crab_positions), max(crab_positions)))
    fuel_for_position = [fuel_to_get_to_position_part2(crab_positions,position) for position in positions]
    print(f"the fuel to get to the position is {min(fuel_for_position)}")


def fuel_to_get_to_position_part2(crab_positions, position):
    fuel = 0
    for crab_position in crab_positions:
        distance_apart = abs(position-crab_position)
        positions = range(1,distance_apart+1)
        fuel += sum(positions)
    return fuel

# This is gross and no one should ever do it, but here it is
def part1a():
    print(f"the fuel to get to the position is {min([sum([abs(position-crab_position) for crab_position in list(map(int, open('day7.input').readline().split(',')))]) for position in list(map(int, open('day7.input').readline().split(',')))])}")

part1()
part2()