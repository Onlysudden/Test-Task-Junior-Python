"""
Когда пользователь заходит на страницу урока, мы сохраняем время его захода. Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), мы фиксируем время выхода с урока. Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
"""

# При разборе задачи заметил, что встречается всего 4 типа вложенности таймстепов:
# Вариант 1 внутренний:   Вариант 2 слева:   Вариант 3 справа:   Вариант 4 внутренний наоборот:
#       1----1                  1----1             1----1              1----1 
#        2--2                 2--2                     2--2          2--------2
#
# Далее подпишу в if какой это вариант проверки

# Создал функцию для очистки аномалий в таймстепах
def clean_times(dirt_list:list) -> list:
    clean_list = []
    i = 0
    # В цикле буду удалять лишние пары, пока не останется одна пара
    while len(dirt_list) != 2:
        # Проверка на вариант 1
        if dirt_list[i] >= dirt_list[i+2] and dirt_list[i+1] <= dirt_list[i+3]:
            # Первая пара вложена в вторую, первую удаляем
            del dirt_list[0:2]
        
        # Проверка на вариант 2
        elif dirt_list[i] >= dirt_list[i+2] and dirt_list[i+1] >= dirt_list[i+3] and dirt_list[i+3] >= dirt_list[i]:
            # Сохраняем крайние значения таймстепа, удаляем старые значения, вставляем новые
            one, two = dirt_list[i+2], dirt_list[i+1]
            del dirt_list[0:4]
            dirt_list.insert(0, two)
            dirt_list.insert(0, one)

        # Проверка на вариант 3
        elif dirt_list[i] <= dirt_list[i+2] and dirt_list[i+1] <= dirt_list[i+3] and dirt_list[i+2] <= dirt_list[i+1]:
            # Сохраняем крайние значения таймстепа, удаляем старые значения, вставляем новые
            one, two = dirt_list[i], dirt_list[i+3]
            del dirt_list[0:4]
            dirt_list.insert(0, two)
            dirt_list.insert(0, one)

        # Проверка на вариант 4
        elif dirt_list[i] <= dirt_list[i+2] and dirt_list[i+1] >= dirt_list[i+3]:
            # Вторая пара вложена в первую, вторую удаляем
            del dirt_list[2:4]
        
        else:
            # Пары не соприкасаются, первую пару сохраняем в новый список и удаляем в старом
            clean_list.append(dirt_list.pop(0))
            clean_list.append(dirt_list.pop(0))
    # Сохраняем последние два значения в старом списке
    clean_list.append(dirt_list.pop(0))
    clean_list.append(dirt_list.pop(0))
    return clean_list

def appearance(intervals: dict) -> int:
    # Сохраняем значения из словаря и проводим их через очищающую функцию
    s1, s2 = clean_times(intervals["lesson"])
    pupil = clean_times(intervals["pupil"])
    tutor = clean_times(intervals["tutor"])

    sum = 0
    # Cнова проверяем вложенность таймстепов через два цикла
    for i in range(0, len(tutor), 2):
        for j in range(0, len(pupil), 2):
            # Проверка на вариант 1
            if tutor[i] <= pupil[j] and tutor[i+1] >= pupil[j+1]:
                # Проверка на крайние значения таймстепа урока
                # Под эту проверку можно также сделать отдельную функцию
                # Таймстеп вложен в таймстеп урока
                if pupil[j] >= s1 and pupil[j+1] <= s2:
                    sum += (pupil[j+1] - pupil[j])
                # Таймстеп выходит за таймстеп урока слева
                elif pupil[j] <= s1 and pupil[j+1] <= s2:
                    sum += (pupil[j+1] - s1)
                # Таймстеп выходит за таймстеп урока справа
                elif pupil[j] >= s1 and pupil[j+1] >= s2:
                    sum += (s2 - pupil[j])
                # Иначе таймстеп занимает весь урок
                else:
                    sum += (s2 - s1)

            # Проверка на вариант 2
            elif tutor[i] >= pupil[j] and tutor[i+1] >= pupil[j+1] and tutor[i] <= pupil[j+1]:
                if tutor[i] >= s1 and pupil[j+1] <= s2:
                    sum += (pupil[j+1] - tutor[i])
                elif tutor[i] <= s1 and pupil[j+1] <= s2:
                    sum += (pupil[j+1] - s1)
                elif tutor[i] >= s1 and pupil[j+1] >= s2:
                    sum += (s2 - tutor[i])
                else:
                    sum += (s2 - s1)

            # Проверка на вариант 3
            elif tutor[i] <= pupil[j] and tutor[i+1] >= pupil[j] and tutor[i+1] <= pupil[j+1]:
                if pupil[j] >= s1 and tutor[i+1] <= s2:
                    sum += (tutor[i+1] - pupil[j])
                elif pupil[j] <= s1 and tutor[i+1] <= s2:
                    sum += (tutor[i+1] - s1)
                elif pupil[j] >= s1 and tutor[i+1] >= s2:
                    sum += (s2 - pupil[j])
                else:
                    sum += (s2 - s1)
            
            # Проверка на вариант 4
            elif tutor[i] >= pupil[j] and tutor[i+1] <= pupil[j+1]:
                if tutor[i] >= s1 and tutor[i+1] <= s2:
                    sum += (tutor[i+1] - tutor[i])
                elif tutor[i] <= s1 and tutor[i+1] <= s2:
                    sum += (tutor[i+1] - s1)
                elif tutor[i] >= s1 and tutor[i+1] >= s2:
                    sum += (s2 - tutor[i])
                else:
                    sum += (s2 - s1)
            
    return sum

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       print(test_answer)
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'