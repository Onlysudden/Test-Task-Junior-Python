Задача №1.
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

def task(array):
    pass

print(task("111111111110000000000000000"))
# >> OUT: 11
…



Задача №2.

В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:

А: 642
Б: 412
В:....



Задача №3.
Когда пользователь заходит на страницу урока, мы сохраняем время его захода. Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), мы фиксируем время выхода с урока. Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).