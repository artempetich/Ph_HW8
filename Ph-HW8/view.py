
def get_class():
    return input("Введите номер класса (букву кириллицей, например 1б): ")

def get_subject():
    subject = input("Какой предмет Вас интересует? Математика - введите 1, русский язык - введите 2, английский -введите 3: ")
    while True:
        try:
            int(subject)
            return int(subject)
        except:
            print("Ошибка ввода. Введите одно число: 1 или 2 или 3, без пробелов и запятых еще раз.")

def get_students_name():
    subject = input("Кого вызовем к доске (введите фамилию кириллицей, например Иванов)? Для выхода из журнала нажмите enter  ")
    return subject

def get_score():
    while True:
        score = input("Поставьте оценку от 1 до 5 без пробелов и нажмите Enter  ")
        try: 
            int(score)
            if 0 < int(score) <= 5:
                return score
            else:
                int("dfds")
        except ValueError:
            print("Ошибка ввода. Введите целое число от 1 до 5, без пробелов и запятых")
            continue

def choose_to_close_journal():
    temp_bool = input("Чтобы выйти из журнала, НЕ СОХРАНИВ ИЗМЕНЕНИЯ, нажмите Enter.\n Чтобы сохранить и выйти, введите любой символ  ")
    if temp_bool == '':
        stop_save = False
    else:
        stop_save = True
    return stop_save

def show(text):
    print(text)