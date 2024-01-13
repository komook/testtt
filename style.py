# x = 'Hello Python!'

# first_two = x[6:7]
# symbol_h = x[-5:-3]


# new_name = first_two + 'a' + symbol_h
# print(new_name)



# print('''
#       {0:10.4f} {1:10.4f} {2:10.4f} {3:10.4f}
#       {4:10.4f} {5:10.4f} {6:10.4f} {7:10.4f}'''.format(1.5435, 54.6345, 773.1232, 54.6345, 773.1232, 992.1112, 665.3344, 23.5345))


# numbers = {1, 2, 3, 4, 5, 'six', 'seven'}
# print(numbers)
# print(type(numbers))


# letters_set = set('Создайте множество при помощи функции set() '
#                   'из текста, чтобы получить уникальные символы, '
#                   'содержащиеся в тексте.')
# print(letters_set)
# number = int(input('Enter an integer number'))

# if number % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')

# list_number = [10,15,27,8,4,25,13,14,21,30]

# for number in list_number:
#     if number % 2 == 0:
#         print('Четное')
#     else:
#         print('не четное')

# greetings = ['hello', 'hi', 'hey', 'hola']

# new_letter = [word[1] for word in greetings]
# print(new_letter)


# greetings2 = ['hello', 'hi', 'hey', 'hola']

# for new_list in greetings2:
#     print(new_list[1])


# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_letter = [even  for even in digits if even % 2  != 0 ]
# print(new_letter)


# digits2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for new_list in digits2:
#     if new_list % 2 != 0:
#         print(new_list)



# smile = '\U0001F600'
# x = 0
# i = 0

# for i in range(10):
#     while x < 10:
#         print(smile)
#         smile += '\U0001F600'
#         x += 1
        


# def cat_voice():
#     print("Meow")
      


# def dog_voice():
#     print("Woof")
    


# for x in range(2):
#     cat_voice(), dog_voice()

# meaning = input('Введите текст')

# def get_voice(text = meaning):
#     return meaning + '!'


# print (get_voice())


# a,b,c = 1,10,2
# print(*(i for i in range(a,b+1) if not i%c))

# summ = []

# def not_even(a,b):
#     for i in range(a,b):
#         if i % 2 != 0:
#             summ.append(i)
#             print(summ)
        

# not_even(1, 15)

# n,d = 15, 30
# summ2 = []

# summ_list = [summ2.append(numbers) for numbers in range(n,d) if numbers % 2 != 0]

# print(summ2)



# def is_cat_here(*args):
   
#     for arg in args:
#         if 'cat' in arg.lower():
#             return True
    
#     return False

# result = is_cat_here("The cat is black.", "There is no dog.")
# print(result1)  


# def is_item_here(item, *args):
#     if 'item' in args:
#         return True
    
#     return False

# result = is_item_here('prvet', 123, 2223, 'asd', 'item', True)
# print(result) 

# def your_favorite_color(my_color, **kwargs):
#     if 'color' in kwargs:
#         print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
#     else:
#         print('My favorite color is {}, what is your favorite color?'.format(my_color))


# your_favorite_color('green', color='yellow')


# class BlogPost:


#     def __init__(self, user_name, text, number_of_likes):
#         self.user_name = user_name
#         self.text = text
#         self.number_of_likes = number_of_likes


# person = BlogPost(user_name='Sasha', text='hello', number_of_likes=5)
# person.number_of_likes = 2

# print(person.number_of_likes)

# person2 = BlogPost(user_name='Masha', text='How are you', number_of_likes=13)
# print(person2.number_of_likes)


# class BankAccount:
#     def __init__(self, client_id, client_first_name, client_last_name, balance = 0.0):
#         self.client_id = client_id
#         self.client_first_name = client_first_name
#         self.client_last_name = client_last_name
#         self.balance = balance

    
#     def add(self,new_balance):
#         self.balance += new_balance
#         return self.balance
    
#     def withdraw(self, decrease_balance):
#         self.balance -= decrease_balance
#         return self.balance

# client = BankAccount(1, 'Alex', 'Andree', 15)
# print(client.add(5))
# print(client.withdraw(5))



# class GameCharacter:
#     def __init__(self, name, health, level ):
#         self.name = name
#         self.health = health
#         self.level = level


#     def speak(self):
#         print('Hi, my name is {}'.format(self.name) )
        

    
    

# class Villain(GameCharacter):

    

#     def speak(self):
#         print('Hi, my name is {} and I will kill you  ' .format(self.name,self.kill()) )

#     def kill(self):
#         self.health = 0
#         print("Bang-bang, now you're dead {}".format(self.health) )

# Gamer = Villain('artem', 11, 15)
# Gamer2 = GameCharacter('artur', 10, 5)

# Gamer.speak()
# print (Gamer.health)
# print(Gamer2.health)

