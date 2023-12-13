#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    school = []

    while True:
        cmd = input(">>> ")

        if cmd == "exit":
            print("Завершение работы программы...")
            break

        elif cmd == "help":
            print("add - добавление нового класса")
            print("list - вывод список текущих классов")
            print("remove - удаление класса")
            print("change - изменение существующего класса")
            print("getsum - вывод общего количества учащихся")
            print("exit - выход из программы")

        elif cmd == "add":
            class_name = input("Название класса: ")
            class_students = input("Количество учеников: ")

            new_class = {
                'name': class_name,
                'students': class_students
            }
            school.append(new_class)

        elif cmd == "list":
            if len(school) > 0:
                for object_class in school:
                    print(f"Класс {object_class['name']}. "
                        f"Количество учеников: {object_class['students']}"
                    )
            else:
                print("Нет созданных классов")

        elif cmd == "remove":
            remove_class_name = input("Введите удаляемый класс: ")

            for object_class in school:
                removed = False

                if object_class['name'] == remove_class_name:
                    school.remove(object_class)
                    removed = True
                    break

            if removed == False:
                print("Класс не был найден")
            else:
                print("Класс успешно удалён")
            
        elif cmd == "change":
            changed_class = input("Введите название класса для изменения: ")
            changed = False

            for object_class in school:
                if object_class['name'] == changed_class:
                    object_class['name'] = input("Введите новое имя класса: ")
                    object_class['students'] = input("Введите новое "
                                                     "количество учеников: ")
                    changed = True
                    break
            
            if changed == False:
                print("Класс не найден")
            else:
                print("Класс изменён")

        elif cmd == "getsum":
            class_sum = 0

            for object_class in school:
                class_sum += int(object_class['students'])

            print(f"Общее количество учащихся: {class_sum}")

        else:
            print("Введённая команда не существует. Введите help")
        