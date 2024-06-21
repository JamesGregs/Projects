#include <math.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>

int calculate_cli(string text);
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Take a sentence to correlate with reading level
    // (Formula for computing reading level of a text) Coleman-Liau index = 0.0588 * L - 0.296 * S - 15.8
    // L - average number of letters per 100 words in the text, S - average number of sentence per 100 words in the text
    string sentence = get_string("Test: ");

    // Calculating reading level
    int letters = count_letters(sentence);
    int words = count_words(sentence);
    int sentences = count_sentences(sentence);
    float cli = (0.0588 * (((float) letters / words) * 100)) - (0.296 * (((float) sentences / words) * 100)) - 15.8;
    // printf("letter: %i\nwords: %i\nsentences: %i\ncli: %f\n", letters, words, sentences, cli);

    // Print reading level
    if (round(cli) < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (round(cli) >= 16)
    {
        printf("Before Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(cli));
    }
}

// counting letters - create a loop that if a char in a string is only a-z index will count
int count_letters(string text)
{
    int i = 0;
    int n = strlen(text);
    int letters = 0;
    while (i < n)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        else
        {
            letters += 0;
        }
        i++;
    }
    return letters;
}

// Counting words - create a loop that counts when a " " is detected.
// This will also count when detect a "." "!" "?" for the last word
int count_words(string text)
{
    int i = 0;
    int n = strlen(text);
    int words = 0;
    while (i < n)
    {
        if ((isspace(text[i]) && !ispunct(text[i - 1])) ||
            (ispunct(text[i]) && text[i] != '-' && text[i] != '\'' && text[i] != '\"'))
        {
            words++;
        }
        else
        {
            words += 0;
        }
        i++;
    }
    return words;
}

// Counting sentence - create a loop that will stop counting
// when a  "." "!" "?" char is detected in the string
int count_sentences(string text)
{
    int i = 0;
    int n = strlen(text);
    int sentence = 0;
    while (i < n)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
        else
        {
            sentence += 0;
        }
        i++;
    }
    return sentence;
}