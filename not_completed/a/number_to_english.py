# 1345 -> one thousand three hundred forty five

digit = ["", 'one', "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]


def number_to_english(number):
    if 0 <= number <= 19:
        print(digit[number], end='')

    elif number / 1000000 > 1:
        print(digit[number // 1000000], end='')
        print(' ' + 'million' + ' ', end='')
        number_to_english(number % 1000000)

    elif number / 10000 > 1 > number / 1000000:
        number_to_english(number // 1000)
        print(' ' + 'thousand' + ' ', end='')
        number_to_english(number % 1000)

    elif number / 1000 > 1:
        print(digit[number // 1000], end='')
        print(' ' + 'thousand' + ' ', end='')
        number_to_english(number % 1000)

    elif number / 100 > 1:
        print(digit[number // 100], end='')
        print(' ' + 'hundred and' + ' ', end='')
        number_to_english(number % 100)

    elif number / 10 > 1:
        print(tens[number // 10], end='')
        number_to_english(number % 10)


number_to_english(1343127)
