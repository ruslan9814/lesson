# def first_function(var_1, var_2, var_3):
#  return var_1* 0.5 + var_2/3 + var_3 ** 4.3
# function_res_1 = first_function(1, 2, 3)
# print(function_res_1)
# function_res_2 = first_function(var_1=1, var_3=3, var_2=2)
# print(function_res_2)
# function_res_3 = first_function(1, 2, var_3=3)
# print(function_res_3)
#
# def appender(var_1, list_1 = []):
#  list_1.append(var_1)
#  return list_1
# first = appender(1)
# print(first)
#from unittest.mock import right

# from turtle import*
# shape("turtle")
# pensize(5)
# for i in range(10):
#     forward(100)
#     left(90)
#     forward(100)
#     penup()
#     color("red", 'yellow')
#     left(80)
#     forward(80)
#     left(180)
#     forward(10)
#     pendown()
#     pensize(13)

# var_1 = 5
# def func_1():
#  var_1 = 10
#  print(var_1)
#
# func_1()
# print(var_1)

# var_1 = 5
# def func_1():
#  print(var_1)
# func_1()
# print(var_1)

# var_1 = 5
# def func_1():
#     print(var_1)
#     var_1 = 1
# print(var_1)

# func_1()

# var_1 = 5
# def first():
#     var_1 = 10
#     def second():
#         print(var_1)
#     second()
# first()
# print(var_1)

# var_2 = 15
# def first():
#     var_1 = 10
#     def second():
#         nonlocal var_1
#         var_1= 1
#         global var_2
#         var_2 = 2
#         second()
#         print(var_1)
# first()
# print(var_2)

# from turtle import *
# print("locals —", locals())
# print("globals —", globals())


# import random
# def game(choice, result):
#     print("")
#     print("=====Start Game rock, paper,scissors=====")
#     computer_choice = random.choice("rps")
#     print("--------------------------------")
#     print("Your select – ",str.capitalize(choice))
#     print("Computer select —",str.capitalize(computer_choice))
#     if str.lower(choice) == computer_choice:
#         print("Result of game – Draw")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#     elif str.lower(choice) == "r" and computer_choice == "p":
#         result["computer"] += 1
#         print("------Computer Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"], "Player")
#     elif str.lower(choice) == "r" and computer_choice == "s":
#         result["player"] += 1
#         print("------Player Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#     elif str.lower(choice) == "p" and computer_choice == "s":
#         result["computer"] += 1
#         print("------Computer Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#     elif str.lower(choice) == "p" and computer_choice == "r":
#         result["player"] += 1
#         print("------Player Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#     elif str.lower(choice) == "s" and computer_choice == "r":
#         result["computer"] += 1
#         print("------Computer Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#     elif str.lower(choice) == "s" and computer_choice == "p":
#         result["player"] += 1
#         print("------Player Wins------")
#         print("Score,Computer", result["computer"], "—", result["player"],"Player")
#
# result = {"computer": 0, "player": 0}
# choise = input("Select R / P / S – ")
# game(choice=choise, result=result)



