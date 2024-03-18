from pathlib import Path


def get_cats_info(path: str):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            id, name, age = line.strip().split(',')
            cats_info.append({'id': id, 'name': name, 'age': age})
        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено. Будь ласка, перевірте ім'я файлу та його розташування.")
    except ValueError:
        print("Помилка формату файлу. Будь ласка, перевірте, чи має ваш файл правильний формат.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


relative_path = Path("cats_file.txt")
absolute_path = relative_path.absolute()
print(absolute_path)

cats_info = get_cats_info(absolute_path)
print(cats_info)
