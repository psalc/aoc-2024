from parsing import read_input
import numpy as np

def iterate_over_lines(input):
    for line in input:
        yield np.array([int(elem) for elem in line.split(' ')])

def iterate_over_deletions(arr):
    for i in range(len(arr)):
        c = arr.copy()
        yield np.delete(c, i)

def evaluate_safety(arr):
    diff_arr = np.diff(arr)
    if (np.all(diff_arr > 0) or np.all(diff_arr < 0)) and (np.all(np.abs(diff_arr) <= 3)):
        return 1
    return 0

def part_one(input):
    return sum([evaluate_safety(arr) for arr in iterate_over_lines(input)])

def part_two(input):
    # toggle for breaking inner loop and continuing outer loop
    continue_outer = False

    safe_rule_count = 0
    
    # iterate over lines in the input array
    for arr in iterate_over_lines(input):
        # If the full array is "safe", increment and continue
        if evaluate_safety(arr) == 1:
            safe_rule_count += 1
            continue
        # Otherwise, iterate over single deletion arrays
        for partial_arr in iterate_over_deletions(arr):
            # If one of the sub-arrays is "safe", toggle continue_outer, increment, and break inner loop
            if evaluate_safety(partial_arr) == 1:
                continue_outer = True
                safe_rule_count += 1
                break
            if continue_outer:
                continue_outer = False
                continue
    return safe_rule_count


def main():
    input = read_input(2)
    print(part_one(input))
    print(part_two(input))

if __name__ == "__main__":
    main()