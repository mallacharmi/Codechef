// Last updated: 8/20/2025, 5:43:43 PM
int singleNumber(int* nums, int numsSize) {
     int result = 0;
    for (int i = 0; i < numsSize; i++) {
        result ^= nums[i];
    }
    return result;
}