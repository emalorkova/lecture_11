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


def pattern_search(sequence, pattern): #najlepsia aj najhorsia zlozitost je O(n*m), O(n) a O(n*m)
    pozicie = set()
    pattern_len = len(pattern)
    left = 0
    right = pattern_len

    while right < len(sequence):
         for idx_pattern in range(pattern_len):
             if pattern[idx_pattern] != sequence[left + idx_pattern]:
                 break
         else:
             pozicie.add((left + pattern_len) // 2)

         left += 1
         right += 1

    return pozicie


def binary_search(zoznam, cislo):
    left = 0
    len_zoznam = len(zoznam) - 1
    right = len_zoznam
    
    while left <= right:
        middle = (left + right) // 2

        if zoznam[middle] == cislo:
            return middle
        elif zoznam[middle] < cislo:
            left = middle + 1
        elif zoznam[middle] > cislo:
            right = middle - 1

    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    result_1 = linear_search(sequential_data, 9)
    print(result_1)

    sequential_data = read_data("sequential.json", "dna_sequence")
    result_2 = pattern_search(sequential_data, "ATA")
    print(result_2)

    sequential_data = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    result_3 = binary_search(sequential_data, 21)
    print(result_3)




if __name__ == '__main__':
    main()