# HastSet
Reference: https://www.geeksforgeeks.org/python-sets/

## Creating a Set
- set1 = set()
- set2 = set('str')
- set3 = set(['str1', 'str2', 'str3'])

## Adding Elements to a Set
### Add Method
Elements can be added to the Set by using the built-in add() function. Only one element at a time can be added to the set by using add() method, loops are used to add multiple elements at a time with the use of add() method.
- set1.add(8)
- set1.add((6, 7))
- set1.add('str')

### Update Method
For the addition of two or more elements Update() method is used. The update() method accepts lists, strings, tuples as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

example:
- set1 = set([4, 5, (6, 7)])
- set1.update([10, 11])
- set1 => {4, 5, (6, 7), 10, 11}

## Accessing a Set
- Directly access a set as a whole
- Accessing element using for loop
- Checking the element using in keyword

## Removing elements from the Set
- remove(): <b>KeyError</b> arises if the element doesn’t exist in the set.
- discard(): if the element doesn’t exist in the set, it remains unchanged.
- pop(): can also be used to remove and return an element from the set, but it removes only the last element of the set.
 - Note: If the set is unordered then there’s no such way to determine which element is popped by using the pop() function. 
- clear(): remove all the elements from the set, clear() function is used.

### FrozenSet
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset.  

## Complicity
### Time Complicity
Reference: https://wiki.python.org/moin/TimeComplexity

- lookup/add/remove in O(1)

### Space Complicity
- Depends on number of elements stored in the set

# HashTable


