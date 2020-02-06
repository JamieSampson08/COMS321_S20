#include <stdio.h>

// #define DEBUG
/*
 * Notes:
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
/*
 * main:
 *      // backup x regs for array
 *      // backup iReg for array pointer X19
 *      // save sizeRg for size of array x20
 *      // B fill
 *      // PRINT all regs
 *      // B bubblesort
 *      // PRINT all regs
 *
 */

void printArray(long long *a, long long size){
    long i; // iReg
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
    long long i; // iReg
    // STUR x19, [xZR, #0] // i = 0
    // percolatLoop:
    //      SUB x9, x19, x20 // i-size
    //      CBZ x9, end // i == size
    //      ADDI x19, #1 // i++
    for (i = 0; i < size - 1; i++) {
        //  BL compare
        //  CBZ, percolateLoop
        if (compare(a + i)) { // a[i] > a[i + 1]
        //  BL swap
            swap(a + i, a + i + 1);
        }
    }
    // end:
    //      B LR
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
    long long temp = *a; // STUR x9, [aReg, #0]
    *a = *b; // STUR aReg, [bReg, #0]
    *b = temp; // STUR bReg, [x9, #0]
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
    next = a + 1; // STUR x10, aReg, #8 ?
#ifdef DEBUG
    printf("Current Value: %lld\n", *a);
    printf("Next Value: %lld\n", *next);
#endif
    // STUR x0, xZR, #0 // return = 0
    // SUB x9, aReg, nextReg
    // CBZ end
    if(*a > *next){ // CMP?
        return 1; // ADDI x0, xZR, #1
    }
    // end:
        // B LR
    return 0;
}


/**
 * Bublesort (sorts array) iterates from n (size of the array) down to 2
 * @param a address of array
 * @param size size of array
 */
void bubblesort(long long *a, long long size){
    long long i; // iReg
    // STUR x19, [x20, #0] // i = size
    // bubblesortLoop:
    //      CBZ x19, end // i == 0
    //      SUBI x19, x19, #1 // i--
    for(i = size; i > 1; i--){
        //  BL precolate
        percolate(a, size);
    }
    //      B bubblesortLoop
    // end:
    //      B LR
};

/**
 * Populates array with consecutive 8-byte integers in reverse-sorted (high to low) order
 * @param a address of array
 * @param size of array
 */
void fill(long long *a, long long size){
    long long i; // iReg
    // STUR x19, [xZR, #0] // i = 0
    // fillLoop:
    //      SUB x9, x19, x20 // i-size
    //      CBZ x9, end // i == size
    //      ADDI x19, #1 // i++
    for(i = 0; i < size; i++){
        a[i] = size-i;
        //  SUB x9, x20, x19 // size - i
        //  STUR aReg, [x9, #x9*8] // a[i] = x9?
    }
    //      B fillLoop
    // end:
    //      B LR // back to main
};
