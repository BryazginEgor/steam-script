import os


steam_path = r"E:\Steam\steamapps\libraryfolders.vdf"

# Получение всех папок Steam\steamapps на всем пк
def get_steam_paths(steam_library_folders):
    steam_path = []
    # Открывает файл Steam\steamapps\libraryfolders.vdf
    with open(steam_library_folders, 'r') as file:
        fileLines = file.readlines()
        # Ищет "path" в каждой строке
        for line in fileLines:
            if "path" in line:
                steam_path.append(line[11:-2] + "\steamapps")

    return steam_path


# Читает манифест файлы в каждой папке Steam\steamapps
def get_manifest(steam_path):
    try:
        # Для каждого файла в steam_path
        for filename in os.listdir(steam_path):
            # Получение общего пути для каждого файла
            f = os.path.join(steam_path, filename)
            # Если файл оканчивается на .acf
            if os.path.isfile(f) and filename.endswith('.acf'):
                with open(f, 'r') as file:
                    fileLines = file.readlines()
                    line = fileLines[7].strip()
                    print(line[15:-1])
    # Если директория отсутствует
    except FileNotFoundError as e:
        print(f"No such directory: {e.filename}")

steam_paths = get_steam_paths(steam_path)

for i in range(len(steam_paths)):
    get_manifest(steam_paths[i])

