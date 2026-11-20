class Solution {
    public long sumAndMultiply(int n) {
         if (n == 0) return 0;

        int[] digits = new int[10];
        int idx = 0;

        while (n > 0) {
            int d = n % 10;
            if (d != 0) {
                digits[idx++] = d;
            }
            n /= 10;
        }

        long x = 0;
        long sum = 0;

        for (int i = idx - 1; i >= 0; i--) {
            x = x * 10 + digits[i];
            sum += digits[i];
        }

        return x * sum;
        
    }
}