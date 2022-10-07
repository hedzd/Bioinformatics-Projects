import copy
PAM250 = {
    'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0, 'P': 1,
          'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3},
    'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4,
          'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0},
    'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2, 'P': -1,
          'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': -1,
          'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3,
          'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7},
    'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': 0,
          'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5},
    'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2, 'P': 0,
          'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0},
    'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
          'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1},
    'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1, 'P': -1,
          'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4},
    'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3,
          'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2,
          'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2},
    'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': 0,
          'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2},
    'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0,
          'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5},
    'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1, 'P': 0,
          'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
    'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0,
          'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4},
    'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 1,
          'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3},
    'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0, 'P': 0,
          'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3},
    'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
          'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2},
    'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4,
          'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0},
    'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2,
          'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}
}

gp = -9  # gap penalty


def get_input():
    seq1 = input()  # Sequence 1
    seq2 = input()  # Sequence 2
    arr1 = [c for c in seq1]
    arr2 = [c for c in seq2]
    return arr1, arr2


def print_output(score, seq):
    print(score)
    sortedSeq = [i[0] + i[1] for i in seq]
    sortedSeq.sort()
    for i in sortedSeq:
        print(i[0:int(len(i) / 2)])
        print(i[int(len(i) / 2):])


def initialize(seq1, seq2):
    matrix = [[0 for col in range(len(seq1)+1)] for row in range(len(seq2)+1)]
    backtrack_matrix = [[[] for col in range(len(seq1)+1)] for row in range(len(seq2)+1)]

    for i in range(1, len(seq2)+1):
        for j in range(1, len(seq1)+1):
            c1 = seq1[j-1]
            c2 = seq2[i-1]

            diag = matrix[i-1][j-1] + PAM250[c1][c2]
            horz = matrix[i][j - 1] + gp
            vert = matrix[i - 1][j] + gp

            max_item = max([diag, horz, vert])
            matrix[i][j] = max_item

            if diag == max_item:
                backtrack_matrix[i][j].append([i-1, j-1])
            if horz == max_item:
                backtrack_matrix[i][j].append([i, j - 1])
            if vert == max_item:
                backtrack_matrix[i][j].append([i -1, j])

    return matrix, backtrack_matrix


def find_max(matrix):
    ls = []
    indices = []
    shape = [len(matrix), len(matrix[0])]
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i == shape[0]-1:
                ls.append(matrix[i][j])
            elif j == shape[1]-1:
                ls.append(matrix[i][j])
    # print(ls)
    max_val = max(ls)
    # print(max_val)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i == shape[0] - 1:
                if max_val == matrix[i][j]:
                    indices.append([i, j])
            elif j == shape[1] - 1:
                if max_val == matrix[i][j]:
                    indices.append([i, j])

    return indices, max_val


def traverse(matrix, i, j, backtrack_matrix, path, paths):
    copy_path = copy.deepcopy(path)
    if i == 0 or j == 0:
        paths.append(path)
        return
    for parent in backtrack_matrix[i][j]:
        copy_path.append(parent)
        traverse(matrix, parent[0], parent[1], backtrack_matrix, copy_path, paths)
        copy_path = path

def back_track(matrix, backtrack_matrix, maximums, seq1, seq2):
    seq = []
    paths = []
    for max_index in maximums:
        traverse(matrix, max_index[0], max_index[1], backtrack_matrix, [max_index], paths)

    # print(paths)

    for path in paths:
        alignment1 = []
        alignment2 = []

        if path[0] != [len(seq1), len(seq2)]:
            if path[0][0] < len(seq2):
                dif = len(seq2) - path[0][0]
                for i in range(dif):
                    alignment1.append('-')
                    alignment2.append(seq2[-(i+1)])
            elif path[0][1] < len(seq1):
                dif = len(seq1) - path[0][1]
                for i in range(dif):
                    alignment2.append('-')
                    alignment1.append(seq1[-(i+1)])
        for i in range(len(path)-1):
            node = path[i]
            next_node = path[i+1]
            if next_node[0]+1 == node[0] and next_node[1]+1 == node[1]:
                alignment1.append(seq1[node[1]-1])
                alignment2.append(seq2[node[0]-1])
            elif next_node[0] == node[0] and next_node[1]+1 == node[1]:
                alignment1.append(seq1[node[1]-1])
                alignment2.append('-')
            elif next_node[0]+1 == node[0] and next_node[1] == node[1]:
                alignment1.append('-')
                alignment2.append(seq2[node[0] - 1])

        if path[-1] != [0,0]:
            if path[-1][0] > 0:
                dif = path[-1][0]
                for i in range(dif):
                    alignment1.append('-')
                    alignment2.append(seq2[dif-i-1])
            if path[-1][1] > 0:
                dif = path[-1][1]
                for i in range(dif):
                    alignment2.append('-')
                    alignment1.append(seq1[dif-i-1])
        alg1 = ""
        alg2 = ""
        for x in reversed(alignment1):
            alg1 += x
        for x in reversed(alignment2):
            alg2 += x

        seq.append([alg1, alg2])

    return seq


if __name__ == '__main__':
    seq1, seq2 = get_input()
    mat, backtrack_mat = initialize(seq1, seq2)
    # print(mat)
    # print("--------")
    # print(backtrack_mat)
    maximums, score = find_max(mat)
    # print(maximums)
    final_seq = back_track(mat, backtrack_mat, maximums, seq1, seq2)
    # print("--------")
    # print(final_seq)
    print_output(score, final_seq)