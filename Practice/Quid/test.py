from collections import defaultdict


def calculateScore(text, prefix, suffix):
    length = len(text)
    lenSuffix = len(suffix)
    lenPrefix = len(prefix)

    dict = defaultdict()
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub = text[i:j]
            preString, subString, subLen = 0, 0, len(sub)

            for k in range(len(sub)):
                if (subLen - k <= lenSuffix):
                    if (sub[k:] == suffix[0:subLen - k]):
                        preString = max(subLen - k, preString)

            for k in range(subLen):
                if k < lenPrefix:
                    if (sub[0:k + 1] == prefix[lenPrefix - k - 1:lenPrefix]):
                        subString = max(k + 1, subString)

            if sub not in dict.keys():
                dict[sub] = (preString + subString)
            else:
                dict[sub] = max(dict[sub], subString + preString)

    tmp = -1
    keys = set()
    for each in dict:
        keys.add(each)

    arr = sorted(keys)

    ans = None
    for i in range(len(arr)):
        if tmp < dict[arr[i]]:
            ans = arr[i]
            tmp = dict[arr[i]]
    return ans
