'''radius = 20 int (целое число)
PI = 3.14159 float (дробное число)
diametr = 2*radius
print("Aylana uzunligi=", PI*diametr)
print(type(diametr))
str(radius) ("str" = текст)
print(type(radius))
radius = str(radius) #при этой командой мы можем перевести "int(целое число)" на "str(текст)"
print(type(radius))'''


# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end#='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ!')

# print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ!', sep='_', end='!')

# print('БЕСКОНЕЧНОСТЬ', 'НЕ', 'ПРЕДЕЛ', sep='_', end='')
# print('!')

# print('БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ', end='')
# print('!')

# print('БЕСКОНЕЧНОСТЬ_', 'НЕ_', 'ПРЕДЕЛ!', sep='', end='')

# print('Follow PEP8!')

# print ('Follow PEP8!')

# print('Follow', 'PEP8!')

# print('Follow','PEP8!')

# print('Follow','PEP8', sep = '**')

# print('Follow', 'PEP8', sep='**')

# name = input()

# name=input()

# print((-10)**2)
# print((-10)**3)

# a = 82 // 3**2 % 7
# print(a)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a,b,c)
# print(b,c,a)
# print(c,a,b)
# print(a,c,b)
# print(b,a,c)
# print(c,b,a)

# from itertools import permutations

# digits = "123"  # или ['1','2','3'], или [1,2,3]
# for perm in permutations(digits):
#     print(''.join(perm))

# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)

# import math
# fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
# print(fun(5))

# import time

# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver

# # импортируем класс By, который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By

# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()

# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(5)

# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://suninjuly.github.io/text_input_task.html")
# time.sleep(5)

# # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# # Ищем поле для ввода текста
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)

# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)

# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# # driver.quit()
# a = 2
# a += 3 # a = a + 3
# print(a)

