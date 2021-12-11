
# (0,6) , (1,2), (2,5), (3,5), (4,4), (5,5), (6,6), (7,3) (8,7), (9,6)
def part1():
    output_lengths = [ list(map(len, line.split(' | ')[1].split())) for line in open('day8.input').readlines()]
    easy_outputs = [ output.count(2) + output.count(4) + output.count(3) + output.count(7) for output in output_lengths]
    total_easy_outputs = sum(easy_outputs)
    print(f"Total easy outputs: {total_easy_outputs}")

#  dddd
# g    b
# g    b
#  cccc 
# a    e
# a    e
#  ffff
def part2():
    io_pairs = [list(map(lambda x: x.split(),line.strip().split(' | '))) for line in open('day8.input').readlines()]
    sum_of_outputs = 0

    for io_pair in io_pairs:
        inputs = io_pair[0]
        outputs = io_pair[1]
        input_map = {
            1: list(filter(lambda x:len(x) == 2, inputs))[0],
            4: list(filter(lambda x:len(x) == 4, inputs))[0],  
            7: list(filter(lambda x:len(x) == 3, inputs))[0], 
            8: list(filter(lambda x:len(x) == 7, inputs))[0], 
        }
        # Get 3,5,2 based on length and common letters with known inputs
        len_5s = list(filter(lambda x:len(x) == 5, inputs))
        input_map[3] = list(filter(lambda x: len(set(x).intersection(set(input_map[1]))) == 2, len_5s))[0]
        len_5s.remove(input_map[3])
        input_map[5] = list(filter(lambda x: len(set(x).intersection(set(input_map[4]))) == 3, len_5s))[0]
        len_5s.remove(input_map[5])
        input_map[2] = len_5s[0]

        # Get 3,5,2 based on length and common letters with known inputs
        len_6s = list(filter(lambda x:len(x) == 6, inputs))
        input_map[9] = list(filter(lambda x: len(set(x).intersection(set(input_map[4]))) == 4, len_6s))[0]
        len_6s.remove(input_map[9])
        input_map[0] = list(filter(lambda x: len(set(x).intersection(set(input_map[7]))) == 3, len_6s))[0]
        len_6s.remove(input_map[0])
        input_map[6] = len_6s[0]

        # Sort all outputs by letter "cab" => "abc"
        input_map = {str(k):"".join(sorted(v)) for k,v in input_map.items()} 

        # Getting the number form our dict...by value
        output = [list(input_map.keys())[list(input_map.values()).index("".join(sorted(output)))] for output in outputs]
        sum_of_outputs += int("".join(output))
    
    print(f"Total easy outputs: {sum_of_outputs}")


part1()
part2()