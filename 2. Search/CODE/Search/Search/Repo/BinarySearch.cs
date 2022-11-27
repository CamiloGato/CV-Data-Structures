namespace Search.Repo;

public class BinarySearch
{

    public int BinarySearchIterative(int[] array, int n, int key)
    {
        int low = 0;
        int high = n - 1;

        while (low <= high)
        {
            int mid = (low + high) / 2;
            if (key == array[mid])
            {
                return mid;
            }
            if (key < array[mid])
            {
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        
        return -1;
    }

    public int BinarySearchRecursive(int[] array, int key, int low, int high)
    {
        if (low > high)
        {
            return -1;
        }

        int mid = (low + high) / 2;
        if (key == array[mid])
        {
            return mid;
        }
        if (key < array[mid])
        {
            return BinarySearchRecursive(array, key, low, mid - 1);
        }
        else
        {
            return BinarySearchRecursive(array, key, mid + 1, high);
        }
    }
    
    public static void Run()
    {
        BinarySearch binarySearch = new BinarySearch();
        int[] list = ArrayBase.CreateRandomArray(10);
        Console.WriteLine("- Binary Search Iterative");
        Console.WriteLine("Array: " + string.Join(", ", list));
        Console.WriteLine("Key: 2");
        Console.WriteLine("Index: " + binarySearch.BinarySearchIterative(list, list.Length, 2));
        Console.WriteLine("- Binary Search Recursive");
        Console.WriteLine("Array: " + string.Join(", ", list));
        Console.WriteLine("Key: 2");
        Console.WriteLine("Index: " + binarySearch.BinarySearchRecursive(list, 2, 0, list.Length - 1));
    }
}