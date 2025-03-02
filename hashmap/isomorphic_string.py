def is_isomorphic(s: str, t: str) -> bool:
    """
    Проверяет, являются ли две строки изоморфными.

    🔹 **Определение**:
       Две строки изоморфны, если символы одной строки можно взаимно заменить
       на символы другой строки, сохраняя порядок, без конфликтов.

    🔹 **Алгоритм (O(n))**:
       1️⃣ Проверяем, что длины строк совпадают (`O(1)`).
       2️⃣ Создаём два словаря:
          - `map_s_t`: Сопоставляет символы `s` → `t`
          - `map_t_s`: Сопоставляет символы `t` → `s`
       3️⃣ Проходим по строкам (`O(n)`) и проверяем:
          - Если символ уже есть в `map_s_t`, но сопоставлен с другим → `False`
          - Если символ уже есть в `map_t_s`, но сопоставлен с другим → `False`
          - Иначе записываем соответствие в оба словаря.
       4️⃣ Если прошли всю строку без конфликтов → `True`

    🔹 **Временная сложность**:
       - `O(n)`, где `n` — длина строки.

    🔹 **Пространственная сложность**:
       - `O(1)`, так как используем фиксированные словари (максимум 256 символов).

    :param s: str - Первая строка.
    :param t: str - Вторая строка.
    :return: bool - `True`, если строки изоморфны, иначе `False`.
    """
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for char_s, char_t in zip(s, t):
        if (char_s in map_s_t and map_s_t[char_s] != char_t) or \
           (char_t in map_t_s and map_t_s[char_t] != char_s):
            return False  # Нарушено уникальное соответствие

        map_s_t[char_s] = char_t
        map_t_s[char_t] = char_s

    return True


# 🔹 Тесты
print(is_isomorphic("egg", "add"))      # ✅ True  (e → a, g → d)
print(is_isomorphic("foo", "bar"))      # ✅ False (f → b, но o нельзя отобразить на две буквы)
print(is_isomorphic("paper", "title"))  # ✅ True  (p → t, a → i, e → l, r → e)
print(is_isomorphic("ab", "aa"))        # ✅ False (a → a, но b → a конфликтует)
print(is_isomorphic("abcd", "baba"))    # ✅ False (конфликт в символах)