# class GameCharacter:

#     def __init__(self, name, health,
#                  level):
#         self.name = name
#         self.health = health
#         self.level = level

#     def speak(self):
#         print('Hi, my name is ' + self.name)


# class Villain(GameCharacter):

#     def __init__(self, name, health,
#                  level):
#         GameCharacter.__init__(self, name, health,
#                                level)

#     def speak(self):
#         print('Hi, my name is ' + self.name + ' and I will kill you')

#     def kill(self, other):
#         other.health = 0
#         print('Bang-bang, now you\'re dead')


# james = GameCharacter('James', 100, 1)
# jim = Villain('Jim', 100, 2)

# james.speak()
# jim.speak()
# print(james.health)
# jim.kill(james)
# print(james.health)



# /////////////////////////////////////////////////////////////////////

# class Chain():
#     def __init__(self, number_of_items):
#         self.number_of_items = number_of_items


#     def __str__ (self):
#         return 'Chain with ' + str(self.number_of_items) +  ' items'

#     def __len__ (self):
#         return self.number_of_items

# person = Chain(123)
# print(person)
# print(len(person))

# from math import*

# print(sqrt(123456789),factorial(987),pow(876, 54))
# nums = [1, 5, 2, 1, 4, 5, 1]
# dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
# print(dup) 




# nums = [1, 5, 2, 1, 4, 5, 1]
# dup = []

# # Пройдемся по всем элементам списка nums
# for i, x in enumerate(nums):
#     # Найдем индекс первого вхождения элемента x
#     first_index = nums.index(x)
    
#     # Проверим, если текущий индекс не равен индексу первого вхождения, то это дубликат
#     if i != first_index:
#         dup.append(x)

# print(dup)


# def modify_list(l):
#     for x in l:
#         if x % 2 == 0:
#             summ = x // 2
#             print(summ)
            

# modify_list([12,22,15,65])
                
# x = int(input("char 1:"))
# y = int(input("char 2:"))


# for summ in range(x,y):
#     if summ // 10:
#         print('делится')
#     else:
#         print('нет')


# class footboll():
#     def __init__(self, game, team1, goal1, team2, goal2):
#         self.game = game
#         self.team1 = team1
#         self.goal1 = goal1
#         self.team2 = team2
#         self.goal2 = goal2

    

#     def check(self):
#         x = self.goal1 > self.goal2
# string = "Добро пожаловать!"
# print("Индекс первой буквы 'о':", string.find("о"))
# football = {'Spartack': {1}, 'Zenit':{10}, 'Lokomativ': {7}}




# print(team('123', 1, 'team2', 5))

# Функция для обновления результатов команды в словаре
# Функция для обновления результатов команды в словаре
# Функция для обновления результатов команды в словаре
# class_points = [13, 22, 55, 42, 22, 66]
# your_points = 44

# def better_than_average(class_points, your_points):
    
#     quality = len(class_points)
#     total = sum(class_points)
#     print(total)
#     print(quality)
    
    
#     result = total // quality  
#     if result < your_points:
#         print(result)
#         return True
#     else:
#         return False

# print(better_than_average(class_points, your_points ))

# a = [12, 54, 433, 54]
# def sum_array(a):
#     b = sum(a)
#     print(b)
#     if a:
#         return 0
    

# sum_array(a)
# n = 5

# def reverse_seq(n = 5):
#     for x in range(n):
#         print(x)
       
# print(reverse_seq() )  


# def square_sum(numbers = [115,210]):
#     degree_lis = []
#     for i in numbers:
#         x = i ** 2
#         degree_lis.append(x)
    

#     xx = sum(degree_lis)
#     print(xx)

# square_sum()

# def summation(num = 5):
#     b = []
#     for x in range(1,num + 1):
#         b.append(x)
#     return sum(b)

# print(summation())


# rock = 'rock'
# scissors = 'scissors'
# paper = 'paper'

# def rps(p1, p2):

#     if p1 == p2:
#         print("Draw!")

#     elif p1 == "rock" and p2 == "scissors" or p1 == "scissors" and p2 == "paper" or p1 == "paper" and p2 == "rock":
#         print('Player 1 won!')
#     else:
#         print('Player 2 won!')


# rps(rock, paper)


# x = { 6, 2, 1, 8, 10 } 
# d = { 1, 1, 11, 2, 3 } 

# def sum_array(arr):
#     k = 0
#     return (k + i for i in arr if i != max(arr) or min(arr))

# print(sum_array(x))



    # g = max(arr)
    # h = min(arr)
    # arr.remove(h)
    # arr.remove(g)
    # return sum(arr)





# x = [0] 
# d = { 1, 1, 11, 2, 3 } 


# def sum_array2(arr):
#     if arr == None :
#         return 0

