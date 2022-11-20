# Simple Data Types

# Arrays

The arrays are a collection of data which is responsible for storing the same type of data. They have three main characteristics.

- The elements that stores are the same type.
- Are stored in consecutive memory location.
- Can be accessed by an index (Starting at zero, ending at length minus one)

Thus, to manipulate an array, in addition to the elements themselves, three pieces of information must be stored: the memory address where the array begins, its length (number of elements) and the data type.

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled.png)

## Indexing

In this way, accessing an element whose index is known i (index) consist of:

```csharp
indexacion(X, i):
	if i < 0 OR i >= X.size:
		return ERROR
	else:
		return dir + (i*sizeOf(type))
```

Thus, for the array of integers seen in the previous example, accessing the element at index 4 means getting the data at memory location 0x37 to 0x40.

In other words, regardless of the size of the array, if it has elements of the same type, the indexing operation is O(1).

## Modification

It consists of updating the element stored in a certain index. This operation implies, first accessing the memory location, which as we have already seen is O(1) and then making the change, which is also O(1).

## Linear Search

Determining if an element e is inside an array X, can be done in the following way:

```csharp
LinearSearch(X, e):
	i = 0
		while i < N:
			if Xi = e:
				return True
			i += 1
		return False
```

Whose complexity is $f(n) = 1 + N(2) + 1 \longrightarrow O(N)$.

## Insertion

In some programming languages, such Java or C#, the fixed-length arrays whose length is established when the array is created, from there, remain fixed, are differentiated from variable-length ones. (Vectors).

Suppose a new element is added to the end of the array.

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled%201.png)

During this operation the additional memory is requested and one of two things can happen:

- That such memory (in the example 0x28 to 0x31) is free.
- That space is occupied.

**The first case is favorable** because the only thing to do is reserve that memory space and then save the element there, that is, the efficiency is O(1).

**The second case is problematic** because the new element cannot be requested in another memory space because the structure would stop being an array (elements in contiguous memory locations).

**What can be done then?.**
The only alternative is to move the entire array to a new memory address where everything you already had fits, plus the new.

In other words you have to:

- Find enough memory space.
- Reserve said memory space.
- "Move" the elements that were already there and add the new one

Which implies $O(1) + O(1) + O(N) = O(N)$.

************************Custom Index************************

Suppose now that we want to insert a new element, not at the end of the array, but at an index i (0 ≤ i < N-1).

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled%202.png)

In this case, the worst case scenario is that there is no contiguous memory available, and the entire resulting array needs to be moved, which would be O(N).

In addition, even with contiguous available memory (at the beginning or at the end of the array), in the worst case N/2 elements will have to be moved either one position to the right or to the left, that is, this scenario is also O(N ).

## Erased

Two cases have to be analysed:

- If the index i of the element is known.
- If it is not known

**In the first case** you have to move the elements to the right of i one position to the left, or the elements to the left of i one position to the right (whichever is more efficient).

In this case $f(N) = \dfrac{N}{2} + 1 \longrightarrow O(N)$

**In the second case** it is necessary, before the previous operation, to search for the first occurrence of the element (find i). This, as we have already seen, can be done in O(N)

In this case $f(N) = N(2) + 1 + \dfrac{N}{2}+1 \longrightarrow O(N)$

## Summary Part I

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled%203.png)

## Binary Search

We saw previously that the efficiency of an array search is O(N), but can it be done better?.

The answer is yes, … and it depends.

Yes, by binary search and depends on whether the array is presorted.

```csharp
BinarySearch( X, e ):
	beggin = 0
	end = N-1
	while beggin <= end:
		mid = ( beggin + end ) / 2
		if x_mid = e:
			return mid
		else if e < x_mid:
			end = mid - 1
		else :
			beggin = mid + 1
	return -1
```

The efficiency is $f(N) = 2+4\cdot log_{_2} N + 1 \longrightarrow O(log_{_2} N)$

## Select Sort

```csharp
SelectSort(X):
	for i = 0 to N-2:
		minIndex = i
			for j = i+1 to N-1:
				if X_j < X_minIndex:
					minIndex = j
		X_i, X_minIndex = X_minIndex, X_i
```

The efficiency is $f(N) = 4 \cdot \dfrac{N(N-1)}{2} \longrightarrow O(N^2)$

## Insert Sort

```csharp
InsertSort(X):
	for i=1 to N-1:
		j=i
		while j > 0 and X_j-1 > X_j:
			X_j-1, X_j = X_j, X_j-1
			j -= 1
```

The efficiency is $f(N) = 3 \cdot \dfrac{N(N-1)}{2} \longrightarrow O(N^2)$

## Bubble Sort

```csharp
BubbleSort(X):
	for i=2 to N:
		for j=0 to N-i:
			if (X_j > X_j+1):
				X_j, X_j+1 = X_j+1, X_j
```

The efficiency is $f(N) = 2 \cdot \dfrac{N(N-1)}{2} \longrightarrow O(N^2)$

## Merge Sort

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled%204.png)

## Summary Part II

![Untitled](Simple%20Data%20Types%208c1f86fc993a48279afb1eef28866357/Untitled%205.png)