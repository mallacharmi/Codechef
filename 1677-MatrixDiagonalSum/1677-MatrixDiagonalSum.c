// Last updated: 8/20/2025, 5:42:07 PM
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0;
    for (int i = 0; i < matSize; i++) {
        sum += mat[i][i]; // Primary diagonal
        if (i != matSize - i - 1) {
            sum += mat[i][matSize - i - 1]; // Secondary diagonal
        }
    }
    return sum;
}
