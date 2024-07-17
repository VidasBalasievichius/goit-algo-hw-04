with open('salaries.txt', 'w', encoding='utf-8') as file:
    file.write("Alex Korp,3000\n")
    file.write("Nikita Borisenko,2000\n")
    file.write("Sitarama Raju,1000\n")

def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        salary = int(parts[1])
                        total_salary += salary
                        num_developers += 1

        if num_developers > 0:
            average_salary = total_salary / num_developers
        else:
            average_salary = 0

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл '{path}' відсутній.")
        return None, None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None, None

with open('salaries.txt', 'w', encoding='utf-8') as file:
    file.write("Alex Korp,3000\n")
    file.write("Nikita Borisenko,2000\n")
    file.write("Sitarama Raju,1000\n")

total, average = total_salary('salaries.txt')
if total is not None:
    print(f"Загальна зарплата: {total}")
    print(f"Середня зарплата: {average}")

