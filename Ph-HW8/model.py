import view
import re


global class_info
class_info = {}

global class_list
class_list = []

global subject_class_info
subject_class_info = {}

global path
path = "JOURNAL\data_base.txt"

global class_num
class_num = 0


def get_data_base():
    global path
    path = "JOURNAL\data_base.txt"

    global data_base
    data_base = {}

    global students_names
    students_names = []

    our_str = ''
    # записываем данные в строку
    with open(path, 'r', encoding='UTF-8') as file:
        for el in file:
            our_str += el
#    создаем словарик 1 уровня
    print(our_str)
    our_list = our_str[:-4].strip().replace("'", "").replace('\n', '').replace(' ', '').replace(
        ':{', ';').replace('},', ';').replace('{', '').replace('}', '').split('--')
    res_res_dic = {}
    our_dic = {}

    for i in range(0, len(our_list), 2):
        our_dic[our_list[i]] = our_list[i+1]
        str_string = our_dic[our_list[i]]
        list_list = str_string.split(';')

#    содаем словарик 2 уровня
        new_dic = {}
        for j in range(0, len(list_list), 2):
            new_dic[list_list[j]] = list_list[j+1]
            str_str_str = new_dic[list_list[j]]
            lis_lis_lis = re.split(':|,', str_str_str)

#    содаем словарик 3 уровня
            new_new_dic = {}
            for z in range(0, len(lis_lis_lis), 2):
                new_new_dic[lis_lis_lis[z].strip()] = lis_lis_lis[z+1]
# собирем словарь из словариков
            res_res_dic[list_list[j]] = new_new_dic

        temp_dic = res_res_dic.copy()
        data_base[our_list[i]] = temp_dic

    view.show("Вы открыли журнал")


def get_class_list():
    global class_list
    class_list = []
    for el in data_base:
        el = el.strip()
        class_list.append(el)


def open_class_num():
    global class_num
    # """ проверяем наличие класса с таким номером """
    while True:
        class_num = view.get_class()

        for i in class_list:
            if i == class_num:
                print(class_num)
                return class_num
        else:
            view.show("Нет такого класса, попробуйте ввести номер класса еще раз")
            continue


def get_class_info():
    global class_info
    class_info = {}

    for el in data_base:

        if el == class_num:
            class_info = data_base[el]
            view.show(class_info)


def get_subject_class_info():
    global subject
    global subject_class_info
    subject_class_info = {}
    subject = ''
    subj_num = view.get_subject()
    match subj_num:
        case 1:
            subject = 'математика'
        case 2:
            subject = 'русский'
        case 3:
            subject = 'английский'

    for el in class_info:

        if el == subject:
            subject_class_info = class_info[el]
            view.show(subject_class_info)


def call_to_the_balckboard():
    global student_info
    student_info = ''
    global student
    global students_names
    a = True
    while a:
        student = ''
        student = view.get_students_name()

        if student == '':
            exit()

        if student in subject_class_info:

            for el in subject_class_info:

                if el.strip() == student:
                    student_info = subject_class_info[el]
                    print(f"Оценки ученика: {student_info}")
                    a = False
        else:

            continue


def add_new_score():
    global data_base
    global student_info
    global score
    global student
    score = 0
    score = view.get_score()
    student_info += ' ' + score
    temp_base1 = data_base[class_num]
    temp_base2 = temp_base1[subject]
    temp_base2[student] = student_info

    if view.choose_to_close_journal():
        res_string = ''
        for i in range(0, len(class_list)):
            res_string += class_list[i] + '--'
            res_string += str(data_base[class_list[i]]) + "--"
        print(res_string)
        with open(path, 'w', encoding='UTF-8') as file:

            file.writelines(res_string)
        view.show(f"Оценка {score} ученику {student} записана в журнал")

    else:
        view.show("Вы вышли не сохранив изменения")
        exit()