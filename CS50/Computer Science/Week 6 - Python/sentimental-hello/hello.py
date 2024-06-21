# TODO
def hello(to="world"):
    print(f"hello, {to}")


def main():
    # Ask user for their name, remove whitespace and auto capitalize
    name = input("What's your name? ").strip()
    # Say hello to the user
    hello(name)

main()