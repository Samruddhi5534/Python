def Fibo(terms2):
    f1 = 0
    yield f1
    if terms2 > 1:  # Only yield the second term if terms2 is greater than 1
        f2 = 1
        yield f2

        for _ in range(terms2 - 2):
            f3 = f1 + f2
            yield f3
            f1, f2 = f2, f3  # Update f1 and f2 for the next iteration

# Main body
terms1 = int(input("How many terms: "))
gen = Fibo(terms1)

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
