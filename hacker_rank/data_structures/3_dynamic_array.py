# https://www.hackerrank.com/challenges/dynamic-array/problem

all_input = input().strip().split(" ")
N = int(all_input[0])
Q= int(all_input[1])

lastAns = 0
empty_list = [[]] * N

for trial in range(Q):

    query = input().split(" ")

    if int(query[0]) == 1:
        index = (int(query[1]) ^ lastAns) % N
        empty_list[index] = empty_list[index] + [query[2]]
    else:
        index = (int(query[1]) ^ lastAns) % N
        number = int(query[2])% len(empty_list[index])
        lastAns = int(empty_list[index][number])
        print(lastAns)