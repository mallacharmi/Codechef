// Last updated: 8/20/2025, 5:44:52 PM
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if complement exists in the map
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            
            // Add the current element to the map
            map.put(nums[i], i);
        }
        
        // Return an empty array if no solution is found (should not happen per problem statement)
        return new int[] {};
    }
}
