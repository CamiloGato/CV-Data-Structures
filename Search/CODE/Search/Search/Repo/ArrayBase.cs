namespace Search.Repo;

public class ArrayBase
{
    public static int[] CreateRandomArray(int amount)
    {
        int[] array = new int[amount];
        Random random = new Random();
        for (int i = 0; i < amount; i++)
        {
            array[i] = random.Next(0, amount);
        }
        return array;
    }
}