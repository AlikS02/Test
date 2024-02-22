import sys

def read_circle_parameters(circle_file_path):
    """Читает параметры окружности из файла."""
    with open(circle_file_path, 'r') as file:
        circle_center = tuple(map(float, file.readline().split()))
        circle_radius = float(file.readline())
    return circle_center, circle_radius

def read_points(points_file_path):
    """Читает координаты точек из файла."""
    with open(points_file_path, 'r') as file:
        points_list = [tuple(map(float, line.split())) for line in file]
    return points_list

def determine_point_position(circle_center, circle_radius, point_coordinates):
    """Определяет положение точки относительно окружности."""
    distance_to_center = ((point_coordinates[0] - circle_center[0])**2 + (point_coordinates[1] - circle_center[1])**2)**0.5
    if distance_to_center < circle_radius:
        return 1  # Точка внутри окружности
    elif distance_to_center == circle_radius:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

def main(circle_params_file, points_file):
    """Основная функция, которая вызывает другие функции и выводит результаты."""
    circle_center, circle_radius = read_circle_parameters(circle_params_file)
    points_list = read_points(points_file)
    
    for point_coordinates in points_list:
        point_position = determine_point_position(circle_center, circle_radius, point_coordinates)
        print(point_position)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_с_параметрами_окружности> <файл_с_координатами_точек>")
        sys.exit(1)
    
    circle_params_file = sys.argv[1]
    points_file = sys.argv[2]
    main(circle_params_file, points_file)
