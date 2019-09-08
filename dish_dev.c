/*
**      Ivan Titkov ititkov42@gmail.com
*/

#include <math.h>
#include <stdio.h>

float       rounding(float rad)
{
    float   scale = 0.25;
    int     whole = 0;
    float   rem = 0;
    int     i = 0;

    whole = rad;
//    printf ("rad = %f, whole part of rad = %d\n", rad, whole);
    rem = rad - whole;
    printf("reminder = %f   ", rem);
    while (rem >= scale)
    {
        rem -= scale;
        i++;
    }
    if (rem >= scale/2)
        rem = scale * (i + 1);
    else
        rem = scale * i;
    return (whole + rem);
}

void        divide_dish(void)
{
    float   d = 90;
    float   pi = 3.14;          // Увеличить точность до 6 знаков
    float   s_cir = 0;
    int     cir = 8;
    float   prev_rad = 0;
    float   rad_arr[8];
    int     i = 0;

    s_cir = pi*pow(d/2, 2)/cir;
    while (i < 8 - 1)
    {
        rad_arr[i] = sqrt(pow(prev_rad, 2) + s_cir/pi);
        prev_rad = rad_arr[i++];
    }
    i = -1;
    while (++i < 8)
    {
        printf("Radius %d = %f    ", i, rad_arr[i]);
        printf("rounded rad = %f\n", rounding(rad_arr[i]));
    }
}

int         main(void)
{
    divide_dish();
    return (0);
}
