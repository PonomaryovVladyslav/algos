def length_of_lis(nums: list[int]) -> int:
    """
    Функция для нахождения длины **наибольшей возрастающей подпоследовательности (LIS)**.

    🔹 Алгоритм (Динамическое программирование O(n^2)):
    1️⃣ Создаём массив `dp`, где `dp[i]` — длина LIS, заканчивающейся на `nums[i]`.
    2️⃣ Инициализируем `dp[i] = 1`, так как минимальная LIS для каждого элемента — он сам.
    3️⃣ Для каждого `nums[i]` проверяем все `nums[j]`, где `j < i`:
        - Если `nums[j] < nums[i]`, можем продлить LIS: `dp[i] = max(dp[i], dp[j] + 1)`.
    4️⃣ Итоговый ответ — `max(dp)`.

    🔹 Временная сложность: **O(n²)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(n)** — массив `dp`.

    :param nums: list[int] - входной массив чисел.
    :return: int - длина наибольшей возрастающей подпоследовательности.
    """

    if not nums:
        return 0

    dp = [1] * len(nums)  # Минимальная длина LIS — 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # Если можем продлить подпоследовательность
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Наибольшее значение в dp — ответ


# 🔹 Тестируем
print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))  # 4
print(length_of_lis([7, 7, 7, 7, 7, 7, 7]))  # 1
print(length_of_lis([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6


# 🔹 Оптимизированный алгоритм O(n log n) с `bisect`
from bisect import bisect_left

def length_of_lis_optimized(nums: list[int]) -> int:
    """
    Функция для нахождения длины **наибольшей возрастающей подпоследовательности (LIS)**
    с использованием **бинарного поиска O(n log n)**.

    🔹 Алгоритм (Гребёнка O(n log n)):
    1️⃣ Используем массив `dp`, где `dp[i]` — наименьший возможный элемент для LIS длины `i + 1`.
    2️⃣ Для каждого `num` ищем место в `dp` через `bisect_left`:
        - Если `num` больше всех в `dp`, добавляем его (LIS увеличилась).
        - Иначе заменяем ближайший больший элемент (обновляем LIS).
    3️⃣ Итоговая длина `dp` — это ответ.

    🔹 Временная сложность: **O(n log n)** — `n` итераций с `log n` поиском.
    🔹 Пространственная сложность: **O(n)** — массив `dp`.

    :param nums: list[int] - входной массив чисел.
    :return: int - длина наибольшей возрастающей подпоследовательности.
    """

    dp = []  # Храним наименьшие последние элементы LIS
    for num in nums:
        i = bisect_left(dp, num)  # Найти место для num
        if i == len(dp):
            dp.append(num)  # Если num больше всех, добавляем
        else:
            dp[i] = num  # Иначе заменяем существующий элемент
    return len(dp)


# 🔹 Тестируем оптимизированную версию
print(length_of_lis_optimized([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(length_of_lis_optimized([0, 1, 0, 3, 2, 3]))  # 4
print(length_of_lis_optimized([7, 7, 7, 7, 7, 7, 7]))  # 1
print(length_of_lis_optimized([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6
