from pathlib import Path


def total_salary(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [int(line.strip().split(',')[1]) for line in file]

        total_sum = sum(salaries)
        average_salary = total_sum / len(salaries)
        return total_sum, average_salary

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху до файлу.")
        return None, None
    except ValueError:
        print("Помилка при обробці даних. Переконайтеся, що дані в файлі відформатовані коректно.")
        return None, None


relative_path = Path("salary_file.txt")
absolute_path = relative_path.absolute()

total_sum, average_salary = total_salary(absolute_path)
if total_sum is not None and average_salary is not None:
    print(
        f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average_salary}")
