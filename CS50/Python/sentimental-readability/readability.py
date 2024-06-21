# TODO
import math

def calculate_cli(text):
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    cli = (0.0588 * ((letters / words) * 100)) - (0.296 * ((sentences / words) * 100)) - 15.8

    return round(cli)

def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1

    return letters

def count_words(text):
    words = 0
    for char in text:
        if char.isspace() and not char in ['.', '!', '?']:
            words += 1
    # Count the last word if it doesn't end with punctuation.
    if text and not text[-1].isspace():
        words += 1

    return words

def count_sentences(text):
    sentences = 0
    for char in text:
        if char in ['.', '!', '?']:
            sentences += 1

    return sentences

def main():
    sentence = input("Test: ")

    cli = calculate_cli(sentence)

    if cli < 1:
        print("Before Grade 1")
    elif cli >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {cli}")


main()
