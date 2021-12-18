def part1():
    polymer_template = open("day14.input2").readline().strip()
    pair_rules = [line.strip().split(' -> ') for line in open('day14.input2') if '->' in line]
    steps = 10

    for i in range(steps):
        for rule in pair_rules:
            new_template = list(polymer_template)
            letter_pair, letter = rule
            # Ex: For Rule NN -> B, replace all NN with NBN
            new_template
            # new_template = new_template.replace(letter_pair, f"{letter_pair[0]}{letter}{letter_pair[1]}")
            polymer_template = new_template
        pass
    letter_frequencies = {letter: polymer_template.count(letter) for letter in set(polymer_template)}
    most_freq = max(letter_frequencies.values())
    min_freq = min(letter_frequencies.values())
    print(f"The answer is {most_freq-min_freq}")

def part2():
    pass


part1()
part2()