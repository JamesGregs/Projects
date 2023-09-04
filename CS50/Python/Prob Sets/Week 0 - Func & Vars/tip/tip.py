def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    ld = d.lstrip("$")
    fd = float(ld)
    return (fd)

def percent_to_float(p):
    # TODO
    rd = p.rstrip("%")
    fd = float(rd) / 100
    return (fd)

main()