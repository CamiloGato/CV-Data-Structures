# Recursion

The fact here is that the function call to itself.

In this case, generally, the iteration is created by a condition, for example, in the iterative form we use the While loop.

Here we can see the iterative form.

```csharp
public void CalculateIterative(int n)
    {
        while (n > 0)
        {
            int k = n * n;
            Console.WriteLine(k);
            n--;
        }
    }
```

Next an example of recursive for.

```csharp
public void CalculateRecursive(int n)
    {
        if (n > 0)
        {
            int k = n * n;
            Console.WriteLine(k);
            CalculateRecursive(n - 1);
        }
    }
```

Now, the time complexity of the Recursive Function is calculated using the n time execution. For example, consider the last function.

```csharp
function calculate(n) <- T(n)
	if n > 0 then       <- 1
		k := n ^ 2        <- 1
		print(k)          <- 1
		calculate(n-1)    <- T(n-1)
```

First, we need to calculate the T(n) case, following the next.

$$
T(n) = 1 + 1 + 1 + T(n-1)\\
T(n) = T(n-1) + 3, \qquad n>0\\
T(n-1) =T(n-2)+3\\
T(n-2) = T(n-3)+3\\
\vdots\\
T(1) = T(0) + 3\\
T(0) = 1
$$

Now We can replace the cases.

$$
T(n) = T(n-1)+3\\
T(n) = (T(n-2)+3)+3\\
T(n) = ((T(n-3)+3)+3)+3\\
T(n) = (T(0) + 3 + 3 + \cdots + 3)
$$

So, thanks to Substitution we can find the Time Complex.

$$
T(n) = 1 + 3n \longrightarrow O(n) = n
$$

```csharp
function someFunction(n):
	...
```

Suppose that the function algorithm cost in n is  $T(n) = T(n-1)+n$ and, $T(1) = 1$.

Now we calculate using the next steps.

$$
T(n) = T(n-1) + n\\
T(n-1) = T(n-2) + (n-1) \\
T(n-2) = T(n-3) + (n-2) \\
$$

Now making substitution we have the next equation.

$$
T(n) = T(n-1) + n \\
T(n) = T(n-2) + (n-1) + n \\ 
T(n) = T(n-3) + (n-2) + (n-1) + n\\
\vdots\\
T(n) = T(n-k) + (n-k-1) + \cdots + (n-2) + (n-1) + n
$$

With the last equation, we need to analyze the base case, i.e.  $n-k = 1 \longrightarrow k=n-1$ 

$$
T(n) = T(n-(n-1))+(n-(n-1)-1) + \cdots + (n-2) + (n-1) + n \\
T(n) = T(1) + 0 + \cdots + (n-2) + (n-1) + n\\
T(n) = 1 + \cdots + (n-2) + (n-1) + n\\
T(n) = \sum_{k=1}^{n} k = \dfrac{n(n+1)}{2}\\
T(n)= \dfrac{n^2 + n}{2} \longrightarrow O(n)=n^2 
$$

# Types of Recursions

## Tail Recursion

This is the commonest recursion type, here we improve the logic before executing the next call of the recursive function.

```csharp
public void TailRecursion(int n)
{
    if (n > 0)
    {
        int k = n * n;
        Console.WriteLine(k);
        TailRecursion(n - 1);
    }
}
```

![Untitled](Recursion%206586512553e847d6828525c16c7bbb21/Untitled.png)

## Head Recursion

Here first we execute the next call of the recursive function, after, we improve the logic, in this case, the logic will be executed when all the calling recursions end.

```csharp
public void HeadRecursion(int n)
{
    if (n > 0)
    {
        HeadRecursion(n - 1);
        int k = n * n;
        Console.WriteLine(k);
    }
}
```

In this case, the calling stack will be.

| Cal(4) | ← Call Back |  |  |  |
| --- | --- | --- | --- | --- |
| - end | Cal(3) | ← Call Back |  |  |
|  | - k = 16
- “16” | Cal(2) | ← Call Back |  |
|  |  | - k = 9
- “9” | Cal(1) | ← Call Back |
|  |  |  | - k = 4
- “4” | Cal(0) |
|  |  |  |  | - k = 1
- “1” |

