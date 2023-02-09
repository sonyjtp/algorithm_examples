# https://www.algoexpert.io/questions/sorted-squared-array

def sortedSquaredArray(array):
    if len(array) == 1:
        return [array[0] * array[0]]
    arr = [(x * x) for x in array]
    arr.sort()
    return arr


