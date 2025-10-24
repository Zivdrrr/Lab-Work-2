def f(x):
    return x**3 - x - 3

def bisection(f, a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
epsilon = float(input("точність: "))

root = bisection(f, a, b, epsilon)

print(f"\n Корінь: x = {root:.6f}")
print(f"Перевірка: f(x) = {f(root):.6e}")
