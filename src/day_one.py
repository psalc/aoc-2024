from parsing import read_input
import numpy as np

def create_arrays(input: str):
    # parse text lines into lists
    array_one = np.array([int(line.split('   ')[0]) for line in input])
    array_two = np.array([int(line.split('   ')[1]) for line in input])
    
    # sort lists least to greatest
    array_one.sort()
    array_two.sort()

    return array_one, array_two

def compare_diffs_and_sum(a1, a2):
    diffs = np.subtract(a1, a2)
    abs_diffs = np.abs(diffs)
    return sum(abs_diffs)

def create_counter_dict(arr):
    elem, counts = np.unique(arr, return_counts=True)
    return dict(zip(elem, counts))

def get_item_count(item, counter_dict):
    return counter_dict.get(item, 0)

def calculate_similarity_scores_and_sum(a1, a2):
    counter_dict = create_counter_dict(a2)
    return sum([item * get_item_count(item, counter_dict) for item in a1])

def part_one(a1, a2):
    print(compare_diffs_and_sum(a1, a2))

def part_two(a1, a2):
    print(calculate_similarity_scores_and_sum(a1, a2))

def main():
    input = read_input(1)
    a1, a2 = create_arrays(input)
    print('Part One:')
    part_one(a1, a2)
    print('Part Two:')
    part_two(a1, a2)


if __name__ == "__main__":
    main()