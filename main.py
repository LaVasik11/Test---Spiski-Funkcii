import random
import time
from random import *
imena = ["Ксения", "Варвара", "Даниил", "Тамара", "Михаил", "Денис", "Анастасия", "Николай", "Ариана", "Макар",
         "Василиса", "Ольга", "Иван", "Георгий", "Мила", "Ника", "Александра", "Фёдор", "Марина", "Мирон", "Александр",
         "Дарья", "Алина", "Анна", "Милана", "Арсений", "Мария", "Никита", "Тимофей", "Лейла", "Ярослав", "Роман",
         "Владимир", "Дмитрий", "Артём", "Роберт", "Екатерина", "Савелий", "Григорий", "Филипп","Матвей", "Ульяна",
         "Вячеслав", "Наталья", "Мирослав", "Виктория", "Алексей", "Глеб", "Марк", "Всеволод"]
ludi = ["Артур","Кирилл","Стас"]
rost = [180,174,186]
while True:
    def menu():
        print("1 - Посмотреть список людей и из рост \n2 - Добавить человека и его рост в список "
              "\n3 - Удалить человека из списка \n4 - Отсортировать лбдей в алфавитном порядке "
              "\n5 - Показать самого высокого и низкого человека \n6 - Показать людей со средним ростом "
              "\n7 - Добавить имена в список")
        a = int(input())
        if a == 1:
            show()
        if a == 2:
            add()
        elif a == 3:
            delete()
        elif a == 4:
            sort()
        elif a == 5:
            min_max()
        elif a == 6:
            sred()
        elif a == 7:
            inimesed()
    def show():
        print(ludi)
        print(rost)
    def add():
        print("Введите имя человека которого хотите добавить")
        add=input()
        ludi.append(add)
        print("Введите рост этого человека")
        add_rost=input()
        rost.append(add_rost)
        return ludi,rost
    def delete():
        print("Введите имя человека которого хотите удалить")
        name=input()
        for i in range(len(ludi)):
            if ludi[i] == name:
                rost.pop(i)
                ludi.remove(ludi[i])
                return i
        return ludi, rost
    def sort():
        print("....Запуск....")
        s = "█"
        for i in range(101):
            time.sleep(0.05)
            print("\r", "Загрузка", i * s, str(i), '%', end="")
        print("\nЛюди отсортированы")
        abi_p = 0
        abi_i = ""
        n = len(rost)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if ludi[i] > ludi[j]:
                    abi_p = ludi[i]
                    ludi[i] = ludi[j]
                    ludi[j] = abi_p
                    abi_i = rost[i]
                    rost[i] = rost[j]
                    rost[j] = abi_i
        return ludi, rost
    def min_max():
        for i in range (len(rost)):
            if rost[i] == min(rost):
                print(min(rost)," ",ludi[i])
        for i in range (len(rost)):
            if rost[i] == max(rost):
                print(max(rost), " ", ludi[i])
    def sred():
        print("Средний рост трёх первых человек",(ludi[0],ludi[1],ludi[2]), "равен",(rost[0]+rost[1]+rost[2])/3)
    def inimesed():
        print("Сколько имён вы хотите добавить в список? 1 - 50")
        kol_vo=int(input())
        for i in range (kol_vo):
            ludi.append(imena[randint(0,49)])
            a = randint(130, 200)
            rost.append(a)
    menu()