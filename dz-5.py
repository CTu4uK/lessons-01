#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


# vir = int(input("Введите выручку фирмы: "))
# izd = int(input("Введите издержки фирмы: "))
# sotr = int(input("Введите численность сотрудников"))
#
# if vir > izd:
#     print("прибыль — выручка больше издержек")
#
# else:
#     print("убыток — издержки больше выручки")
#
# rent = (vir - izd) / vir * 100
#
# print("рентабельность выручки", rent, "%")
#
# prib = (vir - izd) // sotr
#
# print("прибыль фирмы в расчете на одного сотрудника", prib, "тыс")
#Для расчета этого показателя нужно разделить прибыль на выручку и умножить полученное число на 100 %. Показатель рентабельности выручки.

revenue = int(input("Введите сумму выручки >>> "))
const = int(input("Введите сумму издержек >>> "))

profit = revenue - const

if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабильность = {profitability}")

    workers_count = int(input("Укажите количество сотрудников >>> "))

    profit_per_worker = profit / workers_count
    print(f"Прибыль но одного сотрудника = {profit_per_worker}")
else:
    print(f"Убыток = {profit}")