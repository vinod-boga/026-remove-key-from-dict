def solution(dic1, key1):
    if key1 in dic1: del dic1[key1]
    return dic1

print solution({1:10,2:20,3:30},2)
