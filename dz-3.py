#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#
# chislo = (input("Введите число n: "))
# temp = str(chislo)
# t1 = temp + temp
# t2 = temp + temp + temp
# otvet = chislo + int(t1) + int(t2)
#
# print("ОТВЕТ >>> {0} + {1} + {2} = {3}".format(chislo, t1, t2, otvet))

user_input = input("Введите число >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

# простой пример через диапозон (time = 3.5428000000115034)
result = 0 #
for x in range(1, 4): #
    result += int(user_input * x) #

    print(result)

# Пример длинны чtрез while
user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplacation = (10 ** characters_count) + 1
second_level_multiplication = (10 ** characters_count * 2) + first_level_multiplacation

result = user_number + (user_number * first_level_multiplacation) + (user_number * second_level_multiplication)
print(result)