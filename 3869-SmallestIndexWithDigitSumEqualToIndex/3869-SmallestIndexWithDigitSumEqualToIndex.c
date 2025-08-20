// Last updated: 8/20/2025, 5:41:32 PM
int digitSum(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        if (digitSum(nums[i]) == i) {
            return i;
        }
    }
    return -1;
}
