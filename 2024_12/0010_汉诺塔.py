def hanoi(n, a, b, c):
    if n == 1:
        print(f' {a} --> {c}')
    else:
        hanoi(n - 1, a, c, b)      # 将上一层的所有从 a --> b
        hanoi(1, a, b, c)       # 那么 a 上就只有最底下的一块了，将这个最大的块移动到 c 上
        hanoi(n - 1, b, a, c)      # 再将之前的 n-1 块移到 c 上


def get_n():
    while True:
        n = input("Please input n: ")
        try:
            n = int(n)
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():  # test
    n = get_n()
    a, b, c = 'A', 'B', 'C'
    hanoi(n, a, b, c)


if __name__ == "__main__":
    main()
