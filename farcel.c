#include <stdio.h>
main() 
{
    int far,cel; 
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    far = lower;
    printf("far\tcel\n");
    while (far <= upper ) {
        cel = 5 * ( far-32) / 9; 
        printf("%d\t%d\n",far, cel);
        far = far + step; 
    }

}