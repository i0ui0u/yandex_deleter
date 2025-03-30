import os
import subprocess
import ctypes
import shutil  # Для удаления папок


def get_username():
    return os.environ.get("USERNAME", "")  # Упрощенная проверка


if ctypes.windll.shell32.IsUserAnAdmin():
    username = get_username()

    # Формируем пути через os.path.join (безопаснее)
    local_path = os.path.join(f"C:\\Users\\{username}", "AppData", "Local", "Yandex")
    roaming_path = os.path.join(f"C:\\Users\\{username}", "AppData", "Roaming", "Yandex")

    # Проверяем существование путей
    paths_exist = True
    if not os.path.exists(local_path):
        print("Не найден путь Local/Yandex")
        paths_exist = False
    if not os.path.exists(roaming_path):
        print("Не найден путь Roaming/Yandex")
        paths_exist = False

    if not paths_exist:
        input("Нажмите любую клавишу для выхода...")
        exit()

    if input("Удалить Yandex? (Y/N): ").lower() == "y":
        print("Завершение процесса...")
        try:
            subprocess.run(["taskkill", "/F", "/IM", "browser.exe"], check=True)
        except subprocess.CalledProcessError:
            print("Процесс не найден или не может быть завершен")

        try:
            # Удаляем папки с содержимым
            shutil.rmtree(local_path)
            shutil.rmtree(roaming_path)
            print("Yandex успешно удален!")
        except Exception as e:
            print(f"Ошибка удаления: {e}")
        input("Нажмите любую клавишу...")
else:
    print("Запустите скрипт от имени администратора!")
    input("Нажмите любую клавишу...")