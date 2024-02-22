import json
import sys

def load_json_data(file_path):
    """Загружает данные из JSON-файла."""
    with open(file_path, 'r') as file:
        return json.load(file)

def update_test_values(tests, values_dict):
    """Обновляет значения тестов на основе словаря значений."""
    for test in tests:
        if 'value' in test:
            test['value'] = values_dict.get(str(test['id']), '')
        if 'values' in test:
            update_test_values(test['values'], values_dict)

def main(tests_file_path, values_file_path):
    """Основная функция программы."""
    # Загружаем данные из файлов
    tests_data = load_json_data(tests_file_path)
    values_data = load_json_data(values_file_path)

    # Создаем словарь значений для удобства доступа
    values_dict = {str(value['id']): value['value'] for value in values_data['values']}

    # Создаем копию структуры тестов для отчета
    report_data = {'tests': tests_data['tests']}

    # Обновляем значения в структуре отчета
    update_test_values(report_data['tests'], values_dict)

    # Сохраняем обновленные данные в файл report.json
    with open('report.json', 'w') as file:
        json.dump(report_data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <путь_к_tests.json> <путь_к_values.json>")
        sys.exit(1)
    
    tests_file_path = sys.argv[1]
    values_file_path = sys.argv[2]
    
    main(tests_file_path, values_file_path)
