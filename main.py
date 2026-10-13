import os
import time

# ==========================================
# Задание 1: Флаг Бангладеш
# Зеленый фон, красный круг
# ==========================================
def draw_flag():
    green_bg = "\033[42m  \033[0m"  # Зеленый фон
    red_bg = "\033[41m  \033[0m"    # Красный фон
    
    print("Флаг Бангладеш:")
    for i in range(10):
        line = ""
        for j in range(20):
            # Уравнение круга в центре
            if (i - 4.5)**2 + (j - 9.5)**2 <= 9:
                line += red_bg
            else:
                line += green_bg
        print(line)
    print("\n")

# ==========================================
# Задание 2: Узор 'b'
# Повторяющийся узор в виде ступеньки
# ==========================================
def draw_pattern():
    pattern = [
        "██████",
        "█     ",
        "██████",
        "█    █",
        "██████"
    ]
    print("Узор 'b':")
    for line in pattern:
        print(line)
    print("\n")

# ==========================================
# Задание 3: Анимация (3-4 кадра)
# Использование os.system для очистки экрана и управление курсором
# ==========================================
def run_animation():
    frames = [
        "  O  ",
        " O   ",
        "O    ",
        " O   "
    ]
    print("Запуск анимации...")
    time.sleep(1)
    
    for _ in range(3): # Цикл 3 раза
        for frame in frames:
            # Очистка экрана (Windows: 'cls', Mac/Linux: 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            # Перемещение курсора в строку 5, столбец 10
            print("\033[5;10H" + frame)
            time.sleep(0.5)

# ==========================================
# Задание 4: Диаграмма процентного соотношения
# Условие: Сумма по модулю первых 125 чисел и вторых 125 чисел
# ==========================================
def draw_diagram():
    try:
        with open('sequence.txt', 'r') as f:
            numbers = [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("ВНИМАНИЕ: Файл sequence.txt не найден. Используются тестовые данные.")
        numbers = [i for i in range(1, 251)] # Тестовые данные от 1 до 250

    if len(numbers) < 250:
        print("Ошибка: В файле sequence.txt недостаточно чисел (нужно минимум 250).")
        return

    first_125 = numbers[:125]
    second_125 = numbers[125:250]

    # Вычисление сумм по модулю
    sum1 = sum(abs(x) for x in first_125)
    sum2 = sum(abs(x) for x in second_125)
    total = sum1 + sum2

    p1 = (sum1 / total) * 100 if total != 0 else 0
    p2 = (sum2 / total) * 100 if total != 0 else 0

    print("Диаграмма процентного соотношения (Вариант 2):")
    print(f"Сумма по модулю первых 125: {sum1:.2f} ({p1:.1f}%)")
    print(f"Сумма по модулю вторых 125: {sum2:.2f} ({p2:.1f}%)")
    print("\nДиаграмма:")
    # Горизонтальные полосы
    bar1 = '#' * int(p1 // 2)
    bar2 = '#' * int(p2 // 2)
    print(f"Первые 125:  [{bar1:<50}] {p1:.1f}%")
    print(f"Вторые 125:  [{bar2:<50}] {p2:.1f}%")
    print("\n")

# ==========================================
# Допзадание: График функции y = 2x + 3
# Первая четверть, минимум 9 строк в высоту
# ==========================================
# ==========================================
# Допзадание: График функции y = 2x + 3
# Первая четверть, минимум 9 строк в высоту
# ==========================================
def draw_graph():
    width = 50
    height = 15
    max_x = 20
    max_y = 2 * max_x + 3 # 43

    # Создание пустой сетки
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # Рисование осей
    for i in range(height):
        grid[i][0] = '|'
    for j in range(width):
        grid[height-1][j] = '-'
    grid[height-1][0] = '+'

    # Построение точек графика
    for x in range(max_x + 1):
        y = 2 * x + 3
        # Масштабирование координат под размер сетки
        grid_x = int((x / max_x) * (width - 2)) + 1
        grid_y = int((1 - y / max_y) * (height - 2)) + 1

        if 0 <= grid_y < height and 0 <= grid_x < width:
            grid[grid_y][grid_x] = '*'

    # Вывод с использованием управления курсором
    print("\033[2J") # Очистка экрана
    print("График функции y = 2x + 3 (Первая четверть):")
    
    for i in range(height):
        # Перемещение курсора в строку i+3 (чтобы оставить место для заголовка)
        print(f"\033[{i+3};1H" + "".join(grid[i]))
        
    # Перемещение курсора вниз, чтобы не перезаписывать текст
    print(f"\033[{height+4};1H")

# ==========================================
# ГЛАВНАЯ ФУНКЦИЯ
# ==========================================
if __name__ == "__main__":
    draw_flag()
    draw_pattern()
    run_animation()
    draw_diagram()
    draw_graph()