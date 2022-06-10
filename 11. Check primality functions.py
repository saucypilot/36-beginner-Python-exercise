def divisorCalc():
    dividend = int(input("Please enter a number to see its divisor: "))
    divisor_list = [divisor for divisor in range(1, dividend + 1) if (dividend % divisor) == 0]
    return divisor_list
print(divisorCalc())
