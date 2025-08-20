// Last updated: 8/20/2025, 5:41:38 PM
class Solution {
    public int countArrays(int[] original, int[][] bounds) {
        int mod = 1_000_000_007;
        int n = original.length;

        // Initialize range of valid values for copy[i]
        int low = bounds[0][0], high = bounds[0][1];

        for (int i = 1; i < n; i++) {
            int diff = original[i] - original[i - 1];

            // Update the possible range for copy[i]
            int newLow = Math.max(bounds[i][0], low + diff);
            int newHigh = Math.min(bounds[i][1], high + diff);

            // If no valid range exists, return 0
            if (newLow > newHigh) return 0;

            // Update the range for the next iteration
            low = newLow;
            high = newHigh;
        }

        // Count the number of valid arrays
        return (high - low + 1) % mod;
    }
}
