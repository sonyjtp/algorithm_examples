# https://www.algoexpert.io/questions/validate-subsequence

def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False
    i = 0
    idx = 0
    while True:
        if sequence[i] not in array:
            return False
        array = array[array.index(sequence[i]) + 1:]
        i += 1
        if i == len(sequence):
            break
    return True

