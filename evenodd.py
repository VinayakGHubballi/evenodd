def evenandodd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    num = int(input("Enter value num: "))

    print("Even or odd: ", evenandodd(num))

