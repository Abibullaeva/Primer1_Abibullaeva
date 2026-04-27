'''# obchaya chast
# cont rascheta
print("РЕЗУЛЬТАТЫ ОБЩЕЙ ЧАСТИ")
from sympy import *
k, T, C, L = symbols("k T C L")

# 1sposob-lineyniy
C_ost = 100000
Am_Ist = []
C_ost_Ist = []
for i in range(5):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 100000, T: 5, L: 0})
    Am_Ist.append(round(Am.subs({C: 100000, T: 5, L: 0}), 2))
    C_ost_Ist.append(round(C_ost, 2))
print("Am_Ist:", Am_Ist)
print("C_ost_Ist:", C_ost_Ist)
# 2sposob-umen ostatok
Aj = 0
C_ost = 100000
Am_Ist_2 = []
C_ost_Ist_2 = []
for i in range(5):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 100000, T: 5, k: 2})
    Am_Ist_2.append(round(Am.subs({C: 100000, T: 5, k: 2}), 2))
    Aj += Am
    C_ost_Ist_2.append(round(C_ost, 2))
print("Am_Ist_2:", Am_Ist_2)
print("C_ost_Ist_2:", C_ost_Ist_2)
# 3.1
C_ost = 30000
Am_Ist = []
C_ost_Ist = []
for i in range(8):
    Am = (C - L) / T
    C_ost -= Am.subs({C: 30000, T: 8, L: 0})
    Am_Ist.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
    C_ost_Ist.append(round(C_ost, 2))
print("Am_Ist:", Am_Ist)
print("C_ost_Ist:", C_ost_Ist)
# 3.2
Aj = 0
C_ost = 30000
Am_Ist_2 = []
C_ost_Ist_2 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 30000, T: 8, k: 2})
    Am_Ist_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
    Aj += Am
    C_ost_Ist_2.append(round(C_ost, 2))
print("Am_Ist_2:", Am_Ist_2)
print("C_ost_Ist_2:", C_ost_Ist_2)
# 3.3cont tabl vivoda
import pandas as pd

Y = range(1, 9)
print("")
table1 = list(zip(Y, C_ost_Ist, Am_Ist))
table2 = list(zip(Y, C_ost_Ist_2, Am_Ist_2))
tfame = pd.DataFrame(table1, columns=(["Y", "C_ost_Ist", "Am_Ist"]))
tfame2 = pd.DataFrame(table2, columns=(["Y", "C_ost_Ist_2", "Am_Ist_2"]))
print(tfame)
print(tfame2)
# 3.4cont visual
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame["Y"], tfame["C_ost_Ist"], label="Am")
plt.savefig("chart1.png")  # диаграмма остаточной стоимости (линейный способ)
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_Ist_2"], label="Am_2")
plt.savefig("chart2.png")  # диаграмма остаточной стоимости (уменьшаемый остаток)
vals = Am_Ist
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # для круговых диаграмм
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart3.png")  # распределение амортизации по годам линейным способом
vals = Am_Ist_2
labels = [str(x) for x in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart4.png")  # распределение амортизации по годам уменьшаемым остатком
table1_am = list(zip(Y, Am_Ist))
table2_am = list(zip(Y, Am_Ist_2))
tfame_am = pd.DataFrame(table1_am, columns=["Y", "Am_Ist"])
tfame2_am = pd.DataFrame(table2_am, columns=["Y", "Am_Ist_2"])
plt.figure()
plt.bar(tfame_am["Y"], tfame_am["Am_Ist"])  # создание столбчатой диаграммы
plt.savefig("chart5.png")  # амортизация по годам (линейный способ)
plt.figure()
plt.bar(tfame2_am["Y"], tfame2_am["Am_Ist_2"])
plt.savefig("chart6.png")  # амортизация по годам (уменьшаемый остаток)
plt.figure()

#INDIVIDUAL chast
#cont rascheta
print("РЕЗУЛЬТАТЫ ИНДИВИДУАЛЬНОЙ ЧАСТИ")
from sympy import *
k, T, C, L = symbols('k T C L')

#1sposob-lineyniy (Вариант 10: C=120000, T=10)
C_ost=120000
Am_Ist=[]
C_ost_Ist=[]
for i in range(10):
    Am=(C-L)/T
    C_ost-=Am.subs({C:120000,T:10,L:0})
    Am_Ist.append(round(Am.subs({C:120000,T:10,L:0}),2))
    C_ost_Ist.append(round(C_ost,2))
print("Am_Ist:",Am_Ist)
print("C_ost_Ist:",C_ost_Ist)
#2sposob-umen ostatok (Вариант 10: C=120000, T=10, k=2)
Aj=0
C_ost=120000
Am_Ist_2=[]
C_ost_Ist_2=[]
for i in range(10):
    Am=k*1/T*(C-Aj)
    C_ost-=Am.subs({C:120000,T:10,k:2})
    Am_Ist_2.append(round(Am.subs({C:120000,T:10,k:2}),2))
    Aj+=Am
    C_ost_Ist_2.append(round(C_ost,2))
print("Am_Ist_2:",Am_Ist_2)
print("C_ost_Ist_2:",C_ost_Ist_2)
#3.3cont tabl vivoda
import pandas as pd
Y=range(1,11)
print('')
table1=list(zip(Y,C_ost_Ist,Am_Ist))
table2=list(zip(Y,C_ost_Ist_2,Am_Ist_2))
tfame=pd.DataFrame(table1, columns = (['Y', 'C_ost_Ist', 'Am_Ist']))
tfame2=pd.DataFrame(table2, columns = (['Y', 'C_ost_Ist_2', 'Am_Ist_2']))
print(tfame)
print(tfame2)
#3.4cont visual
import numpy as np
import matplotlib.pyplot as plt
plt.plot(tfame['Y'], tfame['C_ost_Ist'], label = 'Am')
plt.savefig('chart7.png') #диаграмма остаточной стоимости (линейный способ)
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_Ist_2'], label = 'Am_2')
plt.savefig('chart8.png') #диаграмма остаточной стоимости (уменьшаемый остаток)
vals = Am_Ist
labels = [str(x) for x in range(1, 11)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #для круговых диаграмм
fig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart9.png') #распределение амортизации по годам линейным способом
vals = Am_Ist_2
labels = [str(x) for x in range(1, 11)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
ax.axis('equal')
plt.savefig('chart10.png') #распределение амортизации по годам уменьшаемым остатком
table1_am = list(zip(Y, Am_Ist))
table2_am = list(zip(Y, Am_Ist_2))
tfame_am = pd.DataFrame(table1_am, columns = ['Y', 'Am_Ist'])
tfame2_am = pd.DataFrame(table2_am, columns = ['Y', 'Am_Ist_2'])
plt.figure()
plt.bar(tfame_am['Y'], tfame_am['Am_Ist']) #создание столбчатой диаграммы
plt.savefig('chart11.png') #амортизация по годам (линейный способ)
plt.figure()
plt.bar(tfame2_am['Y'], tfame2_am['Am_Ist_2'])
plt.savefig('chart12.png') #амортизация по годам (уменьшаемый остаток)'''

