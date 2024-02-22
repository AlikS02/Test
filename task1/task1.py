import sys

def circular_array_path(n, m):
    """
    Вычисляет путь по круговому массиву.

    Параметры:
    n (int): Длина кругового массива.
    m (int): Длина шага.

    Возвращает:
    list: Путь, состоящий из начальных элементов интервалов.
    """
    if n <= 0 or m <= 0:
        raise ValueError("Длина массива и шаг должны быть больше 0")
    
    path = []  # Путь, который мы будем заполнять
    index = 1  # Начинаем с элемента с индексом 1

    while True:
        interval_end = (index + m - 1) % n
        interval_end = n if interval_end == 0 else interval_end
        path.append(index)

        if interval_end == 1:
            break

        index = interval_end % n
        index = n if index == 0 else index

    return path

def main():
    try:
        # Проверяем количество аргументов
    	if len(sys.argv) != 3:
        	print("Использование: python script.py <длина_массива> <длина_шага>")
        	sys.exit(1)  # Завершаем программу с ошибкой

    	# Получаем параметры n и m из аргументов командной строки
    	n = int(sys.argv[1])
    	m = int(sys.argv[2])

    	# Вызываем функцию и выводим результат
    	path = circular_array_path(n, m)
    	print("Путь по массиву:", path)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
