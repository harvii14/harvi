yr = int(input("Enter a year: "))

if yr %4 ==0 or yr%100 == 0 or yr%400 == 0:
    print(f"{yr} is a leap year.")
else:
    print(f"{yr} is not a leap year.")
