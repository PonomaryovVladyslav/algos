def my_sqrt(x: int) -> int:
    """
    Вычисляет целочисленный квадратный корень `⌊sqrt(x)⌋` с помощью бинарного поиска.

    🔹 **Алгоритм**:
       - Используем **бинарный поиск** в диапазоне `[1, x]`.
       - Середина `mid = (left + right) // 2`.
       - Проверяем `mid * mid`:
         - Если `mid^2 == x`, возвращаем `mid`.
         - Если `mid^2 < x`, двигаем `left = mid + 1`.
         - Иначе `right = mid - 1`.
       - Возвращаем `right` как наибольшее значение, удовлетворяющее `right^2 <= x`.

    🔹 **Сложность**:
       - `O(log x)`, так как используем **бинарный поиск**.

    """
    if x == 0:
        return 0

    left, right = 1, x  # Поиск от 1 до x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # Последний корректный mid


# 🔹 Тесты
print(my_sqrt(8))  # ✅ 2
print(my_sqrt(4))  # ✅ 2
print(my_sqrt(0))  # ✅ 0
print(my_sqrt(16))  # ✅ 4
print(my_sqrt(27))  # ✅ 5
print(my_sqrt(1000000))  # ✅ 1000
print(my_sqrt(2147395599))  # ✅ 46339 (пограничный случай)
