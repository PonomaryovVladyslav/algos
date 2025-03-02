def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # O(n log n) сортируем массив
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Пропускаем дубликаты
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Пропускаем одинаковые `left` и `right`
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1  # Нам нужно большее число
            else:
                right -= 1  # Нам нужно меньшее число

    return result
