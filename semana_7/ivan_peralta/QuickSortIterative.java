import java.util.Stack;

public class QuickSortIterative {

    public static void main(String[] args) {
        int[] arr = { 10, 7, 8, 9, 1, 5 };
        int n = arr.length;

        quickSort(arr, 0, n - 1);
        printArray(arr);
    }

    static void quickSort(int[] arr, int low, int high) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] { low, high });

        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            low = range[0];
            high = range[1];

            int pi = partition(arr, low, high);

            if (pi - 1 > low) {
                stack.push(new int[] { low, pi - 1 });
            }

            if (pi + 1 < high) {
                stack.push(new int[] { pi + 1, high });
            }
        }
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
