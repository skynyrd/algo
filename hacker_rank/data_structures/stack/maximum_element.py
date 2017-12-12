# https://www.hackerrank.com/challenges/maximum-element/problem

import sys

if __name__ == "__main__":
    stack = []
    stack_for_max = [-sys.maxsize]

    for i in range(0, int(input())):
        data = str(input())
        if " " in data:
            data_to_be_added = int(data.split(" ")[1])
            stack.append(data_to_be_added)

            if data_to_be_added >= stack_for_max[-1]:
                stack_for_max.append(data_to_be_added)

        elif data == "2":
            top_of_the_stack = stack.pop()
            if top_of_the_stack == stack_for_max[-1]:
                stack_for_max.pop()

        else:
            print(stack_for_max[-1])

