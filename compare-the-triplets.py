a = [5, 6, 7]
b = [3,8,10]


def compareTriplets(a,b):

    score = [1 if x > y else 0 if x == y else -1 for x, y in zip(a, b)]
    print(score)
    return score.count(1), score.count(-1)






print(compareTriplets(a,b))
