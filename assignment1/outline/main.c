#include <stdio.h>

// #define DEBUG
/*
 * Notes:
 *
 * - arrays will contain no duplicates
 */

void swap(long long *a, long long *b);
int compare(long long *a);
void percolate(long long *a, long long size);
void bubblesort(long long *a, long long size);
void fill(long long *a, long long size);
void printArray(long long *a, long long size);

int main() {
    long long size = 8;
    long long a[size];
    fill(a, size);
    printArray(a, size);
    printf("\n");
    bubblesort(a, size);
    printArray(a, size);
    return 0;
}

void printArray(long long *a, long long size){
    long i;
    for(i = 0; i < size; i++){
        printf("%lld ", a[i]);
    }
}

/**
 * Percolate: moves the largest item in the input array to the last index
 * @param a address array
 * @param size of array
 */
void percolate(long long *a, long long size) {
    long long i;
    for (i = 0; i < size - 1; i++) {
        if (compare(a + i)) { // a[i] > a[i + 1]
            swap(a + i, a + i + 1);
        }
    }
}

/**
 * Swaps the two integers
 * @param a addresses of an integer
 * @param b addresses of another integer
 */
void swap(long long *a, long long *b){
#ifdef DEBUG
    printf("Old A: %lld Old B: %lld\n", *a, *b);
#endif
    long long temp = *a;
    *a = *b;
    *b = temp;
#ifdef DEBUG
    printf("New A: %lld New B: %lld\n", *a, *b);
#endif
}


/**
 * Compare value at address a & value at address a+8
 * if a > a+8, return true (non-zero)
 * else false (zero)
 * Note: a == a+8 = false
 * @param a an address
 * @return 0 (false) or non-zero (true)
 */
int compare(long long *a){
    long long *next;
    next = a + 1;
#ifdef DEBUG
    printf("Current Value: %lld\n", *a);
    printf("Next Value: %lld\n", *next);
#endif
    if(*a > *next){
        return 1;
    }
    return 0;
}


/**
 * Bublesort (sorts array) iterates from n (size of the array) down to 2
 * @param a address of array
 * @param size size of array
 */
void bubblesort(long long *a, long long size){
    long long i;
    for(i = size; i > 1; i--){
        percolate(a, size);
    }
};

/**
 * Populates array with consecutive 8-byte integers in reverse-sorted (high to low) order
 * @param a address of array
 * @param size of array
 */
void fill(long long *a, long long size){
    long long i;
    for(i = 0; i < size; i++){
        a[i] = size-i; // + 8
    }
};
