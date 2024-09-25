def Prime(num):
    if num <= 1:
        print("Number is Not Prime")
        return

    flag = 0
    for i in range(2, int(num ** 0.5) + 1):  # Check up to the square root of num
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print("Number is Prime")
    else:
        print("Number is Not Prime")

def Fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    print("Factorial of Given number is:", f)

# Main body
n = int(input("Enter any number to Check: "))
Prime(n)
Fact(n)