#     if len(arr) == 1 or len(arr) == 0 :
#         return 0
    
    
#     g = max(arr)
#     h = min(arr)
#     k = g + h
#     return sum(arr) - k


# print(sum_array2(x))









# def sum_array(arr):
#     k = 0
#     for x in len(arr):
#         if x != arr.index(max(arr)) and x != arr.index(min(arr)):
#             k += arr[x]
#     return k

# print(sum_array(x))








# def sum_array(arr):
#     #your code here
#     try:
#         arr.remove(max(arr))
#         arr.remove(min(arr))
#         return sum(arr)
#     except:
#         return 0






# def lovefunc( flower1, flower2 ):
#     if flower1 == flower2:
#         return False
#     else:
#         if flower1 % 2 == 0 and flower2 % 2 == 0:
#             return False
#         else:            
#             if flower1 % 2 != 0 and flower2 % 2 == 0:
#                 return True       
#             else:
#                 if flower1 % 2 == 0 and flower2 % 2 != 0:
#                     return True








# def lovefunc( flower1, flower2 ):
#     return (flower1 + flower2) % 2 == 1

# print(lovefunc(456, 233))

# print((456 + 456) % 2)





# def lovefunc( flower1, flower2 ):
#     if flower1%2 != flower2%2:
#         return True
#     else:
#         return False

# def basic_op(operator, value1, value2 ):
#     return value1 + value2 if operator == "+" else False or value1 - value2 if operator == "-" \
#     else False or value1 * value2 if operator == "*" else False or value1 / value2 if operator == "/" else False


# def find_average(numbers = [1,2,3]):
#     if numbers == []:
#         return []
#     return sum(numbers) // len(numbers) 
        

# print(find_average())




# number = 1000
# rounded_up = math.ceil(number / 100) * 100
# print(rounded_up)

# print(100 // 100)

# import math
# def century(year):
#     return (math.ceil(year / 100) * 100) // 100


# print(century(2001))
# ///////////////////////////////////

# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []

# /////////////////////////////////////
   
# def count_positives_sum_negatives(arr):
#     b = []
#     d = []
    
#     for x in arr:
#         if x > 1:
#             b.append(x)
#         elif x < 0:
#             d.append(x)
#         else:
#             return []

#     print([len(b), sum(d)])


# count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])

# cap, on, wait = 100, 60, 50

# def enough(cap, on, wait):
#     # cap - мест в автобусе / on  - сколько сейчас / wait - сколько ждут
#     x = on + wait
#     i = x - cap
#     return i
    
    

# enough(cap, on, wait)



# def first_non_consecutive(arr):
#     i = 1
#     try:


#         for x in arr:
        
#             b = arr[i]
#             if x  != b - 1:
#                 return b
#             else:
#                 i += 1
#     except:
#         return None            


# print(first_non_consecutive([1,2,3,4,6,7,8]))

# arr = [1,2,3,4,5,6]


# # for i, x in enumerate(arr[:-1]):
# #     print(i,x)



# x = ()
# x = enumerate(arr[:-1])
# print(x)

# i = 1
# while i < 6:
#   print(i)
#   i += 1


# srt1 = "sadds"

# print(len(srt1))


# test1 = 'asdf'

# if test1[2] == 'a' or test1[2] == 's':
#     print('yes')
# else:
#     print('no')

# .........................

# def get_count(sentence):
#     b = 0
#     n = 0
#     i = 0
    
#     while n <= len(sentence) - 1:  
        
#         for x in sentence[i]:

#             if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                
#                 i += 1
#                 b += 1
#                 n += 1
#             else:
#                 i += 1
#                 n += 1
#     print(b)            
    

# get_count('abracadabra')


# def get_count(sentence):
#     b = 0      
#     for x in sentence:
#         if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#             b += 1  
#     print(b)            
    

# get_count('abracadabra')

# ////////////////////////////////////////////////////////

# def even_odd():
#     even = [
#         "even",
#         "odd",
#         "even",
#         "odd",
#         "even",
#         "odd",
#         "even",
#     ]
#     for odd in even:
#         yield odd

# counter = even_odd()
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())
# print(counter.__next__())

# ////////////////////////////////////////////////////////////////////




# def even_odd(x):
#     while (x > 0):
#         if x%2==0:
#             yield 'even'
#         else:
#             yield 'odd'
#         x -= 1


# even_odd_generator = even_odd(4)
# print(next(even_odd_generator))  # 'even'
# print(next(even_odd_generator))  # 'odd'
# print(next(even_odd_generator))  # 'even'
# print(next(even_odd_generator))  # 'odd'



# mass = [(123, 234), (534, 345)]

# for x in mass:
#     print(x[0])

# data = [(11, 12), (60, 7), (30, 17), (56, 20), (46, 25), (60, 3), (58, 6)]

