def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Вычисляем текущую площадь контейнера
        water = (right - left) * min(height[left], height[right])
        max_water = max(max_water, water)

        # Двигаем указатели, уменьшая расстояние
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
