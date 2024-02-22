import sys

def read_numbers_from_file(file_path):
    """Читает список целых чисел из файла."""
    try:
        with open(file_path, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        sys.exit(1)
    except ValueError:
        print(f"Все строки в файле должны быть целыми числами.")
        sys.exit(1)

def calculate_min_moves(nums):
    """Вычисляет минимальное количество ходов для приведения всех чисел к одному."""
    nums.sort()
    median = nums[len(nums) // 2]  # Медиана для нечетного кол-ва элементов
    if len(nums) % 2 == 0:  # Если четное кол-во элементов, берем нижнюю медиану
        median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) // 2
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <путь_к_файлу>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    nums = read_numbers_from_file(file_path)
    min_moves = calculate_min_moves(nums)
    print(min_moves)
