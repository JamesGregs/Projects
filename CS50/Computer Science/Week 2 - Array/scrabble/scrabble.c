#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins! %i %i\n", score1, score2);
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins! %i %i\n", score1, score2);
    }
    else
    {
        printf("Tie! %i %i\n", score1, score2);
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    // string uppercase = word;
    int sum = 0;
    for (int i = 0, n = strlen(word); i < n; i++) // Convert all lower case to upper case
    {
        if (islower(word[i]))
        {
            word[i] = toupper(word[i]);
            word[i] -= 65;
            // printf("index: %i ascii: %i char: %c\n", i, word[i], word[i]); //for checking if conversion to upper is correct
            if (word[i] >= 0 && word[i] <= 25)
            {
                int j = word[i];
                sum += POINTS[j];
            }
            else
            {
                sum += 0;
            }
        }
        else
        {
            word[i] -= 65;
            if (word[i] >= 0 && word[i] <= 26)
            {
                int j = word[i];
                sum += POINTS[j];
            }
            else
            {
                sum += 0;
            }
        }
    }
    return sum;
}

    //ascii[i] = uppercase[i] - 65;
    // printf("%s\n", uppercase);

    //string ascii = word;
    //for (int j = 0, n = strlen(word); j < n; j++) // The integer will be subtracted by 65 to align with point array
    //{
    //    ascii[j] = word[j] - 65;
    //}
    //printf("%s\n", ascii);

    //int sum = 0;
    //for (int k = 0, n = strlen(word); k < n; k++) // Converted integer greater than 0 or and less than 26 are only considered
    //{
    //    int m = ascii[k];
    //    if (m > 0 && m < 26)
    //    {
    //        sum += ascii[k];
    //    }
    //    else
    //    {
    //        sum += 0;
    //    }
    //}
    //return sum;
