# Explanation: https://www.youtube.com/watch?v=3ZDZ-N0EPV0
# * - any character or zero
# ? - any single character


def is_match(input_str, pattern_raw):
    # replace multiple * with single *

    pattern = ""

    for i in range(0, len(pattern_raw)):
        if pattern_raw[i] != "*":
            pattern += pattern_raw[i]
        else:
            if not i + 1 < len(pattern_raw):
                pattern += "*"
            else:
                if pattern_raw[i + 1] != "*":
                    pattern += "*"

    t = [[False] * (len(pattern) + 1)] * (len(input_str) + 1)

    # input="", pattern=""
    t[0][0] = True

    # input="", pattern"*..."
    if len(pattern) > 0 and pattern[0] == "*":
        t[0][1] = True

    for i in range(1, len(t)):
        for j in range(1, len(t[0])):
            if pattern[j-1] == "?" or input_str[i-1] == pattern[j-1]:
                t[i][j] = t[i-1][j-1]
            elif pattern[j-1] == "*":
                t[i][j] = t[i-1][j] or t[i][j-1]

    return t[len(input_str)][len(pattern)]

print(is_match("abcd", "ab?d*"))
print(is_match("abcd", "ab***d*"))
print(is_match("acd", "ab***d*"))
print(is_match("acd", "acd"))
print(is_match("acd", "ace"))
