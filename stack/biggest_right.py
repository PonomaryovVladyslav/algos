def find_biggest_right(nums):
    """
    Находит ближайший больший элемент справа для каждого числа в `nums`.

    🔹 **Метод**: Monotonic Stack (убывающий стек)
    🔹 **Сложность**: O(n), так как каждый элемент добавляется и удаляется 1 раз.

    ✅ **Пример работы**:
       ```
       Вход: [4, 1, 2, 5, 3]
       Выход: [5, 2, 5, -1, -1]
       ```
    """
    biggest_right = [-1] * len(nums)  # Ответ по умолчанию (-1, если нет большего)
    stack = []  # Монотонный стек (убывает)

    # Двигаемся справа налево
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()  # Убираем ненужные элементы из стека
        if stack:
            biggest_right[i] = stack[-1]  # Следующий больший элемент
        stack.append(nums[i])  # Добавляем текущий элемент

    return biggest_right

# 🔹 Тестируем
nums1 = [4, 1, 2, 5, 3]
nums2 = [10, 3, 7, 2, 8]
nums3 = [2, 7, 3, 5, 1, 6, 9, 8]
nums4 = [5, 4, 3, 2, 1]

print(find_biggest_right(nums1))  # ✅ [5, 2, 5, -1, -1]
print(find_biggest_right(nums2))  # ✅ [-1, 7, 8, 8, -1]
print(find_biggest_right(nums3))  # ✅ [7, 9, 5, 6, 6, 9, -1, -1]
print(find_biggest_right(nums4))  # ✅ [-1, -1, -1, -1, -1]
