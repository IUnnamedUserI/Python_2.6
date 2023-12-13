#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    member_list = []

    while True:
        cmd = input(">>> ")

        if cmd == "help":
            print("add - добавление новых записей")
            print("find - найти запись по фамилии")

        elif cmd == "add":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            date = tuple(map(int, input("Введите дату рождения: ").split('.')))
            
            new_member = {'surname': surname,
                            'name': name,
                            'phone': phone,
                            'date': date
                        }
            member_list.append(new_member)
            member_list.sort(key=lambda item: item.get('phone')[:3])

        elif cmd == "list":
            for member in member_list:
                print(f"{member['surname']} {member['name']}, "
                      f"{member['phone']}, {member['date']}")
                
        elif cmd == "find":
            surname = input("Введите фамилию: ")
            count = 0

            for member in member_list:
                if member['surname'] == surname:
                    print(f"{member['surname']} {member['name']}, "
                      f"{member['phone']}, {member['date']}")
                    count += 1
                
                if count == 0:
                    print("Записи не найдены")

        elif cmd == "exit":
            print("Завершение работы программы...")
            break

        else:
            print(f"Команды {cmd} не существует")
