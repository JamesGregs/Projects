def calculate_checksum(number):
    num_list = [int(digit) for digit in str(number)]  # Convert the number to a list of digits
    num_list.reverse()  # Reverse the list to start from the rightmost digit
    total = 0

    for i in range(len(num_list)):
        if i % 2 == 1:  # Double every second digit from the right
            double_digit = num_list[i] * 2

            if double_digit > 9:  # If the result is greater than 9, add the digits separately
                total += (double_digit // 10) + (double_digit % 10)
            else:
                total += double_digit
        else:
            total += num_list[i]

    return total

def main():
    while True:
        x = input("Credit Card Number (13-16 digits): ")
        if len(x) in range(13, 17) and x.isdigit():
            break
        else:
            print("INVALID")
            break

    checksum = calculate_checksum(x)
    mc = [51, 52, 53, 54, 55]
    am = [34, 37]
    if (checksum % 10 == 0):
        if len(x) in (13, 16):
            if len(x) == 16:
                if int(x[:2]) in mc:
                    print("MASTERCARD")
                elif int(x[:1]) == 4:
                    print("VISA")
                else:
                    print("INVALID")
            else:
                if int(x[:1]) == 4:
                    print("VISA")
                else:
                    print("INVALID")
        elif len(x) == 15:
            if int(x[:2]) in am:
                print("AMEX")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")


main()
