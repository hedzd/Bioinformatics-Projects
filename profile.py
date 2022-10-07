import numpy as np
from itertools import chain, combinations
pseudo_count = 2


def get_input():
    seq_num = int(input())
    seqs = []
    for i in range(seq_num):
        seq = list(input())
        seqs.append(seq)
    main_seq = input()
    seqs = np.array(seqs)
    unique = np.unique(seqs)
    return seqs, main_seq, unique

def make_profile(seqs, unique):
    len_MSA = seqs.shape[1]
    num_seqs = seqs.shape[0]
    profile = np.zeros([len(unique), len_MSA])
    denominator = (len(unique) * pseudo_count) + num_seqs
    for i,char in enumerate(unique):
        for j in range(len_MSA):
            jth_count = np.count_nonzero(seqs[:, j] == char) + pseudo_count
            profile[i, j] = jth_count / denominator

    for i in range(len(unique)):
        sum = 0
        for j in range(len_MSA):
            sum += profile[i, j]
        overall_frequency = sum / len_MSA
        profile[i, :] = profile[i, :]/overall_frequency

    profile = np.log2(profile)
    # print(profile)
    final_profile = {}
    for i,char in enumerate(unique):
        final_profile.update({char: profile[i, :]})
    # print(final_profile)
    return final_profile


def calc_score(seq, profile):
    score = 0
    for i,char in enumerate(seq):
        meh = profile[char][i]
        score += meh
    return score

def skipgram(seq, window_size):
    sg = []
    if len(seq) <= window_size:
        sg.append(seq)
    else:
        for i in range(0, len(seq)-window_size+1):
            sg.append(seq[i: i+window_size])
    return sg


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def getAll(str, window):
    output = []
    all = list(powerset(range(0, len(str))))

    for i in range(window):
        combination = [j for j in all if len(j) == i]
        for item in combination:
            sliced_str = str[0: window - i]
            str_arr = list(sliced_str)

            for index in item:
                str_arr.insert(index, '-')

            output.append(''.join(str_arr))

    return output


def find_all_seqs(query, window_size):
    all = []
    all_powerset = list(powerset(range(0, window_size)))
    # print(all_powerset)

    window_size_seqs = skipgram(query, window_size)

    for seq in window_size_seqs:
        all.extend(getAll(seq, window_size))
    return all

def find_best_subseq(all_possible_seqs, profile):

    best_score = 0
    best_seq = None
    for seq in all_possible_seqs:
        score = calc_score(seq, profile)
        if score > best_score:
            best_score = score
            best_seq = seq
    return best_seq

if __name__ == '__main__':
    seqs, query, unique = get_input()

    profile = make_profile(seqs, unique)
    all_possible_seqs = find_all_seqs(query, seqs.shape[1])
    best_subseq = find_best_subseq(all_possible_seqs, profile)
    print(best_subseq)