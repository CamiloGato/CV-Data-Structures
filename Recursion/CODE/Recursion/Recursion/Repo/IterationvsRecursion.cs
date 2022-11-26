namespace Recursion.Repo;

public class IterationvsRecursion
{
    public void CalculateIterative(int n)
    {
        while (n > 0)
        {
            int k = n * n;
            Console.WriteLine(k);
            n--;
        }
    }

    public void CalculateRecursive(int n)
    {
        if (n > 0)
        {
            int k = n * n;
            Console.WriteLine(k);
            CalculateRecursive(n - 1);
        }
    }

    public static void Run()
    {
        IterationvsRecursion iterationvsRecursion = new IterationvsRecursion();
        Console.WriteLine("Iterative");
        iterationvsRecursion.CalculateIterative(5);
        Console.WriteLine("Recursive");
        iterationvsRecursion.CalculateRecursive(5);
    }
}