![Untitled](Recursion%206586512553e847d6828525c16c7bbb21/Untitled%201.png)

***Note:** This is like an accumulative output call.*

## Tree Recursion

In the tree recursion, we have more than one recursion call.

```csharp
public void TreeRecursion(int n)
{
    if (n > 0)
    {
        TreeRecursion(n - 1);
        int k = n * n;
        Console.WriteLine(k);
        TreeRecursion(n - 1);
    }
}
```

In this case, the calling tree will be.

![Untitled](Recursion%206586512553e847d6828525c16c7bbb21/Untitled%202.png)

Now, the complexity in this case we are going to count the number of recursions, in this case, is 15 but is 15 for n=3, now suppose that n=k, now, we need to analyze each level in the tree, i.e. we have the following equation.

$$
T(3) = 1 + 2 + 4 + 8 \\
T(3) = 2^0 + 2^1 + 2^3\\
T(3) = \sum_{k=0}^{3}2^{k}\\
T(n) = \sum_{k=0}^{n}2^{k} \longrightarrow O(n) = 2^n
$$

This is the output for n=3.

![Untitled](Recursion%206586512553e847d6828525c16c7bbb21/Untitled%203.png)

## Indirect Recursion

This recursion is based on calling another function that calls the function from.

```csharp
public void IndirectRecursionA(int n)
{
    if (n > 0)
    {
        int k = n * n;
        Console.WriteLine(k);
        IndirectRecursionB(n - 1);
    }
}

public void IndirectRecursionB(int n)
{
    if (n > 0)
    {
        int k = n * n;
        Console.WriteLine(k);
        IndirectRecursionA(n - 1);
    }
}
```

# Exercises

## Sum of N Numbers

Create an algorithm that sums the n terms, where n is a Natural Number.

First, we need to consider that the sum of the first n numbers can be written as follow.

$$
sum(n)=n+sum(n-1)\\
sum(n-1)=(n-1)+sum(n-2)\\
\vdots \\
sum(1) = 1
$$

Here the base case is $sum(1)=1$ and the n case $sum(n)=n+sum(n-1)$.

Using recursion we can improve the next algorithm.

```csharp
public int SumOfN(int n)
{
    if (n == 1) return 1;
    return n + SumOfN(n - 1);
}
```

Now we are going to analyze the algorithm based on the next conditions.

$$
T(n) = 1 + 1 + T(n-1) \qquad T(1) = 1
$$

We are going to use substitution to get the algorithm cost.

$$
T(n) = 2+T(n-1)\\
T(n-1) = 2 + T(n-2)\\
T(n-2) = 2 + T(n-3)\\
\vdots \\
T(1) = 1
$$

Next, using the substitution we have the next equation.

$$
T(n) = 2 + T(n-1)\\
T(n) = 2 + (2 + T(n-2))\\
T(n) = 2 + (2 + (2 + T(n-3) )\\
\vdots\\
T(n) = 2 + 2 + 2 + \cdots + 2 + 1\\
T(n) = 2n+1 \longrightarrow O(n)=n
$$

## Factorial

The factorial of n supplies the next formula.

$$
fac(n) = n * (n-1) * (n-2) * (n-3) \cdots 1
$$

First, we are going to consider the factorial with the next conditions.

$$
fac(n) = n * fac(n-1) \qquad fac(1) = 1
$$

With the base condition and the n condition, we can create the next algorithm.

```csharp
public int Factorial(int n)
    {
        if (n == 1) return 1;
        return n * Factorial(n - 1);
    }
```

Now we are going to analyze the complexity of this algorithm.

$$
T(n) = 1 + 1 + T(n-1) \qquad T(1) = 1
$$

We are going to use substitution to calculate the complexity.

$$
T(n) = 2 + T(n-1)\\
T(n) = 2 + ( 2 + T(n-2) )\\
T(n) = 2 + ( 2 + ( 2 + T(n-3) ) )\\
\vdots\\
T(n) = 2 + 2 + 2 + \cdots + 2 + 1\\
T(n) = 2n + 1 \longrightarrow O(n) = n
$$