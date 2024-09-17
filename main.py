import random
import time
from random import *


names = ["Ксения", "Варвара", "Даниил", "Тамара", "Михаил", "Денис", "Анастасия", "Николай", "Ариана", "Макар",
         "Василиса", "Ольга", "Иван", "Георгий", "Мила", "Ника", "Александра", "Фёдор", "Марина", "Мирон", "Александр",
         "Дарья", "Алина", "Анна", "Милана", "Арсений", "Мария", "Никита", "Тимофей", "Лейла", "Ярослав", "Роман",
         "Владимир", "Дмитрий", "Артём", "Роберт", "Екатерина", "Савелий", "Григорий", "Филипп","Матвей", "Ульяна",
         "Вячеслав", "Наталья", "Мирослав", "Виктория", "Алексей", "Глеб", "Марк", "Всеволод"]
people = ["Артур", "Кирилл", "Стас"]
height = [180, 174, 186]


def menu():
    possibilities = {
        1: show,
        2: add,
        3: delete,
        4: sort,
        5: min_max,
        6: sred,
        7: inimesed,
    }

    print("1 - Посмотреть список людей и из рост\n"
          "2 - Добавить человека и его рост в список\n"
          "3 - Удалить человека из списка\n"
          "4 - Отсортировать лбдей в алфавитном порядке\n"
          "5 - Показать самого высокого и низкого человека\n"
          "6 - Показать людей со средним ростом\n"
          "7 - Добавить имена в список\n")

    action = int(input())
    possibilities[action]()


def show():
    print(people)
    print(height)


def add():
    print("Введите имя человека которого хотите добавить")
    name = input()
    people.append(name)
    
    print("Введите рост этого человека")
    height_person = int(input())
    height.append(height_person)
    
    return people, height


def delete():
    print("Введите имя человека которого хотите удалить")
    name = input()
    for i in range(len(people)):
        if people[i] == name:
            height.pop(i)
            people.remove(people[i])
            return i
    return people, height


def sort():
    print("....Запуск....")
    s = "█"
    for i in range(101):
        time.sleep(0.05)
        print("\r", "Загрузка", i * s, str(i), '%', end="")
    print("\nЛюди отсортированы")
    abi_p = 0
    abi_i = ""
    n = len(height)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if people[i] > people[j]:
                abi_p = people[i]
                people[i] = people[j]
                people[j] = abi_p
                abi_i = height[i]
                height[i] = height[j]
                height[j] = abi_i
    return people, height


def min_max():
    for i in range (len(height)):
        if height[i] == min(height):
            print(min(height), " ", people[i])
    for i in range (len(height)):
        if height[i] == max(height):
            print(max(height), " ", people[i])


def sred():
    print("Средний рост трёх первых человек", (people[0], people[1], people[2]), "равен", (height[0] + height[1] + height[2]) / 3)


def inimesed():
    print("Сколько имён вы хотите добавить в список? 1 - 50")
    kol_vo=int(input())
    for i in range (kol_vo):
        people.append(names[randint(0,49)])
        a = randint(130, 200)
        height.append(a)


if __name__ == '__main__':
    menu()
