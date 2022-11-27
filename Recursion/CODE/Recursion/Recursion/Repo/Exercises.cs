namespace Recursion.Repo;

public class Exercises
{
    public int SumOfN(int n)
    {
        if (n == 1) return 1;
        return n + SumOfN(n - 1);
    }

    public static void Run()
    {
        var exercises = new Exercises();
        Console.WriteLine("Sum of N");
        Console.WriteLine(exercises.SumOfN(5));
    }
}