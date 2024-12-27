def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


def main():
    lst = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    lst1 = sorted(lst, key = by_name)
    print(lst1)

    lst2 = sorted(lst, key = by_score)
    print(lst2)


if __name__ == "__main__":
    main()
