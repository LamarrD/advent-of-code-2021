def part1():
    numbers = [line.strip() for line in open('day3.input')]
    number_of_columns = len(numbers)
    value = [0] * 12
    gamma_rate_list = [0] * 12 # the most common bit out of all the numbers for each column
    epsilon_rate_list = [0] * 12  # the most common bit out of all the numbers for each column
    
    for number in numbers:
        for i in range(11):
            value[i] += int(number[i])

    for i in range(len(value)):
        if number_of_columns / 2 > value[i]:
            gamma_rate_list[i] = 1
            epsilon_rate_list[i] = 0
        else:
            gamma_rate_list[i] = 0
            epsilon_rate_list[i] = 1

    gamma_rate = ''.join(str(e) for e in gamma_rate_list)
    epsilon_rate = ''.join(str(e) for e in epsilon_rate_list)

    print(f"The gamma rate is {gamma_rate}")
    print(f"The epsilon rate is {epsilon_rate}")
    print(f"The power consumpyion is {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


def part2():
    numbers = [line.strip() for line in open('day3.input')]

    # Oxygen Rating 
    oxy_index = 0
    while len(numbers) > 1:
        column = [ number[oxy_index] for number in numbers ] 
        sum = 0
        for number in column:
            sum += int(number)

        if sum >= len(numbers) / 2:
            # remove all 0 starting numbers
            tmp = [number for number in numbers if number[oxy_index] == '1']
            numbers = tmp
        else:
            tmp = [number for number in numbers if number[oxy_index] == '0']
            numbers = tmp
        oxy_index += 1
    oxygen_rating = numbers[0]

    # Scrubber rating 
    numbers = [line.strip() for line in open('day3.input')]
    scrub_index = 0
    while len(numbers) > 1:
        column = [ number[scrub_index] for number in numbers ] 
        sum = 0
        for number in column:
            sum += int(number)

        if sum >= len(numbers) / 2:
            # remove all 0 starting numbers
            tmp = [number for number in numbers if number[scrub_index] == '0']
            numbers = tmp
        else:
            tmp = [number for number in numbers if number[scrub_index] == '1']
            numbers = tmp
        scrub_index += 1
    scrubber_rating = numbers[0]

    print(f"The oxygen rating is {oxygen_rating}")
    print(f"The scrubber rating is {scrubber_rating}")
    print(f"The life support rating is {int(scrubber_rating, 2) * int(oxygen_rating, 2)}")

# I know this is close
def part1b():
    gamma_rate = sum([int(line.strip(),2) for line in open('day3.input')]) & 0xfff
    print(f"The gamma rate is {gamma_rate}")

def part2b():
    pass


part1()
part2()