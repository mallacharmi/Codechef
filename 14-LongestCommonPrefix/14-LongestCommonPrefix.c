// Last updated: 8/20/2025, 5:44:30 PM
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";

    // Allocate memory for the prefix (assuming max length 200)
    char* prefix = (char*)malloc(201 * sizeof(char));
    strcpy(prefix, strs[0]);  // Start with the first string

    for (int i = 1; i < strsSize; i++) {
        int j = 0;
        // Compare characters of prefix with current string
        while (prefix[j] && strs[i][j] && prefix[j] == strs[i][j]) {
            j++;
        }
        // Null-terminate at the point of mismatch
        prefix[j] = '\0';

        // If prefix becomes empty, return ""
        if (prefix[0] == '\0') return prefix;
    }

    return prefix;
}
