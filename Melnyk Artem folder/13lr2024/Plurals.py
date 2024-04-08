my_set = {1, 2, 3, 4, 5}
my_set.add(1)  # Не змінить множину, бо 1 вже є в ній
my_set.add(6)  # Додасть 6 до множини
if 2 in my_set:
    print('2 є в множині')
    set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2  # Об'єднання множин
intersection_set = set1 & set2  # Перетин множин
difference_set = set1 - set2  # Різниця множин (елементи, які є в першій множині, але не в другій)
symmetric_difference_set = set1 ^ set2  # Симетрична різниця множин (елементи, які є лише в одній з множин)