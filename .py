def hn(n):
    if not n:
        return None

    highest = n[0]

    for num in n:
        if num > highest:
            highest = num
    return highest

numbers_list = [3, 5, 1, 22, -4, 78, 0]
highest_number = hn(numbers_list)
print("The highest number in the list is:", highest_number)