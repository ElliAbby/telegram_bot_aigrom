def simple_num(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

num = int(input("Введите число для проверки на его простоту: "))
print(simple_num(num))