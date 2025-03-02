from collections import OrderedDict

class LRUCache:
    """
    Реализует кэш с политикой LRU (Least Recently Used) с помощью OrderedDict.

    🔹 **Алгоритм**:
       - Используем `OrderedDict` для хранения пар (ключ, значение) в порядке использования.
       - `get(key)`: Возвращает значение и обновляет порядок (перемещает в конец).
       - `put(key, value)`: Добавляет элемент и при превышении `capacity` удаляет наименее использованный.

    🔹 **Сложность**:
       - `get()`: `O(1)`
       - `put()`: `O(1)`, так как `OrderedDict` поддерживает `move_to_end()` и `popitem()` за `O(1)`.
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Если ключ отсутствует
        self.cache.move_to_end(key)  # Обновляем использование (перемещаем в конец)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Перемещаем в конец (самый новый)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Удаляем первый элемент (LRU)


# 🔹 Тестирование
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # ✅ 1 (обновляется в конец)
lru.put(3, 3)  # ❌ Удаляет 2 (наименее использованный)
print(lru.get(2))  # ✅ -1 (удалён)
lru.put(4, 4)  # ❌ Удаляет 1 (LRU)
print(lru.get(1))  # ✅ -1 (удалён)
print(lru.get(3))  # ✅ 3
print(lru.get(4))  # ✅ 4
