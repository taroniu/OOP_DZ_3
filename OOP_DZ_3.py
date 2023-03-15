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
files = ['1.txt', '2.txt', '3.txt']
result = []
for i in files:
    with open(i, 'r', encoding='utf-8') as f:
        file = f.readlines()
        result += [[i, len(file), file]]

def sort(i):
    return i[1]
result.sort(key=sort)
for data in result:
    with open('file5.txt', 'a', encoding='utf-8') as f:
        f.write(str(data[0]) + '\n')
        f.write(str(data[1]) + '\n')
        f.writelines(data[2] + ['\n'*2])





#
# with open('4.txt', 'w') as file4:
#     file4.writelines('\n2.txt\n')
#     file4.writelines(str(len(copy_file2)))
#     copy_file2.extend('\n')
#     file4.writelines('\n')
#     file4.writelines((copy_file2))
#     file4.writelines('\n1.txt\n')
#     file4.writelines(str(len(copy_file1)))
#     copy_file1.extend('\n')
#     file4.writelines('\n')
#     file4.writelines((copy_file1))
#     file4.writelines('\n3.txt\n')
#     file4.writelines(str(len(copy_file3)))
#     copy_file3.extend('\n')
#     file4.writelines('\n')
#     file4.writelines((copy_file3))