# Creating polymer strands
def part1():
    polymer_template = open("day14.input").readline().strip()
    pair_rules = [line.strip().split(' -> ') for line in open('day14.input') if '->' in line]
    steps = 10

    list_template = [(char,'old') for char in polymer_template]
    for _ in range(steps):
        list_template = [(char, 'old') for char,_ in list_template]
        # Ex: For Rule NN -> B, replace all NN with NBN
        # Also mark the pair as 'new' so that other rules skip it
        for rule in pair_rules:
            letter_pair, letter = rule
            i = 0
            while i < len(list_template)-1:
                current_pair = list_template[i][0] + list_template[i+1][0] 
                should_process = list_template[i][1] != 'new' and list_template[i+1][1] != 'new'
                if current_pair == letter_pair and should_process:
                    list_template.insert(i+1,(letter,'new'))
                i += 1
    polymer_template = "".join([letter for letter,_ in list_template])
    letter_frequencies = {letter: polymer_template.count(letter) for letter in set(polymer_template)}
    most_freq = max(letter_frequencies.values())
    min_freq = min(letter_frequencies.values())
    print(f"The answer is {most_freq-min_freq}")

# Creating much longer polymer strands where a better algorithm is needed
# Instead of keeping it as one long list, lets just keep count of pairs
def part2():
    polymer_template = open("day14.input").readline().strip()
    pair_rules = [line.strip().split(' -> ') for line in open('day14.input') if '->' in line]
    steps = 40

    list_template = [(char,'old') for char in polymer_template]
    for _ in range(steps):
        list_template = [(char, 'old') for char,_ in list_template]
        # Ex: For Rule NN -> B, replace all NN with NBN
        # Also mark the pair as 'new' so that other rules skip it
        for rule in pair_rules:
            letter_pair, letter = rule
            i = 0
            while i < len(list_template)-1:
                current_pair = list_template[i][0] + list_template[i+1][0] 
                should_process = list_template[i][1] != 'new' and list_template[i+1][1] != 'new'
                if current_pair == letter_pair and should_process:
                    list_template.insert(i+1,(letter,'new'))
                i += 1
    polymer_template = "".join([letter for letter,_ in list_template])
    letter_frequencies = {letter: polymer_template.count(letter) for letter in set(polymer_template)}
    most_freq = max(letter_frequencies.values())
    min_freq = min(letter_frequencies.values())
    print(f"The answer is {most_freq-min_freq}")
    pass


part1()
part2()