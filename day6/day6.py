# We need to keep track of fish and their offspring
def part1():
    fish_timers = list(map(int,open("day6.input").readline().strip().split(',')))
    days = 80
    for _ in range(days):
        fish_timers_to_add = []
        # If timer hits 0 (they have a baby) 
        # and we add their timer to the list (8)
        # and reset the parents times
        fish_timers_length = len(fish_timers)
        for j in range(fish_timers_length):
            fish_timer = fish_timers[j]
            if fish_timer == 0:
                fish_timers[j] = 6
                fish_timers_to_add.append(8)
            else:
                fish_timers[j] -= 1
        fish_timers.extend(fish_timers_to_add)
    print(f"There are {len(fish_timers)} lanternfish after {days} days")


# Our first solutions isnt fast enough and uses too much memory
# A better approach is to keep track of the number of fish at each
# stage Ex: [(1 1s), (1 2s), (2 3s), (0 4s), etc]
def part2():
    fish_timers = list(map(int,open("day6.input").readline().strip().split(',')))
    sum_timers = [fish_timers.count(i) for i in range(0,9)]
    days = 256
    for _ in range(days):
        tmp_timers = sum_timers.copy()
        tmp_timers.append(tmp_timers.pop(0))
        tmp_timers[6] += sum_timers[0]
        sum_timers = tmp_timers
    print(f"There are {sum(sum_timers)} lanternfish after {days} days")

part1()
part2()