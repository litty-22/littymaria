import itertools

def gen_perm(n):
    num = list(range(1, n+1))
    perms = itertools.permutations(num)
    perms_list = list(perms)
    print(len(perms_list))
    for perm in perms_list:
        print(" ".join(map(str, perm)))

def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
    gen_perm(n)

if __name__ == "__main__":
    main()
