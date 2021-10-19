zoo = ['cat', 'dog', 'rabbit']
zoo.append('crocodile')
a2 = [1, 2, 4, 5, 6, 7, 8]
a2.pop(6)
a1 = [1, 2, 3, 4, ]
a1.extend('five')
my_list = [1, 3]
my_list.insert(-1, 4)
zoo.remove('cat')
s1 = [4, 45, 51, 21, 45, 55, 77]
s1.index(77)
random = [1, 2, 12, 21, 1, 1, 1, ]
random.count(23)
cars1 = ['Ford', 'BMW', 'Volvo','Toyota', 'Tesla']
cars = ['Ford', 'BMW', 'Volvo','Toyota', 'Tesla']
cars.sort()
cars1.reverse()
zoo.copy()
cars1.clear()
if __name__ == '__main__':
    print(zoo)  # Добавляет элемент в конец списка
    print(a1)  # Расширяет список list, добавляя в конец все элементы списка L
    print(my_list)  # Вставляет на i-ый элемент значение x
    print(zoo)  # Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
    print(a2)  # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
    print(s1)  # Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
    print(random)  # Возвращает количество элементов со значением x
    print(cars)  # Сортирует список на основе функции
    print(cars1) #  Разворачивает список
    print(zoo)  # Поверхностная копия списка
    print(cars1) #  Очищает список