# def open_or_senior(data):
#     b = []
#     for x in data:
#         if x[0] >= 55 and x[1] >=7:
#             b.append('Senior')
#         else:
#             b.append('Open')
#     return b



# print(open_or_senior(data))



# .....................................
# a = '1234'

# if len(a) == 4:
#  return True if len(pin) == 4 or len(pin) == 6 else False

# def validate_pin(pin):
#     b = []
#     c = []
#     for x in pin:
#         if x == '-' or x == '.' or x == 'a' or x == '+' or x == ' ':
#             c.append(x)
#         elif len(pin) == 4 or len(pin) == 6:
#             b.append(x)
#         else:
#             c.append(x)
#     return True if len(b) == 4 or len(b) == 6 else False



# print(validate_pin('09876 '))
# text = "samurai"
# print(text[-4])



# def solution(text, ending):
#     d = len(ending)
#     try:
#         return True if text[(d - d*2)] == ending[d - d*2] else False
#     except:
#         return False
    



# print(solution("samurai", "ai"))



# def print_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         return func(*args, **kwargs)
#     return wrapper


# @print_args
# def some_func():
#     print('Some code')


# some_func(123, 32)


# def hello_from_decorator(func):
#     def printing(*args, **kwargs, ):
#         func()
#         print("Hello from decorator!")
        
#     return printing



# @hello_from_decorator
# def some_func():
#     print('Hello')


# some_func()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# l = [12, 5, '2', '6', 1, 'as']

# def filter_list(l):
#     b = []
#     for x in l:
#         if str(x) == x:
#             pass
#         else:
#             b.append(x)
#     return b



# print(filter_list(l))

# b = [1, 2, 3, 4, 5]

# print(*b)

# s = [5, 8, 12, 18, 22]


# one_min = min(s)

# s.remove(one_min)



# print(s)
# two_min = min(s)

# print(two_min)

# def sum_two_smallest_numbers(s):
#     one_minn = min(s)
#     s.remove(one_minn)
#     two_min = min(s)
#     s.remove(two_min)
#     return one_minn + two_min


# print(sum_two_smallest_numbers(s))

# ////////////////////////////////////////////////////


# str = "pythonist"
# print ("Исходная строка: " + str) 
# res_str = str.replace('t', '') 
# # Удаление всех 't' 
# print("Строка после удаления всех символов t: " + res_str) 
# # Удаление только первой t 
# res_str = str.replace('t', '', 1) 
# print ("Строка после удаления первого t: " + res_str)

# def remove_exclamation_marks(s):

#     x = s.split("!")
#     return x


# print(remove_exclamation_marks(s))
# txt = "welcome to the jungle!"

# x = txt.split("!")

# print(x)


# //////////////////////////////////////////////////////////////////////


# import numpy as np
# import pandas as pd


# df = pd.read_csv('./students.csv', sep=',', header=None, nrows=10)
# df1 = pd.DataFrame(df)

# # # Вывести первые 3 строчки
# # print(df1.head(3))
# # # вывести последнии 2 строчки
# # print(df1.tail(2))
# # # уникальные, количество их, частота
# # print(df.describe())
# # # Размер тут 5 на 5
# # print(df.shape)
# # # Количество элементов
# # print(df.size)
# # df.loc - с метками
# # df.iloc - с строками
# # df.mean() - среднее значение
# print(df1[2])

# print(pd.concat([df, df], axis=1))
# print(df1['Age'].plot.hist())

# /////////////////////////////////////////////////////////////////////////


# s = 'AAAAAAABBBBBBCCCCCCDDDDDD'






# x = 'aaaabbbaccccdd'
# y = []
# for i in x :
#     if i not in y:
#         y.append(i)
# print(y)

# def make_compliment(func):
#     def wrapper():
#         print('213213213')
#         func()
#         print('0000000')
#     return wrapper

# @make_compliment
# def how_do_you():
#     print('Hello')


# how_do_you()


# import csv

# with open('students.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for students in csv_reader:
#         print(f'{students[1]} {students[2] } dfgdfgdfgdfg {students[4]}')


# def find_short(s):
#     d = s.split()
#     lenght = len(d)
#     i = []
#     for x in d:
#         i.append(len(x))
#     return min(i)


def find_next_number(n):
    # Преобразуем число в строку, чтобы работать с его цифрами
    n_str = str(n)
    
    # Сортируем цифры в строке
    sorted_digits = sorted(n_str)
    
    # Ищем следующее положительное число, содержащее те же цифры
    next_number = n + 1
    while True:
        next_str = str(next_number)
        
        # Если отсортированные цифры совпадают, и следующее число меньше или равно введенному числу, то это искомое число
        if sorted(next_str) == sorted_digits and next_number <= n:
            return next_number
        
        next_number += 1

# Пример использования
n = 123
result = find_next_number(n)
print(f"Следующее наименьшее число с теми же цифрами: {result}")
