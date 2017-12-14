# If we have "(", we pass the remaining character list and increment open
# If we have ")", first we should check if open count is more than zero, as there can be something like ")asd", and
# we pass the remaining character list with decrementing open count.True
# If we have something else, we just continue to control the other characters.
#
# If length is zero, we return true if open count is zero as balance inner can pass empty char list for strings last
# character


def balance(char_list):
    def balance_inner(char_list, open_cnt):
        if len(char_list) == 0:
            return open_cnt == 0
        else:
            if char_list[0] == "(":
                return balance_inner(char_list[1:], open_cnt + 1)
            else:
                if char_list[0] == ")":
                    return open_cnt > 0 and balance_inner(char_list[1:], open_cnt - 1)
                else:
                    return balance_inner(char_list[1:], open_cnt)

    if len(char_list) == 0:
        return True
    else:
        return balance_inner(char_list, 0)


print(balance("((x))())("))
print(balance("((m))(a)(h)m(ut)"))
