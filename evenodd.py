import sys

def simpl(pr, intr, tm):
    return (pr*intr*tm)/100

if __name__ == "__main__":
    p = int(sys.argv[1])
    i = float(sys.argv[2])
    t = int(sys.argv[3])

    print("SI: ", simpl(p,i,t))

