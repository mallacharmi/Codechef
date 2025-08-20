// Last updated: 8/20/2025, 5:41:40 PM

import java.util.Arrays;

class Solution {
    public int[] transformArray(int[] nums) {
        // Replace even numbers with 0, odd numbers with 1
        for (int i = 0; i < nums.length; i++) {
            nums[i] = (nums[i] % 2 == 0) ? 0 : 1;
        }
        // Sort the modified array
        Arrays.sort(nums);
        return nums;
    }
}
