from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

pattern_name = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
sub_name = r'\1\3\10\4\6\9\7\8'
pattern_phone = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
sub_phone = r'+7(\4)\8-\11-\14\15\17\18\19\20'

contacts_sub_phone = []
contacts_edit = []
cont = []
contacts_new = []
contacts_sub = []

for contact in contacts_list:
    el = ','.join(contact)

    substitution_phone = re.sub(pattern_phone, sub_phone, el)
    sub_split_phone = substitution_phone.split(',')

    # contacts_sub.append(sub_split_phone and sub_split_name)
    contacts_sub_phone.append(sub_split_phone)

for contacts_sub_name in contacts_sub_phone:
    el = ','.join(contacts_sub_name)
    substitution_name = re.sub(pattern_name, sub_name, el)
    sub_split_name = substitution_name.split(',')
    contacts_sub.append(sub_split_name)

for elem in contacts_sub:
    cont.append(elem[0])
    cont.append(elem[1])
    if elem[2] != '':
        cont.append(elem[2])
    if elem[3] != '':
        cont.append(elem[3])
    if elem[4] == 'position':
        cont.append(elem[4])
    elif elem[4] == '':
        cont.append('')
    else:
        cont.append(elem[4])

    if elem[5] != int:
        for find_phone in contacts_sub:
            if find_phone[0] == elem[0] and find_phone[1] == elem[1] and find_phone[5] != '':
                cont.append(find_phone[5])

    if elem[6] != str:
        for find_email in contacts_sub:
            if find_email[0] == elem[0] and find_email[1] == elem[1] and find_email[6] != '':
                cont.append(find_email[6])
    contacts_edit.append(cont)
    cont = []

count = 0

for find_duplicate in contacts_edit:
    for temp in contacts_new:
        if find_duplicate[0] == temp[0] and find_duplicate[1] == temp[1]:
            count += 1

    if count == 0:
        contacts_new.append(find_duplicate)
    count = 0

pprint(contacts_new)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_new)
