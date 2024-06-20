public class MergeSortIterative {

    public static void main(String[] args) {
        int[] arr = { 12, 11, 13, 5, 6, 7 };
        int n = arr.length;

        mergeSort(arr, n);
        printArray(arr);
    }

    static void mergeSort(int[] arr, int n) {
        int curr_size;
        int left_start;

        for (curr_size = 1; curr_size <= n - 1; curr_size = 2 * curr_size) {
            for (left_start = 0; left_start < n - 1; left_start += 2 * curr_size) {
                int mid = Math.min(left_start + curr_size - 1, n - 1);
                int right_end = Math.min(left_start + 2 * curr_size - 1, n - 1);

                merge(arr, left_start, mid, right_end);
            }
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; ++i) {
            L[i] = arr[left + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[mid + 1 + j];
        }

        int i = 0, j = 0;
        int k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
