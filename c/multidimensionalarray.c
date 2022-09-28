#include <stdio.h>

int main()
{
    int myArray[3][4][2] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24};
    printf("myArray first element is %d \n", myArray[0][3][0]);

    char myOtherArray[2][3] = {"A", "B", "C", "D", "E", "F"};
    printf("myOtherArray first element is %c \n", myOtherArray[0][0]);
    return 0;
}