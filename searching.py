import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, "r") as json_file:
        dict = json.load(json_file)

    return dict[field]


def linear_search(seq, cislo): #najlepsia aj najhorsia zlozitost je O(n)
    positions = []
    count = 0

    for i in range(len(seq)):
        if seq[i] == cislo:
            positions.append(i)
            count = count + 1

    return {
        "positions": positions,
        "count": count
    }


def pattern_search(sequence, pattern): #najlepsia aj najhorsia zlozitost je O(n*m)
    pozicie = set()
    pattern_len = len(pattern)

    for i in range(len(sequence)):
        if pattern == sequence[i:i+pattern_len]:
            pozicie.add((i + pattern_len)//2)

    return pozicie


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    result_1 = linear_search(sequential_data, 9)
    print(result_1)

    sequential_data = read_data("sequential.json", "dna_sequence")
    result_2 = pattern_search(sequential_data, "ATA")
    print(result_2)



if __name__ == '__main__':
    main()