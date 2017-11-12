# Sorting

* Choose algorithm wisely.

For example, Given a very large array of Person objects, sort the people in increasing order of age.

1. It's a large array, so efficiency is important.
2. We are sorting based on ages, so we know the values are in a small range.

* By scanning thru the various sorting algorithms, we might notce that bucket (or radix) sort would be a perfect match.
* In fact, we can make the buckets small (just 1 year each) and get O(n) running time.

## Common Sorting Algorithms

For interviews, most common sorting algorithms are Merge Sort, Quick Sort and Bucket Sort.

#### Bubble Sort | Runtime: O(n^2) average and worst case. Memory: O(1)

* Start at the beginning of the array
* Swap first two if the first is greater than second
* Continue

__Smaller items slowly "bubble" up to the beginning of the list__

#### Selection Sort | Runtime: O(n^2) average and worst case. Memory O(1)

* Child's algorithm, simple but inefficient
* Find the smallest element using a linear scan.
* Move it to the front (swapping it the front element)
* Find the second smallest and do the same thing.

#### Merge Sort | Runtime: O(nlog(n)) average and worst case. Memory: Depends

* Divides the array in half
* Sorts each of those halves
* Merge them back together
* Each of those halves has the same sorting algorithm applied to it
* Eventually you are merging just two single element arrays.
* Heavy lifting is on `merge` part.