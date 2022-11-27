
using Search.Repo;

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Linear Search");
        LinearSearch.Run();
        Console.WriteLine("Binary Search");
        BinarySearch.Run();
    }
}