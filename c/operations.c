#include <stdio.h>

int main()
{
    int a = 0, b = 1, c = 2, d = 3, e = 4;
    a = b - c + d * e;
    printf("%d \n", a);

    float f = 0., g = 1., h = 2.3, prod;
    prod = f + g * h;
    printf("%f \n", prod);

    return 0;
}