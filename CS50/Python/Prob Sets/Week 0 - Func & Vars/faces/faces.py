# Return input with converter emoji
def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

# Function called main that prompts user for input, call convert function on that input and print result
def main():
    string = input()
    result = convert(string)
    print(result)


main()