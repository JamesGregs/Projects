// Luhn's Algorithm - determining a card number is valid
// Checksum
// 1. Multiply every other digit by 2, starting on second-to-last digit, and then add the product of digit together
// 2. Add the sum to the sum of the digits that are not multipled by 2
// 3. If total's last digit is 0, the number is valid!

// American Express numbers start with 34 or 37
// Most MasterCard numbers start with 51, 52, 53, 54, or 55
// Visa numbers start with 4.

#include <math.h>
#include <cs50.h>
#include <stdio.h>

// function to calculate for checksum using Luhn's Algorithm
long calculate_Checksum(long number)
{
    long sum = 0;
    long tempNum1 = number;
    long tempNum2 = number;
    do
    {
        tempNum1 /= 10;
        long double_digit = 2 * (tempNum1 % 10);
        if (double_digit > 9)
        {
            sum = sum + (double_digit % 10) + (double_digit / 10);
        }
        else
        {
            sum = sum + double_digit;
        }
        tempNum1 /= 10;
    }
    while (tempNum1 > 0);

    //sum
    long checksum = sum;
    for (int j = 0; tempNum2 > 0; j++)
    {
        checksum = checksum + (tempNum2 % 10);
        tempNum2 /= 100;
    }
    return checksum; // return final checksum calculation
}


int main(void)
{
    // prompt for credit card number
    long number;
    do
    {
        number = get_long("Credit Card Number (13-16 digits): ");
    }
    while (number < pow(10, 12) || number > pow(10, 16));

    // count digit length
    int c = 0;
    long count = number;
    while (count != 0)
    {
        count /= 10;
        c++;
    }

    // calculating checksum
    int sum1 = calculate_Checksum(number);

    // assign 1st 2 digit of the card number to a variable
    if (sum1 % 10 == 0)
    {
        int num = number / pow(10, c - 2);

        if (num > 9)
        {
            switch (num)
            {
                case 51:
                case 52:
                case 53:
                case 54:
                case 55:
                    printf("MASTERCARD\n");
                    break;
                case 34:
                case 37:
                    printf("AMEX\n");
                    break;
                default:
                    num /= 10;
                    if (num == 4)
                    {
                        printf("VISA\n");
                    }
                    else
                        printf("INVALID\n");
                    break;
            }
        }
    }
    else
    {
        printf("INVALID\n");
    }
}