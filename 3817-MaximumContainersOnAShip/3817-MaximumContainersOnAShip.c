// Last updated: 8/20/2025, 5:41:31 PM
int maxContainers(int n, int w, int maxWeight) {
    int totalCells = n * n;
    int maxByWeight = maxWeight / w;
    return totalCells < maxByWeight ? totalCells : maxByWeight;
}
