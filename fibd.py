def mortal_fibo(n, m):
    ages = [0] * m
    ages[0] = 1
    for month in range(1, n):
        newb = sum(ages[1:])
        for i in range(m - 1, 0, -1):
            ages[i] = ages[i - 1]
        ages[0] = newb
    return sum(ages)

def main():
    with open('input.txt', 'r') as file:
        n, m = map(int, file.readline().split())

    result = mortal_fibo(n, m)
    print(result)

if __name__ == "__main__":
    main()