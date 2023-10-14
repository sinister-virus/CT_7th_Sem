# Euclidean Algorithm
# to compute GCD
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Driver code
if __name__ == "__main__":
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print("gcd(", a, ",", b, ") = ", gcd(a, b))