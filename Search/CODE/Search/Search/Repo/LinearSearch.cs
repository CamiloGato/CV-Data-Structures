namespace Search.Repo;

public class LinearSearch
{

    public static int Search(int[] array, int key)
    {
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i] == key)
            {
                return i;
            }
        }
        return -1;
    }

    public static void Run()
    {
        LinearSearch linearSearch = new LinearSearch();
        int[] list = ArrayBase.CreateRandomArray(10);
        Console.WriteLine("Array: " + string.Join(", ", list));
        Console.WriteLine("Key: 2");
        Console.WriteLine("Index: " + Search(list, 2));
    }
}