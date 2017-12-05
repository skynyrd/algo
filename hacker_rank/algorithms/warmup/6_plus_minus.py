n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

negatives, positives, zeros = 0, 0, 0

for item in arr:
    if item < 0:
        negatives += 1
    elif item > 0:
        positives += 1
    else:
        zeros += 1

print(positives/n)
print(negatives/n)
print(zeros/n)
