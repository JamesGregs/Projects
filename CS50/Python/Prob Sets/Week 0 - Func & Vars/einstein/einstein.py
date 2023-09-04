# Prompt for mass as an integer (in kilograms)
m = int(input("m: "))

# Output the equivalent number of Joules as an integer
c = 300000000
E = m * pow(c, 2)
print("E:", E)