from functools import reduce

# Find the first illegal character on each line
def part1():
    lines = open('day10.input2').readlines()
    bad_chars = []
    for line in lines:
        bad_chars.append(find_first_syntax_error(line))
    char_scores = {"}": 1197, "]": 57, ")": 3, ">": 25137}
    print(f"Total syntax error score: {sum([ char_scores[bad_char] for bad_char in bad_chars if bad_char])}")

def find_first_syntax_error(line):
    char_pairs = {"{": "}", "[": "]", "(": ")", "<": ">"}
    stack = []
    for char in line.strip():
        if char in char_pairs.keys():
            stack.append(char)
        elif char in char_pairs.values():
            if len(stack) == 0:
                return char
            elif char_pairs[stack.pop()] != char:
                return char


def part2():
    lines = open('day10.input').readlines()
    line_scores = []
    for line in lines:
        if not find_first_syntax_error(line):
            line_scores.append(get_incomplete_line_score(line))
    print(f"Middle score: {sorted(line_scores)[int(len(line_scores)/2)]}")
    
def get_incomplete_line_score(line):
    char_pairs = {"{": "}", "[": "]", "(": ")", "<": ">"}
    stack = []
    for char in line.strip():
        if char in char_pairs.keys():
            stack.append(char)
        elif char in char_pairs.values():
            if len(stack) == 0:
                return char
            elif char_pairs[stack.pop()] != char:
                return char

    char_scores = {"}": 3, "]": 2, ")": 1, ">": 4}
    required_chars = "".join([char_pairs[char] for char in stack[::-1]])
    score = reduce(lambda a, b: (a*5) + char_scores[b], required_chars, 0)
    return score


part1()
part2()