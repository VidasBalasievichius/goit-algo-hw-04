with open('cats.txt', 'w', encoding='utf-8') as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    file.write("60b90c2413067a15887e1ae2,Vika,1\n")
    file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    file.write("60b90c4613067a15887e1ae5,Tessi,5\n")

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
                        "age": int(parts[2]) 
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

cats_info = get_cats_info('cats.txt')
print(cats_info)
