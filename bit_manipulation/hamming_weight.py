# Задача: Найти количество единичных битов в двоичном представлении числа.
# Дано: целое число `n`.
# Нужно: вернуть количество `1` в `bin(n)`.

def hamming_weight(n: int) -> int:
    """
    Функция считает количество единичных битов в числе (алгоритм Брайана Кернигана).

    🔹 Временная сложность: O(k), где `k` — количество единиц в числе (обычно O(log n)).
    🔹 Пространственная сложность: O(1), так как используется только одна переменная.

    :param n: int - входное число.
    :return: int - количество битов, равных 1.
    """

    count: int = 0
    while n:
        n &= (n - 1)  # Убираем последний 1
        count += 1
    return count


def hamming_weight_bin(n: int) -> int:
    """
    Функция считает количество единичных битов в числе (через `bin()`).

    🔹 Временная сложность: O(log n), так как `bin(n)` использует O(log n) операций.
    🔹 Пространственная сложность: O(1), так как `bin()` использует фиксированную память.

    :param n: int - входное число.
    :return: int - количество битов, равных 1.
    """

    return bin(n).count('1')


# 🔹 Тестируем
print(hamming_weight(11))  # Ожидаемый результат: 3 (1011)
print(hamming_weight(128))  # Ожидаемый результат: 1 (10000000)
print(hamming_weight(255))  # Ожидаемый результат: 8 (11111111)

print(hamming_weight_bin(11))  # Ожидаемый результат: 3
print(hamming_weight_bin(128))  # Ожидаемый результат: 1
print(hamming_weight_bin(255))  # Ожидаемый результат: 8


"""
🔹 Сравнение методов:

1️⃣ `hamming_weight()` (алгоритм Брайана Кернигана)
   - Временная сложность: O(k), где `k` — количество единиц в числе (обычно O(log n)).
   - Пространственная сложность: O(1).
   - Быстрее, если `n` содержит мало единиц (разреженные биты).

2️⃣ `hamming_weight_bin()` (использование `bin()`)
   - Временная сложность: O(log n), так как `bin(n)` использует O(log n) операций.
   - Пространственная сложность: O(1).
   - Простая и читаемая, но немного медленнее из-за преобразования в строку.

✅ Вывод:
   - **Алгоритм Брайана Кернигана быстрее**, если `n` содержит мало `1` (разреженные биты).
   - **Метод `bin(n).count('1')` проще и удобнее**, но работает за O(log n).

💡 **Почему алгоритм Кернигана эффективен?**
- Он **убирает** последнюю `1` за **O(1)** вместо **полного прохода по битам**.
- Работает **быстрее на разреженных числах** (например, `10000001`).

"""
