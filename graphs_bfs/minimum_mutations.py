from collections import deque


def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    """
    Находит минимальное количество мутаций, необходимых для превращения start_gene в end_gene.

    🔹 **Алгоритм (BFS, O(m * n))**:
    1️⃣ Преобразуем `bank` в `set` для быстрого поиска.
    2️⃣ Запускаем BFS:
       - В очереди `deque([(ген, шаги)])` храним текущий ген и количество шагов.
       - Для каждого гена пробуем заменить **каждый символ** на {A, C, G, T}.
       - Если мутация есть в `bank`, добавляем её в очередь.
    3️⃣ Если достигли `end_gene`, возвращаем количество шагов.
    4️⃣ Если нет пути, возвращаем `-1`.

    🔹 **Временная сложность**:
       - `O(m * n)`, где `m` — длина гена (8), `n` — количество генов в `bank`.

    🔹 **Пространственная сложность**:
       - `O(n)`, так как храним `bank` и `queue`.

    :param start_gene: str - Исходный ген.
    :param end_gene: str - Целевой ген.
    :param bank: list[str] - Доступные мутации.
    :return: int - Минимальное количество мутаций или `-1`, если путь невозможен.
    """
    if end_gene not in bank:
        return -1  # Если целевой ген отсутствует в банке, переход невозможен

    bank = set(bank)  # Превращаем bank в множество для быстрого поиска
    queue = deque([(start_gene, 0)])  # (ген, кол-во мутаций)
    possible_chars = ['A', 'C', 'G', 'T']

    while queue:
        gene, mutations = queue.popleft()

        if gene == end_gene:
            return mutations  # Достигли цели

        # Пробуем заменить каждую букву в гене
        for i in range(len(gene)):
            for char in possible_chars:
                if char != gene[i]:  # Меняем только на другую букву
                    new_gene = gene[:i] + char + gene[i + 1:]

                    if new_gene in bank:  # Если мутация допустима
                        queue.append((new_gene, mutations + 1))
                        bank.remove(new_gene)  # Удаляем, чтобы избежать повторных посещений

    return -1  # Если не нашли путь


# 🔹 Тесты
print(min_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # ✅ 1
print(min_mutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # ✅ 2
print(min_mutation("AACCGGTT", "AACCGCTA", ["AACCGGTA"]))  # ✅ -1
