from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Проверяет, можно ли составить `ransom_note` из букв в `magazine`.

    🔹 **Алгоритм (O(n + m))**:
       1️⃣ Создаём `Counter` (словарь частот) для `ransom_note` и `magazine`.
       2️⃣ Проходим по `ransom_note`, проверяя, хватает ли каждой буквы в `magazine`.
       3️⃣ Если хотя бы одной буквы не хватает, возвращаем `False`, иначе `True`.

    🔹 **Временная сложность**:
       - `O(n + m)`, где `n` — длина `ransom_note`, `m` — длина `magazine`.
       - `Counter` работает за `O(n)`, а проверка за `O(n)`.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как в `Counter` может быть максимум 26 букв английского алфавита.

    :param ransom_note: str - Строка, которую нужно составить.
    :param magazine: str - Строка с буквами, из которых можно составлять.
    :return: bool - `True`, если возможно, иначе `False`.
    """
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False  # Если букв не хватает, вернуть False

    return True  # Если хватает всех букв, вернуть True


# 🔹 Тесты
print(can_construct("a", "b"))  # ✅ False
print(can_construct("aa", "ab"))  # ✅ False
print(can_construct("aa", "aab"))  # ✅ True
print(can_construct("hello", "hlellohe"))  # ✅ True
print(can_construct("abc", "acbd"))  # ✅ True
