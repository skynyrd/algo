def camel_case(input_string):
    counter = 0

    for char in input_string:
        if char == char.upper():
            counter += 1

    return counter + 1

print(camel_case("thisIsCamelCase"))