# print("ЛАБОРАТОРНАЯ РАБОТА №3")
# print("1 Задание - вместе с Ватутиой С.А.")
# # 1 Задание - вместе с Ватутиой С.А.
# import os
# my_secret = os.environ['secret1']
# print(my_secret)
# my_secret = os.environ['secret2']
# print(my_secret)
# my_secret = os.environ['secret3']
# print(my_secret)
# print("2 Задание - вместе с Максимовой Е.А.")
# 2 задание (Вариант 6) - вместе с Максимовой Е.А.
# Контейнер расчета
# from sympy import*
# k, T, C, L = symbols('k T C L')

# #1 способ - линейный способ
# C_ost = 15000 #изменена начальная стоимость
# Am_lst = []
# C_ost_lst = []
# for i in range(8): 
#     Am = (C - L) / T 
#     C_ost -= Am.subs({C: 15000, T: 8, L: 0}) 
#     Am_lst.append(round(Am.subs({C: 15000, T: 8, L: 0}), 2)) 
#     C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)
# # Проверка выполнена/Максимовой

# #2 способ - уменьшаемый остаток
# Aj = 0
# C_ost = 15000 #согласно данным варианта 6 изменена начальная стоимость/Максимовой
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8): #изменен срок полезного использования на 8 лет/Максимовой
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 15000, T: 8, k: 2}) #измененны вводные данные/Максимовой
#     Am_lst_2.append(round(Am.subs({C: 15000, T: 8, k: 2}), 2)) #измененны вводные данные/Максимовой
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер для табличного вывода
# import pandas as pd
# from pandas.core.internals.managers import ensure_np_dtype
# Y = range(1, 9) #изменен срок полезного использования на 8 лет
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = (['Y', 'C_ost_lst', 'Am_lst']))
# tfame2 = pd.DataFrame(table2, columns = (['Y', 'C_ost_lst_2', 'Am_lst_2']))
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
# plt.savefig('chart13.png') #диаграмма остаточной стоимости (линейный способ)
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
# plt.savefig('chart14.png') #диаграмма остаточной стоимости (уменьшаемый остаток)
# vals = Am_lst
# labels = [str(x) for x in range(1, 9)] #изменен срок полезного использования на 8 лет
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #изменено на 8 значений тк СПИ 8 лет
# flig, ax = plt.subplots()
# ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
# ax.axis('equal')
# plt.savefig('chart15.png') #распределение амортизации по годам (линейный способ)
# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]  #изменен срок полезного использования на 8 лет
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #изменено на 8 значений тк СПИ 8 лет
# flig, ax = plt.subplots()
# ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
# ax.axis('equal')
# plt.savefig('chart16.png') #распределение амортизации по годам (уменьшаемый остаток)

