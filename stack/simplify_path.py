def simplify_path(path: str) -> str:
    """
    Упрощает абсолютный путь, убирая "..", ".", и избыточные слэши.

    🔹 **Метод**:
        - Разбиваем `path` по `/`.
        - Используем стек `stack` для хранения имен папок.
        - `..` → удаляет последний элемент в `stack` (если есть).
        - `.` и пустые строки → игнорируются.
        - Итоговый путь собирается из `stack`.

    🔹 **Сложность**:
        - `O(n)`, где `n` — длина строки `path`.

    ✅ **Пример работы**:
       ```
       simplify_path("/home/")       → "/home"
       simplify_path("/../")         → "/"
       simplify_path("/home//foo/")  → "/home/foo"
       simplify_path("/a/./b/../../c/") → "/c"
       ```
    """
    stack = []

    for part in path.split("/"):  # Разбиваем по "/"
        if part == "..":
            if stack:
                stack.pop()  # Поднимаемся на уровень выше
        elif part and part != ".":  # Игнорируем пустые части и "."
            stack.append(part)

    return "/" + "/".join(stack)  # Формируем путь, начиная с "/"

# 🔹 Тесты
print(simplify_path("/home/"))  # ✅ "/home"
print(simplify_path("/../"))  # ✅ "/"
print(simplify_path("/home//foo/"))  # ✅ "/home/foo"
print(simplify_path("/a/./b/../../c/"))  # ✅ "/c"
print(simplify_path("/a/../../b/../c//.//"))  # ✅ "/c"
print(simplify_path("/a//b////c/d//././/.."))  # ✅ "/a/b/c"
