def my_pow(x: float, n: int) -> float:
    """
    Вычисляет `x^n` (x в степени n) с помощью бинарного быстрого возведения в степень.

    🔹 **Алгоритм**:
       - Если `n < 0`, переворачиваем `x` и делаем `n` положительным.
       - Используем метод двоичного разложения (`O(log n)`):
         - Если `n` нечетное → умножаем `result` на `x`.
         - Умножаем `x` само на себя (`x *= x`).
         - Двигаем `n` вправо (целочисленное деление на `2`).

    🔹 **Сложность**:
       - `O(log n)`, так как `n` уменьшается вдвое на каждой итерации.
    """
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n:
        if n % 2:  # Если n нечетное
            result *= x
        x *= x  # Умножаем основание на себя
        n //= 2  # Двигаем n вправо (делим на 2)

    return result


# 🔹 Тесты
print(my_pow(2.0, 10))  # ✅ 1024.0
print(my_pow(2.1, 3))  # ✅ 9.261
print(my_pow(2.0, -2))  # ✅ 0.25
print(my_pow(3.0, 5))  # ✅ 243.0
print(my_pow(0.5, 2))  # ✅ 0.25
print(my_pow(10, 0))  # ✅ 1
print(my_pow(2, -3))  # ✅ 0.125