# table1_am = list(zip(Y, Am_lst))
# table2_am = list(zip(Y, Am_lst_2))
# tfame_am = pd.DataFrame(table1_am, columns = ['Y', 'Am_lst'])
# tfame2_am = pd.DataFrame(table2_am, columns = ['Y', 'Am_lst_2'])
# plt.figure()
# plt.bar(tfame_am['Y'], tfame_am['Am_lst']) #создание столбчатой диаграммы
# plt.savefig('chart17.png') #амортизация по годам (линейный способ)
# plt.figure()
# plt.bar(tfame_am['Y'], tfame2_am['Am_lst_2'])
# plt.savefig('chart18.png') #амортизация по годам (уменьшаемый остаток)
# plt.figure()

# изменения нового варианта внесены корректно, вывод результатов корректный/Максимова Е
# оценка внесенных изменений: 5 баллов

# print("4 Задание - вместе с Третьяковым М.В.")
# # 4 задание - вместе с Третьяковым М.В.
# # Контейнер расчета
# from sympy import*
# k, T, C, L = symbols('k T C L')

# #1 способ - линейный способ
# C_ost = 30000
# Am_lst = []
# C_ost_lst = []
# for i in range(8): #Что это значит? (Ответ: Цикл выполняется 8(для каждого года эксплуатации от 1 до 8). i-счетчик итераций)
#     Am = (C - L) / T 
#     C_ost -= Am.subs({C: 30000, T: 8, L: 0})
#     Am_lst.append(round(Am.subs({C: 30000, T: 8, L: 0}), 2))
#     C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ - уменьшаемый остаток
# Aj = 0
# C_ost = 30000
# Am_lst_2 = []
# C_ost_lst_2 = []
# for i in range(8):
#     Am = k * 1 / T * (C - Aj)
#     C_ost -= Am.subs({C: 30000, T: 8, k: 2})
#     Am_lst_2.append(round(Am.subs({C: 30000, T: 8, k: 2}), 2))
#     Aj += Am
#     C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер для табличного вывода
# import pandas as pd #Что это значит? (Ответ: Импортируется библиотека pandas для работы с табличными данными)
# from pandas.core.internals.managers import ensure_np_dtype
# Y = range(1, 9) 
# table1 = list(zip(Y, C_ost_lst, Am_lst))
# table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
# tfame = pd.DataFrame(table1, columns = (['Y', 'C_ost_lst', 'Am_lst']))
# tfame2 = pd.DataFrame(table2, columns = (['Y', 'C_ost_lst_2', 'Am_lst_2']))
# print(tfame)
# print(tfame2)

# #Контейнер визуализации
# import numpy as np
# import matplotlib.pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
# plt.savefig('chart1.png') #диаграмма остаточной стоимости (линейный способ)
# plt.figure()
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
# plt.savefig('chart2.png') #диаграмма остаточной стоимости (уменьшаемый остаток)
# vals = Am_lst
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #для круговых диаграмм #Что это значит? (Ответ: explode - это список, который определяет, насколько каждый сектор будет "выдвинут" от центра круга. Значения в списке explode указывают, насколько каждый сектор будет смещен относительно центра.)
# flig, ax = plt.subplots()
# ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
# ax.axis('equal')
# plt.savefig('chart3.png') #распределение амортизации по годам (линейный способ)
# vals = Am_lst_2
# labels = [str(x) for x in range(1, 9)]
# explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
# flig, ax = plt.subplots()
# ax.pie(vals, labels = labels, autopct = '%1.1f%%', shadow=True, explode = explode, wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': 'k'}, rotatelabels = True)
# ax.axis('equal')
# plt.savefig('chart4.png') #распределение амортизации по годам (уменьшаемый остаток)

