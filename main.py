def check_valid_matrix(matrix):
    length = len(matrix[0])
    for i in matrix:
        if not len(i) == length:
            return False
    return True


def add_matrix(first: list, second: list):
    if not check_valid_matrix(first):
        return
    if not check_valid_matrix(second):
        return
    end = []
    for i in range(len(first)):
        end.append([])
        for j in range(len(first[i])):
            end[i].append(first[i][j] + second[i][j])
    return end


def multiply_matrix(first: list, second: list):
    if not check_valid_matrix(first):
        return
    if not check_valid_matrix(second):
        return
    if not len(second) == len(first[0]):
        return
    end = []
    for i in range(len(first)):
        end.append([])
    for i in range(len(first)):
        for j in range(len(second[i])):
            dot_sum = 0
            for k in range(len(first[i])):
                dot_sum += first[i][k] * second[k][j]
            end[i].append(dot_sum)
    return end


def print_matrix(matrix: list):
    print("\n")
    for i in range(len(matrix)):
        a = "["
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                a = a[:-1]
                a += "\t| "
            a += str(matrix[i][j]) + "\t"
        a = a[:-1]
        a += "]"
        print(a)


def scale_row(row: list, num: int, check_num: int):
    multiple = row[check_num] / num
    if not multiple == 0:
        new_row = [x / multiple for x in row]
    else:
        new_row = row
    new_row = [int(x) if x == int(x) else x for x in new_row]
    return new_row


def replace_rows(row1: list, row2: list, check_num: int):
    new_row = []
    multiple = row2[check_num] / row1[check_num]
    for i in range(len(row2)):
        new_row.append(row2[i] - (row1[i] * multiple))
    new_row = [int(x) if x == int(x) else x for x in new_row]
    return new_row


def check_if_row_reduced(row: list):
    for i in range(len(row)):
        if i == 0 and row[0] > 1:
            return False
        if not row[i] == 0:
            for j in range(i):
                if not row[j] == 0:
                    return False
            return True


def find_index_of_leftmost_non_zero_num(row: list):
    for i in range(len(row)):
        if not row[i] == 0:
            return i


def row_reduction_algorithm(matrix: list):
    matrix_list = []
    if not check_valid_matrix(matrix):
        return
    new_matrix = matrix
    print_matrix(matrix)
    for i in range(len(new_matrix)):
        index_of_zero = find_index_of_leftmost_non_zero_num(new_matrix[i])
        if index_of_zero is None:
            print("\nThere are linearly dependent rows in the matrix, please try again.")
            return
        new_matrix[i] = scale_row(new_matrix[i], 1, index_of_zero)
        print_matrix(matrix)
        if not i == len(new_matrix) - 1:
            j = i + 1
            while j < len(new_matrix):
                new_matrix[j] = replace_rows(new_matrix[i], new_matrix[j],
                                             find_index_of_leftmost_non_zero_num(new_matrix[i]))
                j += 1
                print_matrix(matrix)

    k = len(new_matrix) - 1
    while k >= 0:
        p = k - 1
        while p >= 0:
            new_matrix[p] = replace_rows(new_matrix[k], new_matrix[p],
                                         find_index_of_leftmost_non_zero_num(new_matrix[k]))
            p -= 1
            print_matrix(matrix)
        k -= 1
    if not check_solved_matrix(matrix):
        print("\nThere is missing information, please try again or no solution. ")
        return
    return matrix_list


def check_solved_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j] == 0:
                k = j + 1
                while k < len(matrix[i]):
                    if not matrix[i][k] == 0 and not k == len(matrix[i]) - 1:
                        return False
                    k += 1
    return True


def print_final(the_matrix: list):
    if the_matrix is not None:
        print_matrix(the_matrix)


if __name__ == "__main__":
    pass
