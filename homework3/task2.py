def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_info)
                else:
                    print(f"Неправильний формат рядка у файлі: {line}")
        
        return cats_info
    
    except FileNotFoundError:
        print(f"Файл '{path}' відсутній.")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []
