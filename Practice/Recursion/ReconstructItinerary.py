import collections


def findItinerary(tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,


findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])


# ab=[[1,1,3]]
#
# for a, b,c in sorted(ab)[::-1]:
#     print(a,b,c)
#
#
# print(sorted(ab))
#
#
# print([2,3,9,5][::-1])