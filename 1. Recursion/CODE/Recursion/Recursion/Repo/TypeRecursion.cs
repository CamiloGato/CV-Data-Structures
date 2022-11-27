namespace Recursion.Repo;

public class TypeRecursion
{

    public void TailRecursion(int n)
    {
        if (n > 0)
        {
            int k = n * n;
            Console.WriteLine(k);
            TailRecursion(n - 1);
        }
    }

    public void HeadRecursion(int n)
    {
        if (n > 0)
        {
            HeadRecursion(n - 1);
            int k = n * n;
            Console.WriteLine(k);
        }
    }

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

    public static void Run()
    {
        TypeRecursion typeRecursion = new TypeRecursion();
        Console.WriteLine("Tail Recursion");
        typeRecursion.TailRecursion(5);
        Console.WriteLine("Head Recursion");
        typeRecursion.HeadRecursion(5);
        Console.WriteLine("Tree Recursion");
        typeRecursion.TreeRecursion(3);
        Console.WriteLine("Indirect Recursion");
        typeRecursion.IndirectRecursionA(5);
    }
}