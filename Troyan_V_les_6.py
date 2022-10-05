
"""1 Задание упрощённый вариант"""
# JSON
# import json
# info = {
#     "first_name": "Vitalii",
#     "last_name": "Troyan",
#     "age": "27"
# }
#
# with open("info.json", "w") as file:
#     json.dump(info, file)
# CSV
# import csv
#
# with open('info.csv', encoding='utf-8') as r_file:
#     file_reader = csv.reader(r_file, delimiter = ",")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы:{",".join(row)}')
#         else:
#             print(f' {row[0]} - {row[1]} и он родился в {row[2]} году. ')
#         count += 1
#     print(f'всего в файле {count}строк.')
# Exel Таблица
# from openpyxl import Workbook
# import datetime
#
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = "Виталий Троян"
#
# # Rows can also be appended
# ws.append(["age", 27])
#
# # Python types will automatically be converted
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("name.xlsx")
"""2 ое задание"""
# file = open("text.txt", "r")
#
# for line in file:
#     line
# print(line)
# "Привет\n "
# "Меня зовут\n"
# "Виталик!\n"
# file.close()