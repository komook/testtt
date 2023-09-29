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


def find_average(numbers = [1,2,3]):
    if numbers == []:
        return []
    return sum(numbers) // len(numbers) 
        


print(find_average())