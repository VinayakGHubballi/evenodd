import sys

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    num = int(sys.argv[1])
    print("Result:", check_even_odd(num))
