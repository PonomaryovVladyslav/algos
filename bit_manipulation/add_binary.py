# Задача: Выполнить сложение двух бинарных чисел, представленных в виде строк.
# Дано: две строки `a` и `b`, содержащие бинарные числа.
# Нужно: вернуть сумму в виде бинарной строки.

def add_binary(a: str, b: str) -> str:
    """
    Функция складывает два бинарных числа, представленных в виде строк.

    🔹 Временная сложность: O(n), где `n` — длина самого длинного числа.
    🔹 Пространственная сложность: O(n), так как результат может быть длиной `n+1` (если есть перенос).

    :param a: str - первое бинарное число.
    :param b: str - второе бинарное число.
    :return: str - сумма `a` и `b` в бинарном виде.
    """

    result: list[str] = []
    carry: int = 0

    # Выравниваем строки по длине, добавляя нули в начало
    max_length: int = max(len(a), len(b))
    a, b = a.zfill(max_length), b.zfill(max_length)

    # Складываем побитово справа налево
    for i in range(max_length - 1, -1, -1):
        bit_sum: int = int(a[i]) + int(b[i]) + carry
        result.append(str(bit_sum % 2))  # Добавляем 0 или 1
        carry = bit_sum // 2  # Новый перенос

    if carry:  # Если остался перенос, добавляем в начало
        result.append("1")

    return "".join(result[::-1])  # Разворачиваем и соединяем в строку


# 🔹 Тестируем
print(add_binary("11", "1"))  # Ожидаемый результат: "100"
print(add_binary("1010", "1011"))  # Ожидаемый результат: "10101"
print(add_binary("0", "0"))  # Ожидаемый результат: "0"
print(add_binary("111", "111"))  # Ожидаемый результат: "1110"
print(add_binary("1001", "110"))  # Ожидаемый результат: "1111"


"""
🔹 Анализ сложности:

✅ Временная сложность: **O(n)**
   - Мы выполняем `O(n)` операций, так как обрабатываем каждый бит ровно один раз.
   - Операции `.zfill()` и `.join()` работают за O(n).

✅ Пространственная сложность: **O(n)**
   - Используем `result`, который хранит `n+1` бит (если есть перенос).
   - В худшем случае (например, `111 + 111`) результат будет на 1 бит длиннее.

📌 **Как работает алгоритм?**
1️⃣ **Выравниваем длины чисел** (если одно короче, добавляем `0` в начало).  
2️⃣ **Складываем побитово справа налево**, учитывая `carry`.  
3️⃣ **Формируем результат**, переворачиваем его и соединяем в строку.  
4️⃣ Если остался `carry`, добавляем его в начало.

💡 **Почему мы используем `zfill()`?**
- Это избавляет от необходимости вручную дописывать `0` перед коротким числом.
- `.zfill()` работает за O(n), что не влияет на общую сложность.

"""
