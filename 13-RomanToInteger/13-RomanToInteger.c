// Last updated: 8/20/2025, 5:44:42 PM
int romanToInt(char* s) {
    int romanValues[256] = {0}; // ASCII mapping for quick lookup
    romanValues['I'] = 1;
    romanValues['V'] = 5;
    romanValues['X'] = 10;
    romanValues['L'] = 50;
    romanValues['C'] = 100;
    romanValues['D'] = 500;
    romanValues['M'] = 1000;

    int total = 0;
    int prevValue = 0;
    
    while (*s) {
        int currentValue = romanValues[*s];
        
        if (currentValue > prevValue) {
            total += currentValue - 2 * prevValue;  // Correct previous addition
        } else {
            total += currentValue;
        }
        
        prevValue = currentValue;
        s++;
    }
    
    return total;
}
