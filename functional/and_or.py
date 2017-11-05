def logical_and(x, y):
    return y if x else False


def logical_or(x, y):
    return True if x else y


print(logical_and(True, True))
print(logical_and(True, False))
print(logical_and(False, True))
print(logical_and(False, False))
print(logical_or(True, True))
print(logical_or(True, False))
print(logical_or(False, True))
print(logical_or(False, False))