# table1_am = list(zip(Y, Am_lst))
# table2_am = list(zip(Y, Am_lst_2))
# tfame_am = pd.DataFrame(table1_am, columns = ['Y', 'Am_lst'])
# tfame2_am = pd.DataFrame(table2_am, columns = ['Y', 'Am_lst_2'])
# plt.figure()
# plt.bar(tfame_am['Y'], tfame_am['Am_lst']) #создание столбчатой диаграммы
# plt.savefig('chart5.png') #амортизация по годам (линейный способ)
# plt.figure()
# plt.bar(tfame_am['Y'], tfame2_am['Am_lst_2'])
# plt.savefig('chart6.png') #амортизация по годам (уменьшаемый остаток)
# plt.figure()
# # Оценка ответов на вопросы - 5 баллов

print("7 Задание - изменения в соотвествии с Вариантом 7")
# Контейнер расчета
from sympy import*
k, T, C, L = symbols('k T C L')

# 1 способ - линейный способ
C_ost = 90000  #  изменено с 30000 на 90000
Am_lst = []
C_ost_lst = []
for i in range(9):  #  9 лет вместо 8 (диапазон 0..8)
    Am = (C - L) / T 
    C_ost -= Am.subs({C: 90000, T: 9, L: 0})  #  T=9, C=90000
    Am_lst.append(round(Am.subs({C: 90000, T: 9, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst (линейный):', Am_lst)
print('C_ost_lst (линейный):', C_ost_lst)

# 2 способ - уменьшаемый остаток (коэффициент ускорения 2)
Aj = 0
C_ost = 90000  #  изменено
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(9):  #  9 лет
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 90000, T: 9, k: 2})  # ← T=9, C=90000
    Am_lst_2.append(round(Am.subs({C: 90000, T: 9, k: 2}), 2))
    Aj += Am.subs({C: 90000, T: 9, k: 2})  #  исправлено: Aj накапливаем численно
    C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2 (уменьш.остаток):', Am_lst_2)
print('C_ost_lst_2 (уменьш.остаток):', C_ost_lst_2)

# Контейнер для табличного вывода
import pandas as pd
Y = range(1, 10)  #  1..9
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=(['Y', 'C_ost_lst', 'Am_lst']))
tfame2 = pd.DataFrame(table2, columns=(['Y', 'C_ost_lst_2', 'Am_lst_2']))
print("\nТаблица 1 (линейный способ):")
print(tfame)
print("\nТаблица 2 (уменьшаемый остаток):")
print(tfame2)

# Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame['Y'], tfame['C_ost_lst'], 'o-', label='Линейный способ')
plt.xlabel('Год')
plt.ylabel('Остаточная стоимость, руб')
plt.title('Остаточная стоимость (линейный способ)')
plt.grid(True)
plt.savefig('chart1.png')
plt.close()

plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], 's-', label='Уменьшаемый остаток', color='orange')
plt.xlabel('Год')
plt.ylabel('Остаточная стоимость, руб')
plt.title('Остаточная стоимость (уменьшаемый остаток)')
plt.grid(True)
plt.savefig('chart2.png')
plt.close()

# Круговые диаграммы
vals = Am_lst
labels = [str(x) for x in range(1, 10)]
explode = tuple([0.05] * 9)  #  9 элементов
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, 
       explode=explode, wedgeprops={'lw':1, 'ls': '--', 'edgecolor': 'k'}, 
       rotatelabels=True)
ax.axis('equal')
ax.set_title('Распределение амортизации по годам (линейный)')
plt.savefig('chart3.png')
plt.close()

vals = Am_lst_2
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, 
       explode=explode, wedgeprops={'lw':1, 'ls': '--', 'edgecolor': 'k'}, 
       rotatelabels=True)
ax.axis('equal')
ax.set_title('Распределение амортизации по годам (уменьш.остаток)')
plt.savefig('chart4.png')
plt.close()

# Столбчатые диаграммы
plt.bar(tfame['Y'], tfame['Am_lst'], color='steelblue')
plt.xlabel('Год')
plt.ylabel('Амортизация, руб')
plt.title('Амортизация по годам (линейный способ)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('chart5.png')
plt.close()

plt.bar(tfame['Y'], tfame2['Am_lst_2'], color='coral')
plt.xlabel('Год')
plt.ylabel('Амортизация, руб')
plt.title('Амортизация по годам (уменьшаемый остаток)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('chart6.png')
plt.close()

print("\n Все графики сохранены: chart1.png ... chart6.png")