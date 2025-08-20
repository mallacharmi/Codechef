// Last updated: 8/20/2025, 5:41:42 PM

char* concatHex36(int n) {
    char hex[100], hex36[100];
    sprintf(hex, "%X", n * n);
    int m = n * n * n;
    int len = 0;
    char* p = hex36;
    if (m == 0) {
        hex36[0] = '0';
        len = 1;
    } else {
        while (m) {
            int rem = m % 36;
            if (rem < 10) {
                *p++ = rem + '0';
            } else {
                *p++ = rem - 10 + 'A';
            }
            m /= 36;
            len++;
        }
    }
    char* res = malloc((strlen(hex) + len + 1) * sizeof(char));
    sprintf(res, "%s", hex);
    p = hex36 + len - 1;
    for (int i = strlen(hex); i < strlen(hex) + len; i++) {
        res[i] = *p--;
    }
    res[strlen(hex) + len] = '\0';
    return res;
}
