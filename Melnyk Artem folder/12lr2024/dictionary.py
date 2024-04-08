my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict['key1'])  # Виведе: value1
my_dict['key4'] = 'value4'
if 'key1' in my_dict:
    print('Key found!')
    keys = my_dict.keys()
values = my_dict.values()