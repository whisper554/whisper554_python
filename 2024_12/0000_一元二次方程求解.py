import math

def get_number(prompt):     # 获取并判断数值
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("请输入一个有效的数值！")
            
            
def main():     # 获取 a, b, c 的值，并确保 a 不为 0
    while True:
        a = get_number("请输入系数 a：")
        if a != 0:
            break
        else:
            print("系数 a 不能为 0，请重新输入！")

    b = get_number("请输入系数 b：")
    c = get_number("请输入系数 c：")

    solutions = quadratic(a, b, c)
    print("方程的解为：", solutions)


def quadratic(a, b, c):     # 判读最终结果
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "方程无实数解"
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2


if __name__ == "__main__":
    main()
