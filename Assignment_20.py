N = float(input("Enter the number:"))

Result = 'Positive' if N > 0 else ('Negative' if N < 0 else 'Zero')-8
print(f"Sign evalution(Ternary):{Result}")

if(N == 0):
    print("The number is Zero(Even/Odd is not evaluated)")

else:
    if(N % 2 == 0):
        print("The number is Even")

    else:
        print("The number is Odd")        


