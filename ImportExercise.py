import math
def distance(x_1: int, y_1: int, x_2: int, y_2: int) -> None:
    print(math.sqrt(((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2)))

def main() -> None:
    distance(3, 5, -1, 2)


if __name__ == '__main__':
    main()
