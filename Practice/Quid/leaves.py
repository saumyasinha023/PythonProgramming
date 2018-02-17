from collections import defaultdict


def countUneatenLeaves(n, a):
    uneatenLeaves, arraylen, eatenLeaves = 0, len(a), 0

    dict = defaultdict()
    for i in range(arraylen):
        cater = a[i]
        j = 1
        while j * cater <= n:
            j += 1
            if (a[i] * j) not in dict.keys():
                dict[a[i] * j] = 1
                eatenLeaves += 1

    uneatenLeaves = n - eatenLeaves
    return uneatenLeaves
