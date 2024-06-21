#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get height
    int x;
    do
    {
        x = get_int("Height: ");
    }
    while (x < 1 || x > 8);

    // print the pyramid
    // each row have spaces, left hash, gap, right hash --> "#  #"

    for (int i = 0; i < x; i++)
    {
        for (int s = 1; s < x - i; s++)
        {
            printf(" ");
        }
        for (int h = 0; h < i + 1; h++)
        {
            printf("#");
        }
        printf("  ");
        for (int h = 0; h < i + 1; h++)
        {
            printf("#");
        }
        printf("\n");
    }
}