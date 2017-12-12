def is_balanced(input_string):
    stack = []

    for char in input_string:
        if char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return "NO"
        if char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return "NO"
        if char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return "NO"
        if char == "(" or char == "[" or char == "{":
            stack.append(char)

    return "YES" if len(stack) == 0 else "NO"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = is_balanced(s)
        print(result)
