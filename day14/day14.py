from collections import defaultdict
from copy import copy


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
# Instead of keeping it as one long list, lets keep counts of letter pairs
def part2():
    polymer_template = open("day14.input").readline().strip()
    pair_rules = [line.strip().split(' -> ') for line in open('day14.input') if '->' in line]
    steps = 40
    letter_pairs = defaultdict(int) # A dictionary with default value of 0 Ex: {"anything": 0}
    letter_freq = defaultdict(int)

    # Fill our object with all the letter pairs
    for i in range(len(polymer_template)-1):
        letter_pair = polymer_template[i] + polymer_template[i+1]
        letter_pairs[letter_pair] += 1 
    
    # Count the frequencies of each letter
    for letter in set(polymer_template):
        letter_freq[letter] = polymer_template.count(letter)

    for _ in range(steps):
        letter_pairs_tmp = copy(letter_pairs)
        # Ex: For Rule NN -> B, add count of NNs to NBs and BNs. THen set NN to 0
        for rule in pair_rules:
            letter_pair, letter = rule
            if letter_pairs_tmp[letter_pair] != 0:
                current_count = letter_pairs_tmp[letter_pair]
                new_pair1 = letter_pair[0] + letter
                new_pair2 = letter + letter_pair[1]
                letter_pairs[letter_pair] -= current_count
                letter_pairs[new_pair1] += current_count
                letter_pairs[new_pair2] += current_count
                letter_freq[letter] += current_count
        
    most_freq = max(letter_freq.values())
    min_freq = min(letter_freq.values())
    print(f"The answer is {most_freq-min_freq}")


part1()
part2()