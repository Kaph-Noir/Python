from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    elif (x == 2 or x == 3):
        return True
    else:
        n = 2
        while sqrt(x) >= n:
            if x%n != 0:
                n += 1
            else:
                return False
        return True

if __name__ == "__main__":
    i = int(input("input: "))
    p = is_prime(i)
    print(p)