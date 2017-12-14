def birthday_cake_candles(n, ar):
    candle_map = {}
    max = 0

    for candle in ar:
        c = candle_map.get(candle, None)
        if not c:
            candle_map[candle] = 1
        else:
            candle_map[candle] += 1
        if candle_map[candle] > max:
            max = candle_map[candle]

    return max


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthday_cake_candles(n, ar)
print(result)
