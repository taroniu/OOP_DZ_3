from pprint import pprint
# задача 1

with open('rec.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        # print(line)
        rec_name = line.strip()
        # print(rec_name)
        ing_count = int(file.readline())
        # print(ing_count)
        ingredients = []
        for _ in range(ing_count):
            ing, quantity, unit = file.readline().strip().split(' | ')
            # print(ing)
            # print(quantity)
            # print(unit)
            ingredients.append({'ingregient_name': ing, 'quantity': quantity, 'measure': unit})
        file.readline()
        cook_book[rec_name] = ingredients
# print(cook_book)
# задача 2
def get_shop_list_by_dishes(dishes, person_count):
    eng_list = []
    same_ing_list = []
    element = {}
    for name, ing in cook_book.items():
        if name in dishes:
            for i in ing:
               if i['ingregient_name'] not in element:
                   element[i['ingregient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity'])}
               else:
                   same_ing_list.append(i)

    for i in same_ing_list:
        if i['ingregient_name'] in element:
            # print(i['quantity'], element[i['ingregient_name']]['quantity'])
            element[i['ingregient_name']]['quantity'] = ((element[i['ingregient_name']]['quantity'] +
                                                          int(i['quantity'])) * person_count)
    pprint(element)
# get_shop_list_by_dishes(['Омлет',  'omelette', 'salad', 'sandwich', 'Запеченный картофель', 'Утка по-пекински', 'Фахитос'], 4)
# Задача 3

with open('1.txt', 'r', encoding='utf-8') as file1:
    copy_file1 = file1.readlines()
with open('2.txt', 'r', encoding='utf-8') as file2:
    copy_file2 = file2.readlines()
with open('3.txt', 'r', encoding='utf-8') as file3:
    copy_file3 = file3.readlines()
print(copy_file3)
print(copy_file2)
print(copy_file1)
#
print(len(copy_file3))
print(len(copy_file2))
print(len(copy_file1))

with open('4.txt', 'w') as file4:
    file4.writelines('\n2.txt\n')
    file4.writelines(str(len(copy_file2)))
    copy_file2.extend('\n')
    file4.writelines('\n')
    file4.writelines((copy_file2))
    file4.writelines('\n1.txt\n')
    file4.writelines(str(len(copy_file1)))
    copy_file1.extend('\n')
    file4.writelines('\n')
    file4.writelines((copy_file1))
    file4.writelines('\n3.txt\n')
    file4.writelines(str(len(copy_file3)))
    copy_file3.extend('\n')
    file4.writelines('\n')
    file4.writelines((copy_file3))