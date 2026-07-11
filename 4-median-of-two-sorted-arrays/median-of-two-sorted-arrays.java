class Solution {
    public double findMedianSortedArrays(int[] a, int[] b) {
        int n1 = a.length;
        int n2 = b.length;
        int n = n1 + n2;

        int ind2 = n / 2;
        int ind1 = ind2 - 1;

        int i = 0, j = 0, count = 0;
        int ind1el = -1, ind2el = -1;

        while (i < n1 && j < n2) {
            if (a[i] < b[j]) {
                if (count == ind1) ind1el = a[i];
                if (count == ind2) ind2el = a[i];
                i++;
            } else {
                if (count == ind1) ind1el = b[j];
                if (count == ind2) ind2el = b[j];
                j++;
            }
            count++;
        }

        while (i < n1) {
            if (count == ind1) ind1el = a[i];
            if (count == ind2) ind2el = a[i];
            i++;
            count++;
        }

        while (j < n2) {
            if (count == ind1) ind1el = b[j];
            if (count == ind2) ind2el = b[j];
            j++;
            count++;
        }

        if (n % 2 == 1) {
            return ind2el;
        }

        return (ind1el + ind2el) / 2.0;
    }
}