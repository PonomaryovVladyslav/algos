numbers = [2,7,11,15]
target = 9

# def two_sum(numbers, target):
#     indices = {}
#     for i in range(len(numbers)):
#         complement = target - numbers[i]
#         if complement in indices:
#             return [indices[complement]+1, i+1]
#         indices[numbers[i]] = i

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


print(two_sum(numbers, target))