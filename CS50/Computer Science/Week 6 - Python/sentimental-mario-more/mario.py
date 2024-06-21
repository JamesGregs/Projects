# TODO
def main():
    while True:
        try:
            x = int(input("Height: "))
            if x in range(1, 9):
                break
        except ValueError:
            print("Please enter an integer.")

    for i in range(1, x + 1):
        spaces = (" " * (x - i))
        hashes = ("#" * i)
        print(f"{spaces}{hashes}  {hashes}")

main()