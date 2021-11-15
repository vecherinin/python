# Есть два списка: tutors - имена учеников, klasses - названия их классов.
# Необходимо реализовать генератор или функцию-генератор, возвращающий кортежи вида `(<tutor>, <klass>)`.
#
# Техническое задание
#     1. Количество генерируемых кортежей не должно быть больше длины списка tutors.
#     2. Если в списке klasses меньше элементов, чем в списке tutors,
#     необходимо вывести последние кортежи в виде: `(<tutor>, None)`, например: `('Станислав', None)`
#     3. Если в списке tutors меньше элементов, чем в списке klasses, то смотри пункт 1.
#     4. Генератор возвращает кортежи указанного вида.
#     5. Доказать, что вы создали именно генератор. Вывести все его значения на экран.
#     6. Не используйте в этом задании функции zip и zip_longest.
#     7. Не меняйте исходные списки tutors и klasses.
#     8. Проверьте работоспособность для обоих вариантов:
#     klasses меньше tutors и tutors меньше klasses. Функция должна работать со списками любой длины.


def school_students_gen(tutors, klasses):
    i = 0
    while i < len(tutors):
        if i >= len(klasses):
            yield tutors[i], None
        else:
            yield tutors[i], klasses[i]
        i += 1


# tutors < klasses
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
print('Ученики:', tutors)
print('Классы:', klasses)
# Доказательство создания генератора
generator = school_students_gen(tutors, klasses)
print('Тип объекта:', type(generator))
print('Все значения генератора:')
for gen in generator:
    print(gen)

# tutors > klasses
tutors2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses2 = ['9А', '7В', '9Б', '9В']
print('\nУченики:', tutors2)
print('Классы:', klasses2)
# Доказательство создания генератора
generator2 = school_students_gen(tutors2, klasses2)
print('Тип объекта:', type(generator2))
print('Все значения генератора:')
for gen in generator2:
    print(gen)
