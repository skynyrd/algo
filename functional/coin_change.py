# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. ,
# Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
#
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should
# be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,
# 5}. So the output should be 5.


from typing import List


def count_change(money: int, coins: List[int]):
    if money == 0:
        return 1
    else:
        return 0 if len(coins) == 0 or money < 0 else count_change(money - coins[0], coins) + count_change(money,
                                                                                                           coins[1:])


print(count_change(10, [2, 5, 3, 6]))

# Explanation:
# Given that you have coins of 2, 5, 3 and 6 for 10 unit of change, you either use the first coin from the list, or not!
# So either you use the first coin, your change will be reduced to 8, and you have 2, 5, 3 and 6.
# Or you don't want to use the first coin, you have 10 unit of change and list of 5, 3 and 6.
