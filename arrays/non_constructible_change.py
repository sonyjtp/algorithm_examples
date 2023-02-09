# https://www.algoexpert.io/questions/non-constructible-change
# function that returns the min number that a combination of the sum of numbers in the given array don't add up to
import itertools


def non_constructible_change(arr):
    target = 1
    result = [seq for i in range(1, len(arr) + 1) for seq in itertools.combinations(arr, i)]
    while True:
        list_tuples = list(result)
        list_tuples.sort()
        list_tuples.sort(key=lambda k: sum(k))
        for j in list_tuples:
            if sum(j) == target:
                target += 1
                continue
        return target


print(non_constructible_change([1, 5, 1, 1, 1, 10, 15, 20, 100]))