# import random
#
# list_of_question = [
#     "У тебя есть слово, которое ты придумал сам?",
#     "Ты когда-нибудь врал о своём возрасте?",
#     "Какую самую большую шутку ты когда-либо придумал?",
#     "У тебя есть какое-то странное или особое умение?",
#     "Ты поёшь в ванной?",
#     "Как ты пытаешься избежать помощи по дому?",
#     "Ты боишься привидений?",
#     "Ты когда-нибудь поливал растение молоком?",
#     "Ты когда-нибудь ломал что-то, не сказав никому?",
#     "Если бы у тебя была 1 минута, чтобы быстро покинуть дом, что бы ты взял с собой?"
# ]
#
# list_of_action = [
#     "Не моргай минуту",
#     "Побеги вокруг дома три раза",
#     "Обними свой почтовый ящик (или дерево/декорацию на лужайке) на 20 секунд",
#     "Говори, высунув язык",
#     "Выполни действие, как будто ты следующий игрок, который выбирает категорию 'Действие'",
#     "Отправь кому-то сообщение, используя только нос",
#     "Притворись, что играешь на воздухе на гитаре",
#     "Спой детскую песенку",
#     "Говори и веди себя как робот",
#     "После всего, что ты скажешь, добавляй слова 'Ух ты… Я хорош!' в течение следующих 15 минут"
# ]
#
#
# gamer_list = []
#
# def gamers(list):
#     while True:
#         name = input("Введите имя игрока (минимум 3 символа) – ")
#         if len(name) >= 3:
#             list.append(name.capitalize())
#         else:
#             print("Имя должно быть не менее 3 символов.")
#             continue
#
#         if len(list) >= 2:
#             need_next_player = input("Добавить еще игроков? (Y/N) ")
#             if need_next_player.lower() in ['n', 'no']:
#                 break
#         else:
#             print("Требуется как минимум 2 игрока.")
#
#
# def game(list_of_question, list_of_action, *args):
#     while True:
#         for gamer in args:
#             print(f"\nХод игрока {gamer}!")
#             user_choice = input("Вопрос или действие? (Q/A) ")
#             if user_choice.lower() in ['q', 'question']:
#                 if list_of_question:
#                     question_index = random.randint(0, len(list_of_question) - 1)
#                     print(f"Вопрос: {list_of_question.pop(question_index)}")
#                 else:
#                     print("Вопросы закончились!")
#                     break
#             elif user_choice.lower() in ['a', 'action']:
#                 if list_of_action:
#                     action_index = random.randint(0, len(list_of_action) - 1)
#                     print(f"Действие: {list_of_action.pop(action_index)}")
#                 else:
#                     print("Действия закончились!")
#                     break
#             else:
#                 print("Некорректный выбор. Вам предстоит и вопрос, и действие.")
#                 if list_of_question:
#                     question_index = random.randint(0, len(list_of_question) - 1)
#                     print(f"Вопрос: {list_of_question.pop(question_index)}")
#                 if list_of_action:
#                     action_index = random.randint(0, len(list_of_action) - 1)
#                     print(f"Действие: {list_of_action.pop(action_index)}")
#
#             next_step = input("Следующий игрок? (Y/N) ")
#             if next_step.lower() in ['n', 'no']:
#                 print("Игра окончена")
#                 return
#
#         select = input("Новый раунд? (Y/N) ")
#         if select.lower() in ['n', 'no']:
#             print("Игра окончена")
#             return
#
# gamers(gamer_list)
# game(list_of_question, list_of_action, *gamer_list)


# def black_hole_mixed(var_1, var_2=3, *args,**kwargs):
#  print("var_1:", var_1)
#  print("var_2:", var_2)
#  for arg in args:
#      print(arg)
#  for key, value in kwargs.items():
#      print(key, value)
#
# black_hole_mixed(1.2, name="Nick", planet=
# "Earth", galaxy="Milky Way", age=13800000000)

# list_1 = [60,2]
# def way(v,t):
#  way = v*t
#  print(way)
# way(*list_1)

# dict_1 = {"t": 2, "v": 60}
# def way(v,t):
#  way = v*t
#  print(way)
# way(**dict_1)

# dict_1 = {"var_3": 3, "var_4": 4}
# list_1 = [2]
# def some_func(var_1, var_2, var_3, var_4):
#  print(var_1, var_2, var_3, var_4)
# some_func(1,*list_1, **dict_1)

mas = ["alice", "bob", "charlie", "dave", "vira", "zara"]

#Sort
# for i in range(len(mas)):
#     for j in range(len(mas)):
#         if mas[i] < mas[j]:
#             temp = mas[i]
#             mas[i] = mas[j]
#             mas[j] = temp
# print(mas)

name = "bob"
left = 0
right = len(mas) - 1


while left <= right:
    sired = left + (right - left) // 2
    if mas[sired] == name:
        print(mas[sired])
        break
    elif mas[sired] < name:
        left = sired + 1
    else:
        right = sired - 1
else:
    print("Name not found.")






