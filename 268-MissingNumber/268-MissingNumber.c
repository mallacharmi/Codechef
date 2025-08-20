// Last updated: 8/20/2025, 5:43:17 PM
int missingNumber(int* nums, int numsSize) {
    int a=(numsSize*(numsSize+1))/2;
    int arr_sum=0;
    for(int i=0;i<numsSize;i++)
    {
        arr_sum=arr_sum+nums[i];
    
    }
    return a-arr_sum;
}