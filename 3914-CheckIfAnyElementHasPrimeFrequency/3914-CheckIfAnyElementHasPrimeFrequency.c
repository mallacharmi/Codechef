// Last updated: 8/20/2025, 5:41:28 PM
bool checkPrimeFrequency(int* nums, int numsSize) {
    int freq[101] = {0};

    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
    }

    for (int i = 0; i <= 100; i++) {
        int count = freq[i];
        if (count > 1) {
            bool isPrime = true;
            for (int j = 2; j * j <= count; j++) {
                if (count % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) return true;
        }
        if (count == 2 || count == 3) return true; // handle small primes
    }

    return false;
}
