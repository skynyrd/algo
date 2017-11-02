### Notes on hash tables:

Simple implementation: array of linked lists and a hash code function.

#### Inserting key:
* Compute key's hashcode.
* map the hash code to an index in the array `get_hash(key) % array_length`
* Keys can have same hash code, therefore they can be stored into the same index.
* At this index, there is a linked list of keys and values. We must use linked list because of collisions.

__If the number of collisions is very high, the worst case runtime is O(N), where N is the number of keys. However, we generally assume a good implementation that keeps collisions to a minimum, in which case the lookup time is O(1)__

```
Alternatively, we can implement hash tables with a balanced binary search tree. This gives us an O(logN) lookup time. The adventage of this is potentially using less space, since we no longer allocate a large array.
```

#### Dynamic Array (List)
An array resizes itself as needed while still providing O(1) access. __When array is full, the array doubles in size__. Each doubling takes O(n) time but happens so rarely that its amortized __insertion time is still O(1)__. In python, resizing factor is not 2, its more complicated but in Java its 2.

Insertion to middle takes O(n) as other elements should move.

##### Why insertion is amortized to O(1)
```
final capacity increase: n/2 elements to copy
previous capacity increase: n/4 elements to copy
previous capacity increase: n/8 elements to copy
previous capacity increase: n/16 elements to copy
...
second capacity increase: 2 elements
first capacity increase: 1 element

sum of all is roughly 1, less than N.
```

#### String builder

```python
joinWords(words):
    result = ""
    for word in words:
        result = result + word
    return result
```

The builder above works on O(n^2), n for loop, and n for copying double characters each time.

If you create a resizable array of all the strings and copying them back to a string only when necessary, your runtime become O(n). Ex. `StringBuilder` in Java.

Good Exercise: Implement your own StringBuilder, HashTable and ArrayList.

ASCII set = 128 chars, extended ASCII set = 256 chars.