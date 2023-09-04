def hello(to="world"):
    print(f"hello, {to}")


def main():
    hello()
    # Ask user for their name, remove whitespace and auto capitalize
    name = input("what's your name? ").strip()
    # Say hello to the user
    hello(name)

main()