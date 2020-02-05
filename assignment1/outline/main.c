#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}

/**
 * Percolate
 * @param a
 * @param size
 */
void compare(long long *a, long long size) {
    long long i;
    for (i = 0; i < size - 1; i++) {
        if (compare(a + i)) { // a[i] > a[i + 1]
            swap(a + i, a + i + 1);
        }
    }
}

// Implement the procedure "swap", which takes the addresses of two integers and swaps them.
